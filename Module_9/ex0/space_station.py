#!usr/bin/venv python3

from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxigen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")  # YYYY-MM-DD
    is_operational: bool = Field(default=True)
    notes: str = Field(max_length=200, default="")


if __name__ == "__main__":
    print("\n\033[46mSpace Station Data Validation\033[0m")
    print("\033[36m=\033[0m" * 59)

    try:
        station1 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxigen_level=92.3,
            last_maintenance=datetime.now().strftime("%Y-%m-%d"),
            is_operational=True,
            notes="All systems nominal."
        )
        print("Valid station created:")
        print(f"  ID               : {station1.station_id}")
        print(f"  Name             : {station1.name}")
        print(f"  Crew             : {station1.crew_size} people")
        print(f"  Power            : {station1.power_level}%")
        print(f"  Oxygen           : {station1.oxigen_level}%")
        print(f"  Last Maintenance : {station1.last_maintenance}")
        print(f"  Status           : "
              f"{'Operational' if station1.is_operational else 'Offline'}")
    except ValidationError as e:
        for error in e.errors():
            field = error['loc'][0]
            msg = error['msg']
            print(f"\033[3;5;101m[ERROR]\033[0m \033[3m{field}: {msg}\033[0m")

    print("\033[36m=\033[0m" * 59)

    try:
        station2 = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxigen_level=92.3,
            last_maintenance=datetime.now().strftime("%Y-%m-%d"),
        )
        print("Valid station created:")
        print(f"  ID               : {station2.station_id}")
        print(f"  Name             : {station2.name}")
        print(f"  Crew             : {station2.crew_size} people")
        print(f"  Power            : {station2.power_level}%")
        print(f"  Oxygen           : {station2.oxigen_level}%")
        print(f"  Last Maintenance : {station2 .last_maintenance}")
        print(f"  Status           : "
              f"{'Operational' if station2.is_operational else 'Offline'}")
    except ValidationError as e:
        for error in e.errors():
            field = error['loc'][0]
            msg = error['msg']
            print(f"\033[3;5;101m[ERROR]\033[0m \033[3m{field}: {msg}\033[0m")

    print("\033[36m=\033[0m" * 59)
