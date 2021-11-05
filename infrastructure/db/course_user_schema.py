from sqlalchemy import (Column, Integer, String, Table, MetaData, Boolean,
                        ForeignKey)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

course_users= Table(
    'course_users',
    metadata,
    Column('id', UUID, primary_key=True),
    Column('course_id', UUID, ForeignKey('courses.id')),
    Column('user_id', UUID),    
    Column('user_type',ARRAY(String(255))),
    Column('progress', Integer),
    Column('aprobal_state',Boolean)
)