from abc import ABC, abstractmethod


class CourseRepository(ABC):

    @abstractmethod
    def add_course(self, db, payload):
        pass


    @abstractmethod
    def get_all_courses(self, db):
        pass


    @abstractmethod
    def get_course_by_id(self, db, course_id):
        pass


    @abstractmethod
    def update_course(self, db, course_id, payload):
        pass
        

    @abstractmethod
    def delete_course(self, db, course_id):
        pass
