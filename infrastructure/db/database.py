from sqlalchemy import (create_engine)
import os
from databases import Database

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)
