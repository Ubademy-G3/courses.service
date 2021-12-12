from infrastructure.db.course_media_schema import CourseMedia
from sqlalchemy import func

class CourseMediaRepositoryPostgres():

    def add_course_media(self, db, payload):
        db.add(payload)
        db.commit()


    def get_all_course_media(self, db, course_id):
        course_media_list = (db.query(CourseMedia).filter(CourseMedia.course_id == course_id).all())
        return course_media_list


    def get_all_course_module_media(self, db, module_id):
        course_module_media_list = (db.query(CourseMedia).filter(CourseMedia.module_id == module_id).all())
        return course_module_media_list
       
    def get_course_media(self, db, course_id, media_id):
        course_media = db.query(CourseMedia).filter(CourseMedia.course_id == course_id).\
                        filter(CourseMedia.id == media_id).first()
        return course_media


    def get_all_module_media(self, db, module_id):
        course_media_list = (db.query(CourseMedia).filter(CourseMedia.module_id == module_id).all())
        return course_media_list


    def delete_course_media(self, db, media):
        db.delete(media)
        db.commit()
        
        