from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def home():
    return {'Home Page': 'Loading Success'}
