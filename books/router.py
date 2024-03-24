from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from db.database import Sessionlocal, engine
from db.crud import get_all_books, get_book, create_book, update_book
from db import schemas, models

router = APIRouter(prefix='/api/books', tags=['books'])

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally: 
        db.close()

dbDependency = Annotated[Session, Depends(get_db)]

@router.get('/', response_model=list[schemas.Book])
async def get_books(db: dbDependency):
    books = get_all_books(db)
    if books == []:
        raise HTTPException(status_code=404, detail='No books found')
    return books

@router.get('/{id}', response_model=schemas.Book)
async def get_book_by_id(id: int, db: dbDependency):
    book = get_book(db, id)
    if not book:
        raise HTTPException(status_code=404, detail=f'Book with id {id} not found')
    return book

@router.post('/', response_model=schemas.Book)
async def create_book_route(book: schemas.BookBase, db: dbDependency):
    return create_book(db=db, book=book)

@router.post('/background')
async def create_book_route_background(book: schemas.BookBase, db: dbDependency, backgroudTask: BackgroundTasks):
    backgroudTask.add_task(create_book, db, book)
    return {'msg': 'book created'}

@router.put('/{id}', response_model=schemas.Book)
async def update_book_route(id: int, book: schemas.BookBase, db: dbDependency):
    db_book = get_book(db, id)
    if not db_book:
        raise HTTPException(status_code=400, detail=f'Book with id {id} not exists')
    return update_book(db=db, db_book=db_book, book=book)