from infrastructure.db.course_rating_schema import CourseRating

class CourseRatingSerializer:

    @classmethod
    def serialize(self, rating: CourseRating):
        
        return {
            "id": rating.id,
            "course_id": rating.course_id,
            "user_id": rating.user_id,
            "score": rating.score,
            "opinion": rating.opinion
        }