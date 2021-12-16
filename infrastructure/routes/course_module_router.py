from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_module_controller import CourseModuleController
from application.services.auth import auth_service
from domain.course_module_model import CourseModuleDB, CourseModuleSchema, CourseModulePatch, CourseModuleList
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/", response_model=CourseModuleDB, status_code=201)
async def create_course_module(
    course_id: str,
    payload: CourseModuleSchema,
    db: Session = Depends(get_db),
    apikey: str = Header(None)
):

    logger.debug("Creating module...")
    auth_service.check_api_key(apikey)
    return CourseModuleController.create_module(db, course_id, payload)


@router.get("/", response_model=CourseModuleList, status_code=200)
async def get_all_modules_by_course_id(
    course_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None)
):

    auth_service.check_api_key(apikey)
    course_module_list = CourseModuleController.get_all_modules_by_course_id(db, course_id)
    return {"amount": len(course_module_list), "course_id": course_id, "modules": course_module_list}


@router.get("/{module_id}", response_model=CourseModuleDB, status_code=200)
async def get_course_module(
    course_id: str,
    module_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None)
):

    auth_service.check_api_key(apikey)
    return CourseModuleController.get_module(db, module_id)


@router.patch("/{module_id}", response_model=CourseModuleDB, status_code=200)
async def update_module(
    course_id: str,
    module_id: str,
    module: CourseModulePatch,
    db: Session = Depends(get_db),
    apikey: str = Header(None)
):

    auth_service.check_api_key(apikey)
    return CourseModuleController.update_module(db, module_id, module)


@router.delete("/{module_id}", response_model=dict, status_code=200)
async def delete_course_module(
    course_id: str,
    module_id: str,
    db: Session = Depends(get_db),
    apikey: str = Header(None)
):

    auth_service.check_api_key(apikey)
    CourseModuleController.delete_module(db, module_id)
    return {"message": "The module {} was deleted successfully".format(module_id)}
