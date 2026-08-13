"""Offline Trace the Ace Submission 02 M0 inference entrypoint.

The generated archive copies this file to ``main.py``.  It intentionally uses
only NumPy and pandas at inference time and implements exactly the frozen
three-feature M0 control.
"""
from __future__ import annotations

import csv
import re
from pathlib import Path
from typing import Iterable, Mapping

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ASSETS = ROOT / "assets"

TRANSCRIPT_COLUMNS = [
    "session_id",
    "utterance_id",
    "role",
    "content",
    "timestamp",
]
FEATURE_COLUMNS = [
    "n_student_words",
    "numeric_turns_per_word",
    "digit_chars_per_word",
]
WORD_RE = re.compile(r"[a-z0-9]+(?:'[a-z]+)?", re.I)
DIGIT_RE = re.compile(r"\d")


def session_features_from_rows(
    rows: Iterable[Mapping[str, str]],
) -> np.ndarray:
    """Return the exact three student-only M0 features for one session."""

    n_student_words = 0
    numeric_turns = 0
    digit_chars = 0
    for row in rows:
        if row.get("role") != "student":
            continue
        text = row.get("content") or ""
        n_student_words += len(WORD_RE.findall(text))
        numeric_turns += int(bool(DIGIT_RE.search(text)))
        digit_chars += len(DIGIT_RE.findall(text))

    if not n_student_words:
        return np.asarray([np.nan, np.nan, np.nan], dtype=np.float64)
    denominator = float(n_student_words)
    return np.asarray(
        [
            denominator,
            numeric_turns / denominator,
            digit_chars / denominator,
        ],
        dtype=np.float64,
    )


def session_features(path: Path) -> np.ndarray:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != TRANSCRIPT_COLUMNS:
            raise RuntimeError("transcript schema mismatch")
        return session_features_from_rows(reader)


def sigmoid(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=np.float64)
    result = np.empty_like(values)
    positive = values >= 0
    result[positive] = 1.0 / (1.0 + np.exp(-values[positive]))
    exponential = np.exp(values[~positive])
    result[~positive] = exponential / (1.0 + exponential)
    return result


def predict_feature_matrix(
    feature_matrix: np.ndarray,
    model: Mapping[str, np.ndarray],
) -> np.ndarray:
    """Apply the stored M0 state, including the quiet-session fallback."""

    matrix = np.asarray(feature_matrix, dtype=np.float64)
    if matrix.ndim != 2 or matrix.shape[1] != len(FEATURE_COLUMNS):
        raise RuntimeError("M0 feature matrix shape mismatch")

    minimum = int(np.asarray(model["min_student_words"]).reshape(-1)[0])
    base_rate = float(np.asarray(model["eligible_base_rate"]).reshape(-1)[0])
    medians = np.asarray(model["feature_median"], dtype=np.float64)
    scaler_mean = np.asarray(model["scaler_mean"], dtype=np.float64)
    scaler_scale = np.asarray(model["scaler_scale"], dtype=np.float64)
    coefficients = np.asarray(model["coef"], dtype=np.float64)
    intercept = float(np.asarray(model["intercept"]).reshape(-1)[0])

    if any(value.shape != (len(FEATURE_COLUMNS),) for value in (
        medians,
        scaler_mean,
        scaler_scale,
        coefficients,
    )):
        raise RuntimeError("M0 asset shape mismatch")
    if not np.isfinite(base_rate) or not 0.0 <= base_rate <= 1.0:
        raise RuntimeError("invalid quiet-session base rate")
    if not np.isfinite(scaler_scale).all() or np.any(scaler_scale <= 0):
        raise RuntimeError("invalid scaler state")

    probabilities = np.full(matrix.shape[0], base_rate, dtype=np.float64)
    eligible = matrix[:, 0] >= minimum
    if np.any(eligible):
        eligible_matrix = matrix[eligible].copy()
        missing = np.where(np.isnan(eligible_matrix))
        eligible_matrix[missing] = medians[missing[1]]
        standardized = (eligible_matrix - scaler_mean) / scaler_scale
        scores = standardized @ coefficients + intercept
        probabilities[eligible] = sigmoid(scores)

    if not np.isfinite(probabilities).all():
        raise RuntimeError("non-finite predictions")
    if np.any((probabilities < 0.0) | (probabilities > 1.0)):
        raise RuntimeError("predictions outside [0,1]")
    return probabilities


def main() -> None:
    submission_format = pd.read_csv(
        DATA / "submission_format.csv", dtype={"response_id": str}
    )
    test_features = pd.read_csv(
        DATA / "test_features.csv",
        dtype={"response_id": str, "session_id": str},
    )
    if list(submission_format.columns) != ["response_id", "probability"]:
        raise RuntimeError("submission format mismatch")
    required = {"response_id", "session_id", "learning_objective"}
    if not required.issubset(test_features.columns):
        raise RuntimeError("test feature schema mismatch")
    if not submission_format["response_id"].is_unique:
        raise RuntimeError("duplicate response_id in submission format")
    if not test_features["response_id"].is_unique:
        raise RuntimeError("duplicate response_id in test features")

    frame = submission_format[["response_id"]].merge(
        test_features[["response_id", "session_id", "learning_objective"]],
        on="response_id",
        how="left",
        validate="one_to_one",
        sort=False,
    )
    if frame[["session_id", "learning_objective"]].isna().any().any():
        raise RuntimeError("test feature coverage mismatch")
    if frame["response_id"].tolist() != submission_format["response_id"].tolist():
        raise RuntimeError("response order changed")

    sessions = sorted(frame["session_id"].astype(str).unique())
    feature_by_session = {}
    for session_id in sessions:
        transcript = DATA / "test_transcripts" / f"{session_id}.csv"
        if not transcript.is_file():
            raise RuntimeError("transcript coverage mismatch")
        feature_by_session[session_id] = session_features(transcript)
    feature_matrix = np.vstack(
        [feature_by_session[session_id] for session_id in frame["session_id"]]
    )

    with np.load(ASSETS / "m0_model.npz", allow_pickle=False) as model:
        probabilities = predict_feature_matrix(feature_matrix, model)
    output = pd.DataFrame(
        {
            "response_id": submission_format["response_id"].astype(str),
            "probability": probabilities,
        }
    )
    if list(output.columns) != ["response_id", "probability"]:
        raise RuntimeError("output schema mismatch")
    if len(output) != len(submission_format) or not output["response_id"].is_unique:
        raise RuntimeError("output identity mismatch")
    output.to_csv(ROOT / "submission.csv", index=False, lineterminator="\n")


if __name__ == "__main__":
    main()
