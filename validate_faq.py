"""Validate faq.json against a small JSON Schema."""
import json
from pathlib import Path
from jsonschema import validate

path = Path(__file__).with_name("faq.json")
data = json.loads(path.read_text(encoding="utf-8"))
schema = {
    "type": "array",
    "minItems": 30,
    "items": {
        "type": "object",
        "required": ["question", "answer"],
        "additionalProperties": False,
        "properties": {
            "question": {"type": "string", "minLength": 1},
            "answer": {"type": "string", "minLength": 1},
        },
    },
}
validate(instance=data, schema=schema)
questions = [item["question"].strip().casefold() for item in data]
assert len(questions) == len(set(questions)), "Duplicate questions found"
assert all(item["question"].strip() and item["answer"].strip() for item in data)
print(f"PASS: {len(data)} valid, distinct FAQ entries")
