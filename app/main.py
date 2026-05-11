from fastapi import FastAPI
from app.config.database import engine, Base

from app.models.user_model import User
from app.models.product_model import Product
from app.models.purchase_model import Purchase

from app.routers import user_router
from app.routers import product_router
from app.routers import purchase_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(user_router.router)
app.include_router(product_router.router)
app.include_router(purchase_router.router)

@app.get("/")
async def root():
    return {"message": "API Running"}