from persistence.repositories.course_certificate_repository_postgres import CourseCertificateRepositoryPostgres
from exceptions.http_error import NotFoundError
from application.serializers.course_certificate_serializer import CourseCertificateSerializer
import logging

logger = logging.getLogger(__name__)

ccrp = CourseCertificateRepositoryPostgres()


def get_all_user_certificates(db, user_id):

    certificates = ccrp.get_all_user_certificates(db, user_id)
    if certificates is None or len(certificates) == 0:
        logger.warning("Certificates of user %s not found", user_id)
        return []
    cert_list = []
    for cert in certificates:
        cert_list.append(CourseCertificateSerializer.serialize(cert))
    return cert_list
