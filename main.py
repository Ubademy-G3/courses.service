from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import (course_router, course_media_router,
                                course_user_router, course_rating_router)
from infrastructure.db.database import database, engine
from infrastructure.db.course_schema import metadata
from errors.ubademy_error import UbademyException
from errors.auth_error import AuthorizationException

metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    error = {"error": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(UbademyException)
async def ubademy_exception_hanlder(request, exc):
    error = {"error": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    error = {"error": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


app.include_router(course_router.router, prefix='/courses', tags=['courses'])

app.include_router(course_media_router.router, prefix='/courses/{course_id}/media', tags=['media'])

app.include_router(course_user_router.router, prefix='/courses/{course_id}/users', tags=['users'])

app.include_router(course_rating_router.router, prefix='/courses/{course_id}/ratings', tags=['ratings'])