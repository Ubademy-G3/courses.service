from infrastructure.db.course_certificate_schema import CourseCertificate
from sqlalchemy import func

class CourseCertificateRepositoryPostgres():

    def add_course_certificate(self, db, payload):
        db.add(payload)
        db.commit()

    def get_all_user_certificates(self, db, user_id):
        query = db.query(CourseCertificate).filter(CourseCertificate.user_id == user_id).all()
        return query