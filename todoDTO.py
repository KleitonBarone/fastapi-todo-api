from pydantic import BaseModel

class TodoDTO(BaseModel):
	name: str
	isdone: bool
	
	class Config:
		orm_mode = True

class Todo(TodoDTO):
	id: int

	class Config:
		orm_mode = True
