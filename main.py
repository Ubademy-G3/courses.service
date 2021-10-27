from fastapi import FastAPI
from infrastructure.routes import (course_router, course_media_router)
from infrastructure.db.database import database, engine
from infrastructure.db.course_schema import metadata

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(course_router.router, prefix='/api/v1/courses', tags=['courses'])

app.include_router(course_media_router.router, prefix='/api/v1/courses_media', tags=['media'])
