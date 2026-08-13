"""Offline Trace the Ace Submission 03 M1-cal inference entrypoint.

The generated archive copies this file to ``main.py``.  It implements only the
frozen M1-prime representation followed by the frozen deployment Platt map.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Iterable, Mapping

import numpy as np
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import HashingVectorizer


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
ASSETS = ROOT / "assets"

SUBMISSION_ID = "SUBMISSION_03_M1_CAL_CONTROL"
MODEL_STATE_KEYS = {
    "text_coef",
    "structural_coef",
    "base_intercept",
    "structural_medians",
    "scaler_mean",
    "scaler_scale",
    "platt_slope",
    "platt_intercept",
}
TRANSCRIPT_COLUMNS = [
    "session_id",
    "utterance_id",
    "role",
    "content",
    "timestamp",
]
ROLE_MARKERS = {
    "tutor": "__ROLE_TUTOR__",
    "student": "__ROLE_STUDENT__",
    "background": "__ROLE_BACKGROUND__",
}
ORDINARY_COLUMNS = [
    "n_turns",
    "n_student_words",
    "numeric_turns_per_word",
    "digit_chars_per_word",
]
N_HASH_FEATURES = 262_144
WORD_RE = re.compile(r"[a-z0-9]+(?:'[a-z]+)?", re.I)
DIGIT_RE = re.compile(r"\d")


def normalize_text(text: str) -> str:
    """Apply the exact historical internal-whitespace normalization."""

    return " ".join((text or "").split())


def transcript_blocks_from_rows(
    rows: Iterable[Mapping[str, str]],
) -> tuple[str, np.ndarray]:
    """Return exact M1-prime text and exact four ordinary covariates."""

    parts: list[str] = []
    n_turns = 0
    n_student_words = 0
    numeric_turns = 0
    digit_chars = 0
    for row in rows:
        n_turns += 1
        role = row.get("role")
        if role not in ROLE_MARKERS:
            raise RuntimeError(f"unexpected transcript role: {role!r}")
        content = row.get("content") or ""
        parts.append(f"{ROLE_MARKERS[role]} {normalize_text(content)}")
        if role == "student":
            n_student_words += len(WORD_RE.findall(content))
            numeric_turns += int(bool(DIGIT_RE.search(content)))
            digit_chars += len(DIGIT_RE.findall(content))

    denominator = float(n_student_words) if n_student_words else float("nan")
    ordinary = np.asarray(
        [
            float(n_turns),
            float(n_student_words) if n_student_words else float("nan"),
            numeric_turns / denominator,
            digit_chars / denominator,
        ],
        dtype=np.float64,
    )
    return "\n".join(parts), ordinary


def transcript_blocks(path: Path) -> tuple[str, np.ndarray]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != TRANSCRIPT_COLUMNS:
            raise RuntimeError("transcript schema mismatch")
        return transcript_blocks_from_rows(reader)


def make_vectorizer() -> HashingVectorizer:
    return HashingVectorizer(
        analyzer="word",
        ngram_range=(1, 2),
        n_features=N_HASH_FEATURES,
        alternate_sign=False,
        binary=False,
        norm="l2",
        lowercase=True,
        token_pattern=r"(?u)\b\w+\b",
        dtype=np.float32,
    )


def stable_sigmoid(values: np.ndarray) -> np.ndarray:
    values = np.asarray(values, dtype=np.float64)
    result = np.empty_like(values)
    positive = values >= 0
    result[positive] = 1.0 / (1.0 + np.exp(-values[positive]))
    exponential = np.exp(values[~positive])
    result[~positive] = exponential / (1.0 + exponential)
    return result


def validate_state(model: Mapping[str, np.ndarray]) -> None:
    available = set(getattr(model, "files", model.keys()))
    if available != MODEL_STATE_KEYS:
        raise RuntimeError("M1-cal asset keys mismatch")
    required_shapes = {
        "text_coef": (N_HASH_FEATURES,),
        "structural_coef": (len(ORDINARY_COLUMNS),),
        "base_intercept": (1,),
        "structural_medians": (len(ORDINARY_COLUMNS),),
        "scaler_mean": (len(ORDINARY_COLUMNS),),
        "scaler_scale": (len(ORDINARY_COLUMNS),),
        "platt_slope": (1,),
        "platt_intercept": (1,),
    }
    for name, shape in required_shapes.items():
        value = np.asarray(model[name])
        if value.shape != shape or not np.isfinite(value).all():
            raise RuntimeError(f"invalid M1-cal asset: {name}")
    scale = np.asarray(model["scaler_scale"], dtype=np.float64)
    if np.any(scale <= 0):
        raise RuntimeError("invalid structural scaler state")
    if float(np.asarray(model["platt_slope"]).reshape(-1)[0]) <= 0:
        raise RuntimeError("invalid deployment Platt slope")


def predict_blocks(
    text_matrix: sparse.csr_matrix,
    ordinary_matrix: np.ndarray,
    model: Mapping[str, np.ndarray],
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Predict from frozen fitted state, retaining component outputs for tests."""

    validate_state(model)
    text = sparse.csr_matrix(text_matrix, dtype=np.float32)
    ordinary = np.asarray(ordinary_matrix, dtype=np.float64)
    if text.shape[1] != N_HASH_FEATURES or ordinary.shape != (
        text.shape[0],
        len(ORDINARY_COLUMNS),
    ):
        raise RuntimeError("M1-cal inference matrix shape mismatch")

    medians = np.asarray(model["structural_medians"], dtype=np.float64)
    scaler_mean = np.asarray(model["scaler_mean"], dtype=np.float64)
    scaler_scale = np.asarray(model["scaler_scale"], dtype=np.float64)
    imputed = ordinary.copy()
    missing = np.where(np.isnan(imputed))
    imputed[missing] = medians[missing[1]]
    standardized = ((imputed - scaler_mean) / scaler_scale).astype(np.float32)
    design = sparse.hstack(
        [text, sparse.csr_matrix(standardized)], format="csr", dtype=np.float32
    )
    coefficient = np.concatenate(
        [
            np.asarray(model["text_coef"]),
            np.asarray(model["structural_coef"]),
        ]
    ).reshape(1, -1)
    # Preserve sklearn's ``decision_function`` sparse multiplication shape.
    # Multiplying by a 1-D vector changes float32 summation order enough to
    # violate the transport equivalence gate on otherwise identical state.
    # Add the fitted float32 intercept before widening, matching sklearn's
    # float32 ``decision_function`` arithmetic exactly.
    raw_score = np.asarray(
        design @ coefficient.T + np.asarray(model["base_intercept"]),
        dtype=np.float64,
    ).reshape(-1)
    calibrated_score = (
        float(np.asarray(model["platt_slope"]).reshape(-1)[0]) * raw_score
        + float(np.asarray(model["platt_intercept"]).reshape(-1)[0])
    )
    probability = stable_sigmoid(calibrated_score)
    if not np.isfinite(probability).all() or np.any(
        (probability < 0.0) | (probability > 1.0)
    ):
        raise RuntimeError("invalid M1-cal predictions")
    return raw_score, calibrated_score, probability


