from abc import ABC, abstractmethod


class CourseCategoryRepository(ABC):

    @abstractmethod
    def add_course_category(self, payload):
        pass


    @abstractmethod
    def get_course_category(self, category_id):
        pass
        

    @abstractmethod
    def delete_course_category(self, category_id):
        pass
