from persistence.repositories.course_certificate_repository_postgres import CourseCertificateRepositoryPostgres
from infrastructure.db.course_certificate_schema import CourseCertificate
from application.use_cases.course.get import get_course
from application.services.certificate_generator.certificate_generator import CertificateGenerator
from uuid import uuid4

ccrp = CourseCertificateRepositoryPostgres()


def add_course_certificate(db, course_id, user_id, username):

    id = uuid4()
    course_name = get_course(db, course_id)["name"]
    path_to_pdf = CertificateGenerator.create_certificate(username, course_name, id)

    certificate = CourseCertificate(id, course_id=course_id, user_id=user_id, pdf_path=path_to_pdf)

    ccrp.add_course_certificate(db, certificate)
