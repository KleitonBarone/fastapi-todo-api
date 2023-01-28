from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from todoModel import Base
from db import SessionLocal, engine
from todoService import get_todos

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

@app.get("/todos")
def read_item(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
	todos = get_todos(db=db, skip=skip, limit=limit)
	return todos
