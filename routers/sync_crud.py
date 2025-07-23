# sync_crud.py
from sqlalchemy.orm import Session
from models import User, MainRecord

def create_user(db: Session, name: str, email: str, age: int):
    user = User(name=name, email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_record(db: Session, user_id: int, data: str):
    record = MainRecord(user_id=user_id, record_data=data)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record


# async_crud.py
from sqlalchemy.future import select
from models import User, MainRecord

async def create_user(db, name: str, email: str, age: int):
    user = User(name=name, email=email, age=age)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user(db, user_id: int):
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalar_one_or_none()

async def create_record(db, user_id: int, data: str):
    record = MainRecord(user_id=user_id, record_data=data)
    db.add(record)
    await db.commit()
    await db.refresh(record)
    return record
