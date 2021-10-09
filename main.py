# from fastapi import Depends, FastAPI, HTTPException, status
# from sqlalchemy.orm.session import Session
# from typing import Iterator
from fastapi import FastAPI

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong!"}
