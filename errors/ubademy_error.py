class UbademyException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code

class CourseAlreadyAcquired(UbademyException):
    def __init__(self):
        msg = "The course is already acquired by this user"
        super().__init__(status_code = 400, detail = msg)