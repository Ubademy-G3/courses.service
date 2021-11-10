from abc import ABC, abstractmethod


class CourseUserRepository(ABC):

    @abstractmethod
    def add_course_user(self, payload):
        pass

    @abstractmethod
    def get_all_course_users(self, course_id):
        pass

    @abstractmethod
    def get_course_user(self, course_id, user_id):
        pass

    @abstractmethod
    def delete_course_user(self, course_id, user_id):
        pass
