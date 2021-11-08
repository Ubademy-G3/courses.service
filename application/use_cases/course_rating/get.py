from persistence.repositories.course_rating_repository_postgres import CourseRatingRepositoryPostgres
from errors.http_error import NotFoundError

crrp = CourseRatingRepositoryPostgres()

async def get_all_course_ratings(course_id):

    ratings_list = await crrp.get_all_course_ratings(course_id)
    if ratings_list is None or len(ratings_list) == 0:
        raise NotFoundError("Ratings")
    return ratings_list


async def get_course_rating(course_id, rating_id):

    rating = await crrp.get_course_rating(course_id, rating_id)
    if rating is None:
        raise NotFoundError("Rating {} in course {}".format(rating_id,course_id))
    return rating


async def course_already_scored(course_id, user_id):

    return await crrp.get_course_rating_from(user_id, course_id) != None