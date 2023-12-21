from uuid import UUID

from fastapi_cache.db.tables.models import MovieBase


class MovieCreate(MovieBase):
    ...

class MovieRead(MovieBase):
    id: UUID

class MoviePatch(MovieBase):
    ...
    