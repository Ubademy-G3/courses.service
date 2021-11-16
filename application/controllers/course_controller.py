from application.use_cases.course import (create,delete,get,update)


class CourseController:
    
    @classmethod
    def create_course(self, db, args):

        return create.add_course(db, args)


    @classmethod
    def get_all_courses(self, db, category, subscription_type):

        return get.get_all_courses(db, category, subscription_type)


    @classmethod
    def get_course(self, db, course_id):

        return get.get_course(db, course_id)


    @classmethod
    def update_course(self, db, course_id, update_args):
       
        return update.update_course(db, course_id, update_args)


    @classmethod
    def delete_course(self, db, course_id):

        return delete.delete_course(db, course_id)
        