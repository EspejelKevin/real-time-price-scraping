from sqlalchemy import ForeignKey, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import datetime

from .base import Base


class PriceHistorical(Base):
    __tablename__ = 'price_historical'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id', ondelete='CASCADE'), nullable=False)
    price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))

    product: Mapped['Product'] = relationship(back_populates='prices')
