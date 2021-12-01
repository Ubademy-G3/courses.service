from fastapi import APIRouter, Header, Depends
from infrastructure.db.database import Session, get_db
from application.controllers.course_certificate_controller import *
from application.services.auth import auth_service
from domain.course_certificate_model import *

router = APIRouter()

@router.get('/', response_model = dict, status_code = 200)
async def get_all_user_certificates(
                                    user_id: str,
                                    db: Session = Depends(get_db),
                                    apikey: str = Header(None)
                                ):
    
    auth_service.check_api_key(apikey)
    user_certificates_list = CourseCertificateController.get_all_user_certificates(db, user_id)
    return {
        "amount": len(user_certificates_list),
        "user_id": user_id,
        "certificates": user_certificates_list
    }