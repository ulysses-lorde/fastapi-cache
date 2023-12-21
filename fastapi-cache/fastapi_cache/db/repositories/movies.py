from typing import Optional
from uuid import UUID

from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from fastapi_cache.db.errors import EntityDoesNotExist
from fastapi_cache.db.tables.models import Movie
from fastapi_cache.schemas.movies import MovieRead


class MovieRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def _get_instance(self, movie_id: UUID):
        statement = select(Movie).where(Movie.id == movie_id)
        results = await self.session.exec(statement)
        
        return results.first()
    
    async def list(self) -> list[MovieRead]:
        statement = select(Movie)
        results = await self.session.exec(statement)

        return [MovieRead(**movie.dict()) for movie in results]

    async def get(self, movie_id: UUID) -> Optional[MovieRead]:
        db_movie = await self._get_instance(movie_id)

        if db_movie is None:
            raise EntityDoesNotExist
        
        return MovieRead(**db_movie.dict())