from sqlalchemy.orm import Mapped, mapped_column
import uuid

from core.models.base import Base


class Product(Base):
    __tablename__ = "products"
    id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    price: Mapped[float] = mapped_column()
