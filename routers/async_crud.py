# sync_crud.py
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from models import User, Record
from schemas import UserResponse, UserCreateRequest, UserUpdateRequest, RecordCreateRequest, RecordResponse, \
    RecordUpdateRequest
from fastapi import Depends, APIRouter, HTTPException
from database import get_async_postgres_db

router = APIRouter(prefix="/async", tags=["Async"])


#================================================================================================
#                                     USER endpoints
#================================================================================================


@router.post("/users/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreateRequest, db: AsyncSession = Depends(get_async_postgres_db)):
    new_user = User(**user.model_dump())
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    return new_user

@router.get("/users/{user_id}", response_model=UserResponse, status_code=200)
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/users/{user_id}", response_model=UserResponse, status_code=200)
async def update_user(user_id: int, user_update: UserUpdateRequest, db: AsyncSession = Depends(get_async_postgres_db)):

    result = await db.execute(select(User).where(User.id == user_id))
    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for field, value in user_update.model_dump(exclude_unset=True).items():
        setattr(db_user, field, value)

    await db.commit()
    await db.refresh(db_user)

    return db_user


@router.delete("/users/{user_id}", status_code=200)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await db.delete(user)
    await db.commit()
    return {"message": "User deleted"}



#================================================================================================
#                                  RECORD endpoints
#================================================================================================


@router.post("/users/{user_id}/records/", response_model=RecordResponse, status_code=201)
async def create_record(user_id: int, record: RecordCreateRequest, db: AsyncSession = Depends(get_async_postgres_db)):
    new_record = Record(**record.model_dump())
    db.add(new_record)
    await db.commit()
    await db.refresh(new_record)
    return new_record

@router.get("/records/{record_id}", response_model=RecordResponse, status_code=200)
async def read_record(record_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    result = await db.execute(select(Record).where(Record.id == record_id))
    record = result.scalar_one_or_none()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record


@router.put("/records/{record_id}", response_model=RecordResponse, status_code=200)
async def update_record(record_id: int, record_update: RecordUpdateRequest, db: AsyncSession = Depends(get_async_postgres_db)):

    result = await db.execute(select(Record).where(Record.id == record_id))
    record = result.scalar_one_or_none()

    if not record:
        raise HTTPException(status_code=404, detail="Record not found")

    for field, value in record_update.model_dump(exclude_unset=True).items():
        setattr(record, field, value)

    await db.commit()
    await db.refresh(record)

    return record


@router.delete("/records/{record_id}", status_code=200)
async def delete_record(record_id: int, db: AsyncSession = Depends(get_async_postgres_db)):

    result = await db.execute(select(Record).where(Record.id == record_id))
    record = result.scalar_one_or_none()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    await db.delete(record)
    await db.commit()
    return {"message": "Record deleted"}