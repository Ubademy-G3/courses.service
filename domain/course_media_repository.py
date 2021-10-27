from abc import ABC, abstractmethod


class CourseMediaRepository(ABC):

    @abstractmethod
    def add_course_media(self, payload):
        pass

    @abstractmethod
    def get_all_courses_media(self):
        pass

    @abstractmethod
    def get_course_media_by_id(self, id):
        pass

    @abstractmethod
    def update_course_media(self, id, payload):
        pass

    @abstractmethod
    def delete_course_media(self, id):
        pass

    @abstractmethod
    def delete_all_courses_media(self):
        pass