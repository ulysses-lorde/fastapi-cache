from enum import Enum
from datetime import date
from typing import List
from uuid import UUID, uuid4

from sqlmodel import JSON, Column, Field, SQLModel


class GenderEnum(str, Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class ProfileBase(SQLModel):
    username: str = Field(default=None, nullable=True)
    mail: str = Field(default=None, nullable=True)
    name: str = Field(default=None, nullable=True)
    sex: GenderEnum = Field(default=None, nullable=True)


class Profile(ProfileBase, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False,
    )

    __tablename__ = "profiles"
