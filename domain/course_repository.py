from abc import ABC, abstractmethod

class CourseRepository(ABC):

    @abstractmethod
    def add_course(self, payload):
        pass