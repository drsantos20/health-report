import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine
)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()
notes = Table(
    "covid",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("country", String(50)),
    Column("confirmed", Integer, default=0, nullable=False),
    Column("deaths", Integer, default=0, nullable=False),
    Column("recovered", Integer, default=0, nullable=False),
    Column("last_update", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)