from fastapi import FastAPI

from fastapi_cache.core.config import GlobalConfig as settings
from fastapi_cache.db.session import create_db_and_tables, bulk_create_movies, bulk_create_genres


app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    docs_url=settings.docs_url,
    openapi_url=settings.openapi_url,
)


@app.get('/')
async def home():
    return {'Home Page': 'Loading Success'}

@app.get('/create_tables')
async def create_tables():
    await create_db_and_tables()

    return {'Database': 'Tables Created!'}


@app.get("/create_registers/{number}")
async def create_profiles(number: int):
    await bulk_create_movies(number)
    await bulk_create_genres()

    return {"Say": "Registers created!"}
