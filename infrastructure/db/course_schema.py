from sqlalchemy import (Column, Integer, String, Table, MetaData, Text, JSON)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

courses = Table(
    'courses',
    metadata,
    Column('id', UUID, primary_key = True,default = uuid.uuid4),
    Column('name', String(255), nullable = False),
    Column('description', Text, nullable = False),
    Column('category', Integer, nullable = False),
    Column('kind', String(255), nullable = False),
    Column('subscription_type', String(255), nullable = False),
    Column('location', String(255), nullable = False),
    Column('info', JSON, nullable = False),
    Column('profile_picture', String(255), nullable = False)
)