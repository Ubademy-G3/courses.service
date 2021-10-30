from sqlalchemy import (Column, Integer, String, Table, MetaData)
from sqlalchemy.dialects.postgresql import (UUID, ARRAY)
import uuid

metadata = MetaData()

courses = Table(
    'courses',
    metadata,
    Column('id', UUID, primary_key=True,default=uuid.uuid4),
    Column('name', String(255), nullable=False),
    Column('description',String(255), nullable=False),
    Column('hashtags', ARRAY(String(255))),
    Column('kind',String(255), nullable=False),
    Column('subscription_type',ARRAY(String(255))),
    Column('location',String(255))
)