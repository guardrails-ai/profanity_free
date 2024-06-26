from typing import Any, Dict

from guardrails.validator_base import (
    FailResult,
    PassResult,
    ValidationResult,
    Validator,
    register_validator,
    ErrorSpan
)

from profanity_check import predict


@register_validator(name="guardrails/profanity_free", data_type="string")
class ProfanityFree(Validator):
    """Validates that a translated text does not contain profane language.

    This validator uses the `alt-profanity-check` package to check if a string
    contains profanity language.

    **Key Properties**

    | Property                      | Description                       |
    | ----------------------------- | --------------------------------- |
    | Name for `format` attribute   | `guardrails/profanity_free`       |
    | Supported data types          | `string`                          |
    | Programmatic fix              | None                              |
    """

    def validate(self, value: Any, metadata: Dict) -> ValidationResult:
        """Validation method for the ProfanityFree validator."""
        prediction = predict([value])
        if prediction[0] == 1:
            return FailResult(
                error_message=f"{value} contains profanity. "
                f"Please return profanity-free output.",
                fix_value="",
                error_spans=[
                    ErrorSpan(
                        start=0,
                        end=len(value),
                        reason="This text contains profanity."
                    )
                ]
            )
        return PassResult()