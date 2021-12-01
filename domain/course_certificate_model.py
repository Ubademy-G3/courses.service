from pydantic import BaseModel
from uuid import UUID, uuid4
from typing import List,Optional

class CourseCertificateSchema(BaseModel):
    course_id: UUID
    user_id: UUID
    pdf_path: str


class CourseCertificateDB(CourseCertificateSchema):
    id: UUID


class CourseCertificateList(BaseModel):
    amount: int
    user_id: UUID
    certificates: List[CourseCertificateDB]
    

