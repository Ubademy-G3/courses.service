from sqlalchemy import (Column, Integer, String, Table, ARRAY, MetaData)

metadata = MetaData()

courses = Table(
    'courses',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)