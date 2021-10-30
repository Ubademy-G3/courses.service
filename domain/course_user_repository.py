from abc import ABC, abstractmethod


class CourseUserRepository(ABC):

    @abstractmethod
    def add_course_user(self, payload):
        pass

    @abstractmethod
    def get_all_course_users(self):
        pass

    @abstractmethod
    def get_course_user_by_id(self, id):
        pass

    @abstractmethod
    def delete_course_user(self, id):
        pass

    @abstractmethod
    def delete_all_course_users(self):
        pass