# GreenField Farmers FAQ Dataset

## Overview
A sample FAQ dataset for the GreenField Farmers Co-op project. The entries are illustrative and are not verified statements of the co-op's actual policies.

## Data generation
Run `python generate_faq.py` to write `faq.json` as UTF-8 JSON with two-space indentation. The script builds a curated list of question-and-answer dictionaries and exports it deterministically.

## Topics covered
- Membership and joining
- Produce sales and pricing
- Seasonal produce
- Orders and pickup
- Farming practices
- Sustainability
- Payments, cancellations, and refunds

## Validation
Install the validation dependency with `python -m pip install -r requirements.txt`, then run:

```bash
python -m json.tool faq.json
python validate_faq.py
```

All entries should have non-empty string values and no nulls. This is a starter dataset for the project; confirm actual co-op policies before using the answers in a live assistant.
