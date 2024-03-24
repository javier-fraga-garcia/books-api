from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    genre: str
    read: bool = False


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True