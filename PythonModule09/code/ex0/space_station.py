from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ValidationError
import json


class SpaceStation(BaseModel):
    station_id: str = Field(
        min_length=3, max_length=10,
        description="station Serial ID"
    )
    name: str = Field(
        min_length=1, max_length=50,
        description="Name of the Station"
    )
    crew_size: int = Field(
        ge=1, le=20,
        description="Max crew capacity"
    )
    power_level: float = Field(
        ge=0.0, le=100.0,
        description="Current Power Level"
    )
    oxygen_level: float = Field(
        ge=0.0, le=100.0,
        description="Current Oxygen Level"
    )
    last_maintenance: datetime
    is_operational: bool = True
    notes: Optional[str] = Field(
        default=None, max_length=200,
        description="Additional Notes about Space Station (optional)"
    )


def test_from_generated_json() -> None:
    filepath = "../../generated_data/space_stations.json"
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)

        print("\nTesting with Generated JSON Data")
        print("=" * 40)

        valid_count = 0
        invalid_count = 0

        for item in raw_data:
            try:
                station = SpaceStation.model_validate(item)
                print_station_data(station)
                valid_count += 1
            except ValidationError:
                invalid_count += 1

        print(f"Successfully validated {valid_count} stations from JSON.")
        if invalid_count > 0:
            print(f"Rejected {invalid_count} invalid stations from JSON.")

    except FileNotFoundError:
        print("File not found!")
        pass


def print_station_data(station: SpaceStation) -> None:
    print("Valid station created:")
    print(f"ID: {station.station_id}")
    print(f"Name: {station.name}")
    print(f"Crew: {station.crew_size} people")
    print(f"Power: {station.power_level}%")
    print(f"Oxygen: {station.oxygen_level}%")
    status = "Operational" if station.is_operational else "Down"
    print(f"Status: {status}\n")


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
        station = SpaceStation.model_validate(valid_data)
        print_station_data(station)

    except ValidationError as e:
        print(f"Unexpected error: {e}")

    print("=" * 40)

    invalid_data = valid_data.copy()
    invalid_data["crew_size"] = 25

    print("Expected validation error:")
    try:
        SpaceStation.model_validate(invalid_data)
    except ValidationError as e:
        print(e.errors()[0]['msg'])


if __name__ == "__main__":
    main()
