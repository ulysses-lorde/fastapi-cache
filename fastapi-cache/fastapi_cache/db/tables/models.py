from uuid import UUID, uuid4
from typing import Optional

from sqlmodel import SQLModel, Field


class MovieBase(SQLModel):
    title: str = Field(default=None, nullable=False)
    release_year: str = Field(default=None, nullable=False)
    description: str = Field(default=None, nullable=False)


class Movie(MovieBase, table=True):
    id: UUID = Field(
        default_factory=uuid4,
        primary_key=True,
        index=True,
        nullable=False
    )

    __tablename__ = "movies"


class GenreBase(SQLModel):
    name: str = Field(default=None, nullable=False)


class Genre(GenreBase, table=True):
    id: int = Field(primary_key=True)

    __tablename__ = "genres"


class MovieGenre(SQLModel):
    movie_id: Optional[UUID] = Field(
        default=None,
        foreign_key="movies.id",
        primary_key=True
    )
    genre_id: Optional[int] = Field(
        default=None,
        foreign_key="genres.id",
        primary_key=True
    )
