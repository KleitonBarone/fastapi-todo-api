from sqlalchemy.orm import Session
import todoModel

def get_todos(db: Session, skip: int = 0, limit: int = 100):
	return db.query(todoModel.Todo).offset(skip).limit(limit).all()
