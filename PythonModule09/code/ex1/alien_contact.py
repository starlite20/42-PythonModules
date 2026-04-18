from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(
        min_length=5, max_length=15,
        description="Contact ID of Alien"
    )
    timestamp: datetime
    location: str = Field(
        min_length=3, max_length=100,
        description="Location of Alien Identification"
    )
    contact_type: ContactType
    signal_strength: float = Field(
        ge=0.0, le=10.0,
        description="Signal Strength of Contact"
    )
    duration_minutes: int = Field(
        ge=1, le=1440,
        description="Duration of Contact"
    )
    witness_count: int = Field(
        ge=1, le=100,
        description="Number of Witnesses"
    )
    message_received: Optional[str] = Field(
        default=None, max_length=500,
        description="Message Received from Alien"
    )
    is_verified: bool = False

    @model_validator(mode='after')
    def validate_business_rules(self) -> 'AlienContact':
        if not self.contact_id.startswith("AC"):
            raise PydanticCustomError(
                "invalid_prefix",
                "Contact ID must start with 'AC'"
            )

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise PydanticCustomError(
                "unverified_physical",
                "Physical contact reports must be verified"
            )

        if ((self.contact_type == ContactType.telepathic)
                and (self.witness_count < 3)):
            raise PydanticCustomError(
                "telepathic_witnesses",
                "Telepathic contact requires at least 3 witnesses"
            )

        if self.signal_strength > 7.0 and not self.message_received:
            raise PydanticCustomError(
                "missing_message",
                "Strong signals (> 7.0) should include received messages"
            )

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("=" * 40)

    valid_data = {
        "contact_id": "AC_2024_001",
        "timestamp": "2024-11-15T08:30:00",
        "location": "Area 51, Nevada",
        "contact_type": "radio",
        "signal_strength": 8.5,
        "duration_minutes": 45,
        "witness_count": 5,
        "message_received": "Greetings from Zeta Reticuli"
    }

    try:
        contact = AlienContact.model_validate(valid_data)
        print("Valid contact report:")
        print(f"ID: {contact.contact_id}")
        print(f"Type: {contact.contact_type.value}")
        print(f"Location: {contact.location}")
        print(f"Signal: {contact.signal_strength}/10")
        print(f"Duration: {contact.duration_minutes} minutes")
        print(f"Witnesses: {contact.witness_count}")
        print(f"Message: '{contact.message_received}'")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("\n", end="")
    print("=" * 40)

    invalid_data = valid_data.copy()
    invalid_data["contact_type"] = "telepathic"
    invalid_data["witness_count"] = 1

    print("Expected validation error:")
    try:
        AlienContact.model_validate(invalid_data)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
