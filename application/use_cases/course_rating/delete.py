from persistence.repositories.course_rating_repository_postgres import CourseRatingRepositoryPostgres
from errors.http_error import NotFoundError

crrp = CourseUserRepositoryPostgres()

async def delete_course_rating(course_id, rating_id):

    rating = await crrp.get_course_rating(course_id, rating_id)
    if not rating:
        raise NotFoundError("Rating {} in Course {}".format(rating_id,course_id))
    return await crrp.delete_course_rating(course_id, rating_id)