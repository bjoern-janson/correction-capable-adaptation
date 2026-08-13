ASSIGNMENT_CONSTRUCTION = "sha256(seed:unit_id) mod 2"
UNIT_ID_POLICY = (
    "all unit_id values are frozen and auditor-checkpointed before campaign seed commitment "
    "and before evidence/direction construction"
)
CAMPAIGN_SEED_POLICY = (
    "campaign seed is fixed and auditor-checkpointed after unit_id freeze and before any "
    "audit-unit package construction"
)
FORBIDDEN_ASSIGNMENT_INPUTS = (
    "evidence",
    "direction",
    "candidate_identity",
    "selector_prediction",
    "outcome_analysis_state",
)
