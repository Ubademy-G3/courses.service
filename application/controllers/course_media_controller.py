from application.use_cases.course_media import (create, get, delete)

class CourseMediaController:

    @classmethod
    def create_course_media(self, db, args, course_id):

        return create.add_course_media(db, course_id, args)


    @classmethod
    def get_all_course_media(self, db, course_id):

        return get.get_all_course_media(db,course_id)


    @classmethod
    def get_course_media(self, db, course_id, media_id):

        return get.get_course_media(db, course_id, media_id)


    @classmethod
    def get_all_module_media(self, db, module_id):

        return get.get_all_module_media(db, module_id)


    @classmethod
    def delete_course_media(self, db, course_id, media_id):
        
        return delete.delete_course_media(db, course_id, media_id)
