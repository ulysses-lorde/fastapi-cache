from sqlmodel import SQLModel, create_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
#from sqlalchemy_utils import database_exists, create_database
from faker import Faker
from faker.providers import BaseProvider

from fastapi_cache.core.config import GlobalConfig
#from tables.profiles import Profile
from .tables.models import Movie, Genre


settings = GlobalConfig()

engine = create_engine(
    'sqlite:///meu_banco.db',
    connect_args={"check_same_thread": False}
)

async_engine = create_async_engine(
    settings.async_database_url,
    echo=True,
    future=True
)

async_session = sessionmaker(
    bind=async_engine, class_=AsyncSession,
    expire_on_commit=False
)

async def create_db_and_tables() -> None:
    '''if database_exists == False:
        create_database(engine.url)'''
    SQLModel.metadata.drop_all(engine)
    SQLModel.metadata.create_all(engine)

async def bulk_create_movies(number: int) -> None:
    fake = Faker()
    async with AsyncSession(async_engine) as session:
        for _ in range(number):
            movie_data = {
                'title': fake.sentence(),
                'release_year': fake.year(),
                'description': fake.paragraph(),
            }
            movie = Movie(**movie_data)
            session.add(movie)
        
        await session.commit()

async def bulk_create_genres()  -> None:
    async with AsyncSession(async_engine) as session:
        genres = ['Action', 'Comedy', 'Drama', 'Sci-Fi', 'Horror', 'Romance', 'Thriller', 'Fantasy', 'Animation']
        for genre_name in genres:
            genre = Genre(name=genre_name)
            session.add(genre)

        await session.commit()
