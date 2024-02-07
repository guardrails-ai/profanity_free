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

## Example Usage Guide

### Installation

```bash
$ gudardrails hub install is-profanity-free
```

### Initialization

```python
profanity_validator = IsProfanityFree(on_fail="noop")

# Create Guard with Validator
guard = Guard.from_string(
    validators=[profanity_validator, ...],
)
```

### Invocation

```python
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
