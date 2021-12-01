from infrastructure.db.course_certificate_schema import CourseCertificate

class CourseCertificateSerializer:

    @classmethod
    def serialize(self, cert: CourseCertificate):
        
        return {
            "id": cert.id,
            "course_id": cert.course_id,
            "pdf_path": cert.pdf_path
        }