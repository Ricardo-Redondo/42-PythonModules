#!usr/bin/venv python3

from pydantic import BaseModel, Field, ValidationError
from enum import Enum
from datetime import datetime


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: str = Field(pattern=r"^\d{4}-\d{2}-\d{2}$")
    species: str = Field(min_length=1, max_length=50)
    home_planet: str = Field(min_length=1, max_length=50)
    contact_type: str = Field(
        regex=r"^(visual|radio|telepathic|other)$", case_sensitive=False)
    description: str = Field(max_length=200, default="")
