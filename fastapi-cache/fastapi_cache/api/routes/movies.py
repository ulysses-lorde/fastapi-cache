from typing import Optional
from uuid import UUID

from fastapi import APIRouter, status, Depends, HTTPException

from fastapi_cache.api.dependencies.repositories import get_repository
from fastapi_cache.db.errors import EntityDoesNotExist
from fastapi_cache.db.repositories.movies import MovieRepository
from fastapi_cache.schemas.movies import MovieRead


router = APIRouter()


@router.get(
        "/movies",
        response_model=list[Optional[MovieRead]],
        status_code=status.HTTP_200_OK,
        name="get_movies"
)
async def get_movies(
    repository: MovieRepository = Depends(get_repository(MovieRepository))
) -> list[Optional[MovieRead]]:
    return await repository.list()

@router.get(
    "/movies/{movie_id}",
    status_code=status.HTTP_200_OK,
    name="get_movie"
)
async def get_movie(
    movie_id: UUID,
    repository: MovieRepository = Depends(get_repository(MovieRepository)),   
) -> MovieRead:
    try:
        movie = await repository.get(movie_id=movie_id)
        
        return movie
    
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found!"
        )

