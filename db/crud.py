from sqlalchemy.orm import Session

from . import models, schemas

def get_book(db: Session, id: str):
    return db.query(models.Book).filter(models.Book.id == id).first()

def get_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(models.Book.title == title).first()

def get_all_books(db: Session):
    return db.query(models.Book).all()

def create_book(db: Session, book: schemas.BookBase):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    return db_book

def update_book(db: Session, db_book: models.Book, book: schemas.BookBase):
    for key, value in book.model_dump().items():
        setattr(db_book, key, value)
        db.commit()
    return db_book