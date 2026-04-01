#!usr/bin/venv python3

from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime


class Rank(str, Enum):
    CADET = "Cadet",
    OFFICER = "Officer",
    LIEUTENANT = "Lieutenant",
    CAPTAIN = "Captain",
    COMMANDER = "Commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=300)
    destination: str = Field(min_length=3, max_length=30)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12,
                                   default_factory=list)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=0.0, le=10000.0)

    @model_validator(mode="after")
    def validate(self):
        errors = []

        if not self.mission_id.startswith("M"):
            errors.append("mission_id must start with 'M'")

        has_commander = any(m.rank == Rank.COMMANDER for m in self.crew)
        has_captain = any(m.rank == Rank.CAPTAIN for m in self.crew)
        if not has_commander and not has_captain:
            errors.append("Mission crew must include at "
                          "least one Captain or Commander")

        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced < len(self.crew) / 2:
                errors.append("Long missions require at least "
                              "half the crew with 5+ years experience")

        if not all(m.is_active for m in self.crew):
            errors.append("All crew members must be active for the mission")

        if errors:
            raise ValueError(" | ".join(errors))

        return self


if __name__ == "__main__":
    print("\n\033[46mSpace Mission Data Validation\033[0m")
    print("\033[36m=\033[0m" * 59)

    err = "\n\033[3;5;101m[ERROR]\033[0m \033[3m"

    try:
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C001",
                    name="Sarah Connor",
                    rank=Rank.COMMANDER,
                    age=45,
                    specialization="Mission Command",
                    years_experience=10,
                    is_active=True
                ),
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=4,
                    is_active=True
                )
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"  Mission     : {mission1.mission_name}")
        print(f"  ID          : {mission1.mission_id}")
        print(f"  Destination : {mission1.destination}")
        print(f"  Launch Date : {mission1.launch_date}")
        print(f"  Duration    : {mission1.duration_days} days")
        print(f"  Budget      : ${mission1.budget_millions} million")
        print(f"  Status      : {mission1.mission_status}")
        print(f"  Crew Size   : {len(mission1.crew)} members")
        print("  Crew Members:")
        for member in mission1.crew:
            print(f"    - {member.name} ({member.rank.value}) = ",
                  member.specialization)
    except ValidationError as e:
        for error in e.errors():
            field = f"{error['loc'][0]}: " if error['loc'] else ""
            msg = error['msg'].split(', ')[-1].replace(' | ', err)
            parsed_msg = f"Validation Error: {msg}" \
                if len(error['msg'].split(', ')) > 1 else error['msg']
            print(f"{err}{field}{msg}\033[0m")

    print("\033[36m=\033[0m" * 59)
    try:
        mission2 = SpaceMission(
            mission_id="2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime.now(),
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Navigation",
                    years_experience=6,
                    is_active=True
                ),
                CrewMember(
                    member_id="C003",
                    name="Alice Johnson",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Engineering",
                    years_experience=4,
                    is_active=True
                )
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"  Mission     : {mission2.mission_name}")
        print(f"  ID          : {mission2.mission_id}")
        print(f"  Destination : {mission2.destination}")
        print(f"  Launch Date : {mission2.launch_date}")
        print(f"  Duration    : {mission2.duration_days} days")
        print(f"  Budget      : ${mission2.budget_millions} million")
        print(f"  Status      : {mission2.mission_status}")
        print(f"  Crew Size   : {len(mission2.crew)} members")
        print("  Crew Members:")
        for member in mission2.crew:
            print(f"    - {member.name} ({member.rank.value}) = ",
                  member.specialization)
    except ValidationError as e:
        for error in e.errors():
            field = f"{error['loc'][0]}: " if error['loc'] else ""
            msg = error['msg'].split(', ')[-1].replace(' | ', err)
            parsed_msg = f"Validation Error: {msg}" \
                if len(error['msg'].split(', ')) > 1 else error['msg']
            print(f"{err}{field}{msg}\033[0m")
