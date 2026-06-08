from fastapi import APIRouter, Depends, HTTPException


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
async def create_new_user(
    user: UserCreate
):

    return await create_user(user)


# OBTENER TODOS
@router.get(
    "/",
    response_model=list[UserResponse]
)
async def get_all_users():

    return await get_users()

# OBTENER POR ID
@router.get(
    "/{user_id}",
    response_model=UserResponse
)
async def get_user(
    user_id: int
):

    user = await get_user_by_id(user_id)

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
async def update_existing_user(
    user_id: int,
    user_data: UserUpdate
):

    updated_user = await update_user(
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
async def delete_existing_user(
    user_id: int
):

    deleted_user = await delete_user(
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