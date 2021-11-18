from application.use_cases.course_user import (create, get, update, delete)

class CourseUserController:

    @classmethod
    def create_course_user(self, db, args, course_id):

        return create.add_course_user(db, course_id, args)


    @classmethod
    def get_all_course_users(self, db, course_id, user_type):

        return get.get_all_course_users(db, course_id, user_type)


    @classmethod
    def get_all_user_courses(self, db, user_id, aprobal_state, user_type):

        return get.get_all_user_courses(db, user_id, aprobal_state, user_type)

    @classmethod
    def update_course_user(self, db, course_id, user_id, update_args):
       
        return update.update_course_user(db, course_id, user_id, update_args)


    @classmethod
    def delete_course_user(self, db, course_id, user_id):
        
        return delete.delete_course_user(db, course_id, user_id)
