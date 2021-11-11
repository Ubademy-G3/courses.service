from abc import ABC, abstractmethod


class CourseRatingRepository(ABC):

    @abstractmethod
    def add_course_rating(self, payload):
        pass


    @abstractmethod
    def get_all_course_ratings(self, course_id):
        pass


    @abstractmethod
    def get_course_rating(self, course_id, rating_id):
        pass


    @abstractmethod
    def get_course_rating_from(self, user_id, course_id):
        pass
        

    @abstractmethod
    def delete_course_rating(self, course_id, rating_id):
        pass
