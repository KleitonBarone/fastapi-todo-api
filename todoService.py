from sqlalchemy.orm import Session
import todoModel
import todoDTO

def get_todos(db: Session, skip: int = 0, limit: int = 100):
	return db.query(todoModel.Todo).offset(skip).limit(limit).all()

def get_todo_by_id(db: Session, todo_id: int):
	return db.query(todoModel.Todo).filter(todoModel.Todo.id == todo_id).first()

def add_todo_to_db(db: Session, todo: todoDTO.TodoDTO):
	new_todo = todoModel.Todo(
		name=todo.name,
		isdone=todo.isdone
	)
	db.add(new_todo)
	db.commit()
	db.refresh(new_todo)
	return todoModel.Todo(**todo.dict())
