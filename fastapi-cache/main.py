from fastapi import FastAPI

from fastapi_cache.db.session import create_db_and_tables, bulk_create_movies, bulk_create_genres


title: str = "Title"
version: str = "1.0.0"
description: str = "Description here"
docs_url: str = "/docs"
redoc_url: str = "/redoc"
openapi_url: str = "/openapi.json"
api_prefix: str = "/api"
debug: bool = True

app = FastAPI(
    title=title,
    version=version,
    description=description,
    docs_url=docs_url,
    openapi_url=openapi_url,
)

#app = FastAPI()


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
