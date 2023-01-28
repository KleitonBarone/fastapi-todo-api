from pydantic import BaseModel

class TodoDTO(BaseModel):
	name: str
	isdone: str
	
	class Config:
		orm_mode = True
