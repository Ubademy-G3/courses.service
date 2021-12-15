class UbademyException(Exception):
    def __init__(self, status_code, detail):
        super().__init__(detail)
        self.detail = detail
        self.status_code = status_code


class CourseAlreadyAcquired(UbademyException):
    def __init__(self):
        msg = "Course already acquired by this user"
        super().__init__(status_code=400, detail=msg)


class CourseAlreadyScored(UbademyException):
    def __init__(self):
        msg = "Course already scored by this user"
        super().__init__(status_code=400, detail=msg)


class CourseNotAcquired(UbademyException):
    def __init__(self):
        msg = "Course not acquired by this user"
        super().__init__(status_code=400, detail=msg)
