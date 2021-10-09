from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm.session import Session
#from app.db import engine, database, metadata

#metadata.create_all(engine)

app = FastAPI()

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

#@app.on_event("startup")
#async def startup():
#    await database.connect()


#@app.on_event("shutdown")
#async def shutdown():
#    await database.disconnect()