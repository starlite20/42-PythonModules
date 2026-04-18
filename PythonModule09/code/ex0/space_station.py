from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ValidationError


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3, max_length=10,
        default="IS0000",
        description="station Serial ID"
    )
    name: str = Field(
        min_length=1, max_length=50,
        default="ssujaude",
        description="Name of the Station"
    )
    crew_size: int = Field(
        ge=1, le=20,
        default=10,
        description="Max crew capacity"
    )
    power_level: float = Field(
        ge=0.0, le=100.0,
        default=100.0,
        description="Current Power Level"
    )
    oxygen_level: float = Field(
        ge=0.0, le=100.0,
        default=100.0,
        description="Current Oxygen Level"
    )
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(
        default=None, max_length=200,
        description="Additional Notes about Space Station (optional)"
    )


def main() -> None:
    print("Space Station Data Validation")
    print("=" * 40)

    valid_data = {
        "station_id": "ISS001",
        "name": "International Space Station",
        "crew_size": 6,
        "power_level": 85.5,
        "oxygen_level": 92.3,
        "last_maintenance": "2023-10-01T10:00:00"
    }

    try:
        station = SpaceStation(**valid_data)
        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        status = "Operational" if station.is_operational else "Down"
        print(f"Status: {status}")
    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("\n", end="")
    print("=" * 40)

    invalid_data = valid_data.copy()
    invalid_data["crew_size"] = 25

    print("Expected validation error:")
    try:
        SpaceStation(**invalid_data)
    except ValidationError as e:
        # Extracting the exact standard Pydantic v2 error message
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
