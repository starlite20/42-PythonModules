from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field, ValidationError, model_validator
from pydantic_core import PydanticCustomError


class Rank(str, Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    captain = "captain"
    commander = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(
        min_length=3, max_length=10,
        description="ID of Member"
    )
    name: str = Field(
        min_length=2, max_length=50,
        description="Name of Member"
    )
    rank: Rank
    age: int = Field(
        ge=18, le=80,
        description="Age of Member"
    )
    specialization: str = Field(
        min_length=3, max_length=30,
        description="Specialization of Member"
    )
    years_experience: int = Field(
        ge=0, le=50,
        description="Years of experience of Member"
    )
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(
        min_length=5, max_length=15,
        description="ID of Mission"
    )
    mission_name: str = Field(
        min_length=3, max_length=100,
        description="Mission Name"
    )
    destination: str = Field(
        min_length=3, max_length=50,
        description="Destination of Mission"
    )
    launch_date: datetime
    duration_days: int = Field(
        ge=1, le=3650,
        description="Duration of Mission"
    )

    crew: list[CrewMember] = Field(
        min_length=1, max_length=12,
        description="Crew List of Mission"
    )
    mission_status: str = "planned"
    budget_millions: float = Field(
        ge=1.0, le=10000.0,
        description="Budget of Mission"
    )

    @model_validator(mode='after')
    def validate_mission_safety(self) -> 'SpaceMission':
        # Rule 1: Mission ID prefix
        if not self.mission_id.startswith("M"):
            raise PydanticCustomError(
                "invalid_prefix", "Mission ID must start with 'M'"
            )

        # Rule 2: Must have at least one Commander or Captain
        has_command = any(
            m.rank in (Rank.commander, Rank.captain) for m in self.crew
        )
        if not has_command:
            raise PydanticCustomError(
                "missing_command",
                "Mission must have at least one Commander or Captain"
            )

        # Rule 3: Long missions (> 365 days) need 50% experienced crew
        if self.duration_days > 365:
            experienced = sum(
                1 for m in self.crew if m.years_experience >= 5
            )
            if experienced < (len(self.crew) / 2):
                raise PydanticCustomError(
                    "inexperienced_crew",
                    "Long missions (> 365 days) need "
                    "50% experienced crew (5+ years)"
                )

        # Rule 4: All crew must be active
        inactive = [m.name for m in self.crew if not m.is_active]
        if inactive:
            raise PydanticCustomError(
                "inactive_crew",
                f"All crew members must be active."
                f" Inactive: {', '.join(inactive)}"
            )

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=" * 40)

    valid_data = {
        "mission_id": "M2024_MARS",
        "mission_name": "Mars Colony Establishment",
        "destination": "Mars",
        "launch_date": "2025-06-01T08:00:00",
        "duration_days": 900,
        "budget_millions": 2500.0,
        "crew": [
            {
                "member_id": "CMD001",
                "name": "Sarah Connor",
                "rank": "commander",
                "age": 35,
                "specialization": "Mission Command",
                "years_experience": 12
            },
            {
                "member_id": "LT002",
                "name": "John Smith",
                "rank": "lieutenant",
                "age": 28,
                "specialization": "Navigation",
                "years_experience": 6
            },
            {
                "member_id": "OFR003",
                "name": "Alice Johnson",
                "rank": "officer",
                "age": 24,
                "specialization": "Engineering",
                "years_experience": 2
            }
        ]
    }

    try:
        mission = SpaceMission.model_validate(valid_data)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        print("Crew members:")
        for member in mission.crew:
            print(
                f"- {member.name} ({member.rank.value})"
                f" - {member.specialization}"
            )
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("\n" + "=" * 40)

    invalid_data = valid_data.copy()
    # Rule 2 violation: No commander or captain
    invalid_data["crew"] = [
        {
            "member_id": "OFR004",
            "name": "Bob Brown",
            "rank": "officer",
            "age": 30,
            "specialization": "Medic",
            "years_experience": 5
        }
    ]

    print("Expected validation error:")
    try:
        SpaceMission.model_validate(invalid_data)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
