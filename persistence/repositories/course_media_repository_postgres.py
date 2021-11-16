from infrastructure.db.course_media_schema import CourseMedia
from sqlalchemy import func


class CourseMediaRepositoryPostgres():

    def add_course_media(self, db, payload):
        db.add(payload)
        db.commit()


    def get_all_course_media(self, db, course_id):
        course_media_list = (db.query(CourseMedia).filter(CourseMedia.course_id == course_id).all())
        return course_media_list

       
    def get_course_media(self, db, course_id, media_id):
        course_media = db.query(CourseMedia).filter(CourseMedia.course_id == course_id).\
                        filter(CourseMedia.id == media_id).first()
        return course_media


    def delete_course_media(self, db, media):
        db.delete(media)
        db.commit()
        
        