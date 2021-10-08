from fastapi import FastAPI

#from app.api import ping
from app.db import engine, database, metadata

metadata.create_all(engine)

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


#app.include_router(ping.router)