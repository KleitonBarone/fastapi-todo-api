from fastapi import FastAPI, Depends
from typing import List
from sqlalchemy.orm import Session

from todoDTO import Todo, TodoDTO
from todoModel import Base
from db import SessionLocal, engine
from todoService import get_todos, add_todo_to_db

Base.metadata.create_all(bind=engine)

app = FastAPI(
	title="Todo API",
	description="CRUD operations of TODOs using this API",
	version="1.0.0",
)

def get_db():
	db = SessionLocal()
	try:
		yield db
	finally:
		db.close()

@app.get("/health")
def health():
	return {"status": "UP"}

@app.get("/todos", response_model=List[Todo])
def read_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	todos = get_todos(db=db, skip=skip, limit=limit)
	return todos

@app.post("/todos", response_model=TodoDTO)
def read_item(todo: TodoDTO, db: Session = Depends(get_db)):
	return add_todo_to_db(db=db, todo=todo)
