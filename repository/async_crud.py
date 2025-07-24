# async crud
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.future import select
from models import User, Record
from schemas import  UserCreateRequest, UserUpdateRequest, RecordCreateRequest, RecordUpdateRequest
from fastapi import HTTPException


class AsyncCRUD:



#================================================================================================
#                                      ASYNC USER CRUD
#================================================================================================

    @staticmethod
    async def create_user(user: UserCreateRequest, db: AsyncSession):
        new_user = User(**user.model_dump())
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user


    @staticmethod
    async def read_user(user_id: int, db: AsyncSession):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user


    @staticmethod
    async def update_user(user_id: int, user_update: UserUpdateRequest, db: AsyncSession):

        result = await db.execute(select(User).where(User.id == user_id))
        db_user = result.scalar_one_or_none()

        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")

        for field, value in user_update.model_dump(exclude_unset=True).items():
            setattr(db_user, field, value)

        await db.commit()
        await db.refresh(db_user)

        return db_user


    @staticmethod
    async def delete_user(user_id: int, db: AsyncSession):
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        await db.delete(user)
        await db.commit()
        return {"message": "User deleted"}



    #================================================================================================
    #                                   ASYNC RECORD CRUD
    #================================================================================================


    @staticmethod
    async def create_record(user_id: int, record: RecordCreateRequest, db: AsyncSession):
        new_record = Record(**record.model_dump(), user_id=user_id)
        db.add(new_record)
        await db.commit()
        await db.refresh(new_record)
        return new_record


    @staticmethod
    async def read_record(record_id: int, db: AsyncSession):
        result = await db.execute(select(Record).where(Record.id == record_id))
        record = result.scalar_one_or_none()
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        return record


    @staticmethod
    async def update_record(record_id: int, record_update: RecordUpdateRequest, db: AsyncSession):

        result = await db.execute(select(Record).where(Record.id == record_id))
        record = result.scalar_one_or_none()

        if not record:
            raise HTTPException(status_code=404, detail="Record not found")

        for field, value in record_update.model_dump(exclude_unset=True).items():
            setattr(record, field, value)

        await db.commit()
        await db.refresh(record)

        return record


    @staticmethod
    async def delete_record(record_id: int, db: AsyncSession):

        result = await db.execute(select(Record).where(Record.id == record_id))
        record = result.scalar_one_or_none()
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        await db.delete(record)
        await db.commit()
        return {"message": "Record deleted"}