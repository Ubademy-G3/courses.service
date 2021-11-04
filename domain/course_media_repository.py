from abc import ABC, abstractmethod


class CourseMediaRepository(ABC):

    @abstractmethod
    def add_course_media(self, payload):
        pass

    @abstractmethod
    def get_all_course_media(self, course_id):
        pass

    @abstractmethod
    def get_course_media_by_id(self, id):
        pass

    @abstractmethod
    def delete_course_media(self, id):
        pass
