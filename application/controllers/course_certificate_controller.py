from application.use_cases.course_certificate import create, get


class CourseCertificateController:
    @classmethod
    def add_course_certificate(self, db, course_id, user_id, username):

        return create.add_course_certificate(db, course_id, user_id, username)

    @classmethod
    def get_all_user_certificates(self, db, user_id):

        return get.get_all_user_certificates(db, user_id)
