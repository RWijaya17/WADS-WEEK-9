from sqlalchemy.orm import Session
from models import TodoItem
from schemas import TodoItemCreate, TodoItemUpdate
from uuid import UUID

def get_todo_item(db: Session, todo_id: UUID):
    return db.query(TodoItem).filter(TodoItem.id == todo_id).first()

def get_todo_items(db: Session):
    return db.query(TodoItem).all()

def create_todo_item(db: Session, todo: TodoItemCreate):
    db_todo = TodoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo_item(db: Session, todo_id: UUID, todo_update: TodoItemUpdate):
    db_todo = get_todo_item(db, todo_id)
    if db_todo is None:
        return None
    for attr, value in todo_update.dict().items():
        setattr(db_todo, attr, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo_item(db: Session, todo_id: UUID):
    db_todo = get_todo_item(db, todo_id)
    if db_todo is None:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo