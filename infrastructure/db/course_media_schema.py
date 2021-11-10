from sqlalchemy import (Column, String, Table, MetaData, ForeignKey)
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata = MetaData()

course_media = Table(
    'course_media',
    metadata,
    Column('id', UUID, primary_key=True,default=uuid.uuid4),
    Column('course_id', UUID, ForeignKey('courses.id')),
    Column('url', String(255))
)