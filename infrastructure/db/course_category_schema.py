from sqlalchemy import (Column, Integer, String, Table, MetaData)

metadata = MetaData()

course_categories = Table(
    'course_categories',
    metadata,
    Column('id', Integer, primary_key = True, autoincrement = True),
    Column('name', String(255), nullable = False)
)