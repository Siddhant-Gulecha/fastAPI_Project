# async_pg_crud.py
from sqlalchemy.ext.asyncio.session import AsyncSession
from repository.async_crud import AsyncCRUD
from schemas import UserResponse, UserCreateRequest, UserUpdateRequest, RecordCreateRequest, RecordResponse, \
    RecordUpdateRequest
from fastapi import Depends, APIRouter
from database import get_async_postgres_db


router = APIRouter(prefix="/async_pg", tags=["AsyncPg"])


#================================================================================================
#                                     USER endpoints
#================================================================================================


@router.post("/users/", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreateRequest, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.create_user(user,db)

@router.get("/users/{user_id}", response_model=UserResponse, status_code=200)
async def read_user(user_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.read_user(user_id, db)


@router.put("/users/{user_id}", response_model=UserResponse, status_code=200)
async def update_user(user_id: int, user_update: UserUpdateRequest, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.update_user(user_id, user_update, db)


@router.delete("/users/{user_id}", status_code=200)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.delete_user(user_id, db)



#================================================================================================
#                                  RECORD endpoints
#================================================================================================


@router.post("/users/{user_id}/records/", response_model=RecordResponse, status_code=201)
async def create_record(user_id: int, record: RecordCreateRequest, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.create_record(user_id, record, db)

@router.get("/records/{record_id}", response_model=RecordResponse, status_code=200)
async def read_record(record_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.read_record(record_id, db)


@router.put("/records/{record_id}", response_model=RecordResponse, status_code=200)
async def update_record(record_id: int, record_update: RecordUpdateRequest, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.update_record(record_id, record_update, db)


@router.delete("/records/{record_id}", status_code=200)
async def delete_record(record_id: int, db: AsyncSession = Depends(get_async_postgres_db)):
    return await AsyncCRUD.delete_record(record_id, db)