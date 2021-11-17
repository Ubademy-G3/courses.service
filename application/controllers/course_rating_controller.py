from application.use_cases.course_rating import (create, get, delete)

class CourseRatingController:

    @classmethod
    def create_course_rating(self, db, args, course_id):

        return create.add_course_rating(db, course_id, args)


    @classmethod
    def get_all_course_ratings(self, db, course_id):

        return get.get_all_course_ratings(db, course_id)


    @classmethod
    async def delete_course_rating(self, db, course_id, rating_id):
        
        return await delete.delete_course_rating(db, course_id, rating_id)
