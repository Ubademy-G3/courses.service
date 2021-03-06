from fastapi import HTTPException


class NotFoundError(HTTPException):
    def __init__(self, item):
        msg = f"{item} not found"
        super().__init__(status_code=404, detail=msg)
