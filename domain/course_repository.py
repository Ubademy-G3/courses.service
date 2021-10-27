from abc import ABC, abstractmethod


class CourseRepository(ABC):

    @abstractmethod
    def add_course(self, payload):
        pass

    @abstractmethod
    def get_all_courses(self):
        pass

    @abstractmethod
    def get_course_by_id(self, id):
        pass

    @abstractmethod
    def update_course(self, id, payload):
        pass

    @abstractmethod
    def delete_course_by_id(self, id):
        pass

    @abstractmethod
    def delete_all_courses(self):
        pass
