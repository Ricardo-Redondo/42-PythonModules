#!usr/bin/venv python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(min_length=0, max_length=500,
                                            default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate(self):
        errors = []

        if self.contact_id != ("AC" + self.contact_id[2:]):
            errors.append("contact_id must start with 'AC'")

        if self.contact_type == ContactType.PHYSICAL and not self.is_verified:
            errors.append("Physical contacts must be verified")

        if self.contact_type == ContactType.TELEPATHIC and \
                self.witness_count < 3:
            errors.append("Telepathic contacts "
                          "requires at least 3 witnesses")

        if self.signal_strength > 7.0 and not self.message_received:
            errors.append("Strong signals must have a message received")

        if errors:
            raise ValueError(" | ".join(errors))

        return self


if __name__ == "__main__":
    print("\n\033[46mAlien Contact Data Validation\033[0m")
    print("\033[36m=\033[0m" * 59)

    err = "\n\033[3;5;101m[ERROR]\033[0m \033[3m"

    try:
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            timestamp=datetime.now(),
            location="Area 51, Nevada",
            contact_type=ContactType.RADIO,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli!",
            is_verified=True
        )
        print("Valid contact created:")
        print(f"  ID             : {contact1.contact_id}")
        print(f"  Timestamp      : {contact1.timestamp}")
        print(f"  Location       : {contact1.location}")
        print(f"  Type           : {contact1.contact_type.value}")
        print(f"  Signal Strength: {contact1.signal_strength}/10")
        print(f"  Duration       : {contact1.duration_minutes} minutes")
        print(f"  Witnesses      : {contact1.witness_count}")
        print(f"  Message        : "
              f"{contact1.message_received or 'No message received'}")
        print(f"  Verified       : {'Yes' if contact1.is_verified else 'No'}")
    except ValidationError as e:
        for error in e.errors():
            field = f"{error['loc'][0]}: " if error['loc'] else ""
            msg = error['msg'].split(', ')[-1].replace(' | ', err)
            parsed_msg = f"Validation Error: {msg}" \
                if len(error['msg'].split(', ')) > 1 else error['msg']
            print(f"{err}{field}{msg}\033[0m")

    print("\033[36m=\033[0m" * 59)
    try:
        contact2 = AlienContact(
            contact_id="AC_2024_002",
            timestamp=datetime.now(),
            location="Sahara Desert",
            contact_type=ContactType.TELEPATHIC,
            signal_strength=8.0,
            duration_minutes=60,
            witness_count=2,
            is_verified=True
        )
        print("Valid contact created:")
        print(f"  ID             : {contact2.contact_id}")
        print(f"  Timestamp      : {contact2.timestamp}")
        print(f"  Location       : {contact2.location}")
        print(f"  Type           : {contact2.contact_type.value}")
        print(f"  Signal Strength: {contact2.signal_strength}/10")
        print(f"  Duration       : {contact2.duration_minutes} minutes")
        print(f"  Witnesses      : {contact2.witness_count}")
        print(f"  Message        : "
              f"{contact2.message_received or 'No message received'}")
        print(f"  Verified       : {'Yes' if contact2.is_verified else 'No'}")
    except ValidationError as e:
        for error in e.errors():
            field = f"{error['loc'][0]}: " if error['loc'] else ""
            msg = error['msg'].split(', ')[-1].replace(' | ', err)
            parsed_msg = f"Validation Error: {msg}" \
                if len(error['msg'].split(', ')) > 1 else error['msg']
            print(f"{err}{field}{msg}\033[0m")
