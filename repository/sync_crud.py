# sync crud.py
from http.client import HTTPException
from sqlalchemy.orm.session import Session
from models import User, Record
from schemas import UserCreateRequest, UserUpdateRequest, RecordCreateRequest, RecordUpdateRequest



class SyncCRUD:

    #================================================================================================
    #                                    SYNC USER CRUD
    #================================================================================================


    def create_user(user: UserCreateRequest, db: Session ):
        new_user = User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user



    def read_user(user_id: int, db: Session ):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user



    def update_user(user_id: int, user_update: UserUpdateRequest, db: Session ):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        for field, value in user_update.model_dump(exclude_unset=True).items():
            setattr(user, field, value)

        db.commit()
        db.refresh(user)
        return user



    def delete_user(user_id: int, db: Session ):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        db.delete(user)
        db.commit()
        return {"message": "User deleted"}



    #================================================================================================
    #                                   SYNC RECORD CRUD
    #================================================================================================



    def create_record(user_id: int, record: RecordCreateRequest, db: Session ):
        new_record = Record(**record.model_dump())
        db.add(new_record)
        db.commit()
        db.refresh(new_record)
        return new_record



    def read_record(record_id: int, db: Session ):
        record = db.query(Record).filter(Record.id == record_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        return record



    def update_record(record_id: int, record_update: RecordUpdateRequest, db: Session ):
        record = db.query(Record).filter(Record.id == record_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")

        for field, value in record_update.model_dump(exclude_unset=True).items():
            setattr(record, field, value)

        db.commit()
        db.refresh(record)
        return record



    def delete_record(record_id: int, db: Session ):
        record = db.query(Record).filter(Record.id == record_id).first()
        if not record:
            raise HTTPException(status_code=404, detail="Record not found")
        db.delete(record)
        db.commit()
        return {"message": "Record deleted"}
