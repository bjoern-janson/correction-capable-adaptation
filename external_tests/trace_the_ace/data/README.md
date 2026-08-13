# Data integrity layer

This directory contains code only. Competition-derived data and generated artifacts are not committed.

`build_index.py` asserts the first data-integrity boundary:

- exact expected response count;
- exact expected unique-session count;
- one-to-one feature/label response mapping;
- deterministic response → session/objective/label mapping;
- exact transcript coverage of training sessions;
- no extra transcript sessions;
- no duplicate transcript session files;
- exact transcript schema;
- internal transcript `session_id` equals filename stem;
- contiguous zero-based `utterance_id` sequence per transcript;
- no missing values in required transcript fields.

A failed assertion is a data-integrity failure. The script does not silently drop or repair records.
