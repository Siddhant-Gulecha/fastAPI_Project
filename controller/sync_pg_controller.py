# sync_pg_crud.py
from sqlalchemy.orm.session import Session
from repository.sync_crud import SyncCRUD
from schemas import UserResponse, UserCreateRequest, UserUpdateRequest, RecordResponse, RecordCreateRequest, \
    RecordUpdateRequest
from fastapi import Depends, APIRouter
from database import get_sync_postgres_db

router = APIRouter(prefix="/sync_pg", tags=["SyncPg"])


#================================================================================================
#                                     USER endpoints
#================================================================================================

@router.post("/users/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreateRequest, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.create_user(user, db)


@router.get("/users/{user_id}", response_model=UserResponse, status_code=200)
def read_user(user_id: int, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.read_user(user_id, db)


@router.put("/users/{user_id}", response_model=UserResponse, status_code=200)
def update_user(user_id: int, user_update: UserUpdateRequest, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.update_user(user_id, user_update, db)


@router.delete("/users/{user_id}", status_code=200)
def delete_user(user_id: int, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.delete_user(user_id, db)



#================================================================================================
#                                  RECORD endpoints
#================================================================================================


@router.post("/users/{user_id}/records/", response_model=RecordResponse, status_code=201)
def create_record(user_id: int, record: RecordCreateRequest, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.create_record(user_id, record, db)


@router.get("/records/{record_id}", response_model=RecordResponse, status_code=200)
def read_record(record_id: int, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.read_record(record_id, db)


@router.put("/records/{record_id}", response_model=RecordResponse, status_code=200)
def update_record(record_id: int, record_update: RecordUpdateRequest, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.update_record(record_id, record_update, db)


@router.delete("/records/{record_id}", status_code=200)
def delete_record(record_id: int, db: Session = Depends(get_sync_postgres_db)):
    return SyncCRUD.delete_record(record_id, db)