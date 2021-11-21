from fastapi import FastAPI
import logging
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from infrastructure.routes import (course_router, course_media_router,
                                course_user_router, course_rating_router,
                                course_category_router, user_courses_router,
                                course_metrics_router)

from infrastructure.db.database import Base, engine
from sqlalchemy.exc import SQLAlchemyError
from exceptions.ubademy_error import UbademyException
from exceptions.auth_error import AuthorizationException

Base.metadata.create_all(engine)

app = FastAPI(
                title = "Ubademy - Courses service",
                description = "Courses service API"
            )
            

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    error = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(UbademyException)
async def ubademy_exception_handler(request, exc):
    error = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(AuthorizationException)
async def auth_exception_handler(request, exc):
    error = {"message": exc.detail}
    logging.error(f"status_code: {exc.status_code} message: {exc.detail}")
    return JSONResponse(status_code = exc.status_code, content = error)


@app.exception_handler(SQLAlchemyError)
async def sql_exception_handler(request, exc):
    error = {"message": str(exc.__dict__['orig'])}
    logging.error(f"status_code: 500 message: {str(exc.__dict__['orig'])}")
    return JSONResponse(status_code = 500, content = error)


app.include_router(course_router.router, prefix='/courses', tags=['courses'])

app.include_router(course_media_router.router, prefix='/courses/{course_id}/media', tags=['media'])

app.include_router(course_user_router.router, prefix='/courses/{course_id}/users', tags=['users'])

app.include_router(course_rating_router.router, prefix='/courses/{course_id}/ratings', tags=['ratings'])

app.include_router(course_metrics_router.router, prefix='/courses/{course_id}/metrics', tags=['metrics'])

app.include_router(course_category_router.router, prefix='/courses/category', tags=['category'])

app.include_router(user_courses_router.router, prefix='/courses/user/{user_id}', tags=['user courses'])