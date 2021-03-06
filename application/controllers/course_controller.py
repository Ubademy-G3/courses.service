from application.use_cases.course import create, delete, get, update


class CourseController:
    @classmethod
    def create_course(self, db, args):

        return create.add_course(db, args)

    @classmethod
    def get_all_courses(self, db, category, subscription_type, text):

        return get.get_all_courses(db, category, subscription_type, text)

    @classmethod
    def get_all_courses_with_rating(self, db, category, subscription_type, text):

        return get.get_all_courses_with_rating(db, category, subscription_type, text)

    @classmethod
    def get_all_courses_by_user_with_rating(self, db, user_id, user_type, approval_state, category, subscription_type, text):
        return get.get_all_courses_by_user_with_rating(db, user_id, user_type, approval_state, category, subscription_type, text)

    @classmethod
    def get_all_courses_from_list(self, db, course_list):

        return get.get_all_courses_from_list(db, course_list)

    @classmethod
    def get_all_courses_from_list_with_rating(self, db, course_list):

        return get.get_all_courses_from_list_with_rating(db, course_list)

    @classmethod
    def get_course(self, db, course_id):

        return get.get_course(db, course_id)

    @classmethod
    def get_course_with_rating(self, db, course_id):

        return get.get_course_with_rating(db, course_id)

    @classmethod
    def update_course(self, db, course_id, update_args):

        return update.update_course(db, course_id, update_args)

    @classmethod
    def delete_course(self, db, course_id):

        return delete.delete_course(db, course_id)
