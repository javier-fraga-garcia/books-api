from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from books.router import router as books_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*']
)
app.include_router(books_router)

@app.get('/')
def home():
    return {'msg': 'App running!'}