def load_model_manifest() -> dict:
    manifest = json.loads((ASSETS / "model_manifest.json").read_text(encoding="utf-8"))
    if manifest.get("schema_version") != 1 or manifest.get("submission_id") != SUBMISSION_ID:
        raise RuntimeError("model manifest identity mismatch")
    if manifest.get("objective_information_present") is not False:
        raise RuntimeError("objective exclusion manifest mismatch")
    return manifest


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

    # ``learning_objective`` is schema-checked above and intentionally never merged.
    frame = submission_format[["response_id"]].merge(
        test_features[["response_id", "session_id"]],
        on="response_id",
        how="left",
        validate="one_to_one",
        sort=False,
    )
    if frame["session_id"].isna().any():
        raise RuntimeError("test feature coverage mismatch")
    if frame["response_id"].tolist() != submission_format["response_id"].tolist():
        raise RuntimeError("response order changed")

    sessions = sorted(frame["session_id"].astype(str).unique())
    texts: list[str] = []
    ordinary_by_session: dict[str, np.ndarray] = {}
    for session_id in sessions:
        path = DATA / "test_transcripts" / f"{session_id}.csv"
        if not path.is_file():
            raise RuntimeError("transcript coverage mismatch")
        text, ordinary = transcript_blocks(path)
        texts.append(text)
        ordinary_by_session[session_id] = ordinary
    session_text = make_vectorizer().transform(texts).tocsr().astype(np.float32)
    session_row = {session_id: index for index, session_id in enumerate(sessions)}
    response_rows = np.fromiter(
        (session_row[str(session_id)] for session_id in frame["session_id"]),
        dtype=np.int32,
        count=len(frame),
    )
    text_matrix = session_text[response_rows].tocsr()
    ordinary_matrix = np.vstack(
        [ordinary_by_session[str(session_id)] for session_id in frame["session_id"]]
    )

    load_model_manifest()
    with np.load(ASSETS / "m1_cal_model.npz", allow_pickle=False) as model:
        _, _, probabilities = predict_blocks(text_matrix, ordinary_matrix, model)
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
