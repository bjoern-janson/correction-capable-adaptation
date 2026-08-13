ASSIGNMENT_CONSTRUCTION = "sha256(seed:unit_id) mod 2"
CAMPAIGN_SEED_POLICY = (
    "seed is fixed and auditor-checkpointed before any audit-unit package construction"
)
UNIT_ID_POLICY = "unit_id is assigned before evidence and direction construction"
FORBIDDEN_ASSIGNMENT_INPUTS = (
    "evidence",
    "direction",
    "candidate_identity",
    "selector_prediction",
    "outcome_analysis_state",
)
