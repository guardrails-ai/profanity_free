## Details

| Developed by | Guardrails AI |
| --- | --- |
| Date of development |  |
| Validator type | Brand risk |
| Blog |  |
| License | Apache 2 |
| Input/Output | Output |

## Description

This validator ensures that there’s no profanity in any generated text. This validator uses the `alt-profanity-check` package to check if a string contains profanity language.


## Installation

```bash
$ gudardrails hub install hub://guardrails/profanity_free
```

## Usage Examples

### Validating string output via Python

In this example, we apply the validator to a string output generated by an LLM.

```python
# Import Guard and Validator
from guardrails.hub import ValidChoices
from guardrails import Guard

profanity_validator = IsProfanityFree(on_fail="noop")

# Create Guard with Validator
guard = Guard.from_string(
    validators=[profanity_validator, ...],
)
```

guard("Some text with profanity")
```

## Intended use

- Primary intended uses: This validator catches profanity in the English language only
- Out-of-scope use cases:

## Expected deployment metrics

|  | CPU | GPU |
| --- | --- | --- |
| Latency |  | - |
| Memory |  | - |
| Cost |  | - |
| Expected quality |  | - |

## Resources required

- Dependencies: `alt-profanity-check`
- Foundation model access keys:
- Compute:

## Validator Performance

### Evaluation Dataset

### Model Performance Measures

| Accuracy |  |
| --- | --- |
| F1 Score |  |

### Decision thresholds
