from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session

from todoDTO import Todo, TodoDTO
from todoModel import Base
from db import SessionLocal, engine
from todoService import get_todos, add_todo_to_db, get_todo_by_id, update_todo, delete_todo_by_id

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
def insert_item(todo: TodoDTO, db: Session = Depends(get_db)):
	return add_todo_to_db(db=db, todo=todo)

@app.put("/todos", response_model=Todo)
def update_item(todo_id: int, todo_data: TodoDTO, db: Session = Depends(get_db)):
	details = get_todo_by_id(db=db, todo_id=todo_id)
	if not details:
		raise HTTPException(status_code=404, detail=f"No record found to update")

	return update_todo(db=db, todo_data=todo_data, todo_id=todo_id)

@app.delete("/todos")
def delete_item(todo_id: int, db: Session = Depends(get_db)):
    details = get_todo_by_id(db=db, todo_id=todo_id)
    if not details:
        raise HTTPException(status_code=404, detail=f"No record found to delete")

    try:
        delete_todo_by_id(db=db, todo_id=todo_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Unable to delete: {e}")
    return details
