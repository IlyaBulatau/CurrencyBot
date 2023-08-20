import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    tg_id = db.Column(db.BigInteger(), unique=True, nullable=False)
    username = db.Column(db.String(), nullable=False, default="Doen't have username")
    date_add = db.Column(db.DateTime(), nullable=False, server_default=db.sql.func.now())

class Bank(Base):
    __tablename__ = "banks"

    id = db.Column(db.UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    buy_currency = db.Column(db.Float(), nullable=True)
    surrender_currency = db.Column(db.Float(), nullable=True)
    update_time = db.Column(db.DateTime(), onupdate=db.sql.func.now())

