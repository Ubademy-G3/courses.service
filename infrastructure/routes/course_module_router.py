from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import get_db
from sqlalchemy.orm import Session
from application.controllers.course_module_controller import *
from application.services.auth import auth_service
from domain.course_module_model import *

router = APIRouter()

@router.post('/', response_model = CourseModuleDB, status_code = 201)
async def create_course_module(
                                payload: CourseModuleSchema,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):

    auth_service.check_api_key(apikey)
    return CourseModuleController.create_module(db, payload)


@router.get('/{module_id}', response_model = CourseModuleDB, status_code = 200)
async def get_course_module(
                            module_id: str,
                            db: Session = Depends(get_db),
                            apikey: str = Header(None)
                        ):

    auth_service.check_api_key(apikey)
    return CourseModuleController.get_module(db, module_id)


@router.patch('/{module_id}', response_model = CourseModuleDB, status_code = 200)
async def update_module(
                        module_id: str,
                        module: CourseModulePatch,
                        db: Session = Depends(get_db),
                        apikey: str = Header(None)
                    ):

    auth_service.check_api_key(apikey)
    return CourseModuleController.update_module(db, module_id, module)


@router.delete('/{module_id}', response_model = dict, status_code = 200)
async def delete_course_module(
                                module_id: str,
                                db: Session = Depends(get_db),
                                apikey: str = Header(None)
                            ):
    
    auth_service.check_api_key(apikey)
    module_deleted = CourseModuleController.delete_module(db, module_id)
    return {
        "message": "The module {} was deleted successfully".format(module_id)
    }