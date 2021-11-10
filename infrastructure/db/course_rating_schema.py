from sqlalchemy import (Column, String, Table, MetaData, ForeignKey, Integer)
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata = MetaData()

course_ratings = Table(
    'course_ratings',
    metadata,
    Column('id', UUID, primary_key=True,default=uuid.uuid4),
    Column('course_id', UUID, ForeignKey('courses.id')),
    Column('user_id', UUID, ForeignKey('course_users.user_id')),
    Column('score', Integer),
    Column('opinion', String(500))
)