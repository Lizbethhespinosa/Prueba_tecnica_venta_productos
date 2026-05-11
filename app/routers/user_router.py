from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.config.database import get_db

from app.schemas.user_schema import (
    UserCreate,
    UserResponse,
    UserUpdate
)

from app.services.user_service import (
    create_user,
    get_users,
    get_user_by_id,
    update_user,
    delete_user
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# CREAR USUARIO
@router.post(
    "/",
    response_model=UserResponse,
    status_code=201
)
def create_new_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):

    return create_user(db, user)


# OBTENER TODOS
@router.get(
    "/",
    response_model=list[UserResponse]
)
def get_all_users(
    db: Session = Depends(get_db)
):

    return get_users(db)


# OBTENER POR ID
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return user


# ACTUALIZAR
@router.put(
    "/{user_id}",
    response_model=UserResponse
)
def update_existing_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):

    updated_user = update_user(
        db,
        user_id,
        user_data
    )

    if not updated_user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return updated_user


# ELIMINAR
@router.delete("/{user_id}")
def delete_existing_user(
    user_id: int,
    db: Session = Depends(get_db)
):

    deleted_user = delete_user(
        db,
        user_id
    )

    if not deleted_user:
        raise HTTPException(
            status_code=404,
            detail="Usuario no encontrado"
        )

    return {
        "message": "Usuario eliminado correctamente"
    }