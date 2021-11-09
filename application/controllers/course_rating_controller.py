from domain.course_rating_model import *
from application.use_cases.course_rating import (create, get, delete)

class CourseRatingController:

    @classmethod
    async def create_course_rating(self, args, course_id):

        return await create.add_course_rating(course_id, args)


    @classmethod
    def get_all_course_ratings(self, course_id):

        return get.get_all_course_ratings(course_id)


    @classmethod
    async def delete_course_rating(self, course_id, rating_id):
        
        return await delete.delete_course_rating(course_id, rating_id)
