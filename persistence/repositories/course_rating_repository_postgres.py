from infrastructure.db.course_rating_schema import CourseRating
from sqlalchemy import func

class CourseRatingRepositoryPostgres():

    def add_course_rating(self, db, payload):
        db.add(payload)
        db.commit()


    def get_all_course_ratings(self, db, course_id):
        course_rating_list = db.query(CourseRating).filter(CourseRating.course_id == course_id).all()
        return course_rating_list

       
    def get_course_rating(self, db, course_id, rating_id):
        rating = db.query(CourseRating).filter(CourseRating.course_id == course_id).\
                        filter(CourseRating.id == rating_id).first()
        return rating


    def get_course_rating_from(self, db, user_id, course_id):
        rating = db.query(CourseRating).filter(CourseRating.course_id == course_id).\
                        filter(CourseRating.user_id == user_id).first()
        return rating

    def delete_course_rating(self, db, rating):
        db.delete(rating)
        db.commit()