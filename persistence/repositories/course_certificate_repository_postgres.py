from infrastructure.db.course_certificate_schema import CourseCertificate
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)

class CourseCertificateRepositoryPostgres():

    def add_course_certificate(self, db, payload):
        db.add(payload)
        db.commit()

        logger.info("New certificate created")
        logger.debug("URL of the new certificate", payload.pdf_path)

    def get_all_user_certificates(self, db, user_id):
        query = db.query(CourseCertificate).filter(CourseCertificate.user_id == user_id).all()
        logger.debug("Getting all certificates")
        return query