from sqlalchemy import Column, String, Boolean, Integer
import uuid

from .database import Base

class Book(Base):
    __tablename__ = 'books'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    title = Column('title', String)
    author = Column('author', String)
    genre = Column('genre', String)
    read = Column('read', Boolean, default=False)
