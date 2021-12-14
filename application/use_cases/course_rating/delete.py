from persistence.repositories.course_rating_repository_postgres import CourseRatingRepositoryPostgres
from exceptions.http_error import NotFoundError

crrp = CourseRatingRepositoryPostgres()


def delete_course_rating(db, course_id, rating_id):

    rating = crrp.get_course_rating(db, course_id, rating_id)
    if not rating:
        raise NotFoundError("Rating {} in Course {}".format(rating_id, course_id))
    crrp.delete_course_rating(db, rating)
