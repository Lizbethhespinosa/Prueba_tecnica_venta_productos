from sqlalchemy import Column, Integer, ForeignKey
from app.config.database import Base

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    total_productos = Column(Integer, nullable=False)