from abc import ABC, abstractmethod


class CourseRepository(ABC):

    @abstractmethod
    def add_course(self, payload):
        pass


    @abstractmethod
    def get_all_courses(self):
        pass


    @abstractmethod
    def get_course(self, course_id):
        pass


    @abstractmethod
    def update_course(self, course_id, payload):
        pass
        

    @abstractmethod
    def delete_course(self, course_id):
        pass
