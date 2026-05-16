from typing import List, Optional
from sqlalchemy import String, Text, Numeric, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

import datetime

from .base import Base


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    url: Mapped[str] = mapped_column(Text, nullable=False)
    store: Mapped[Optional[str]] = mapped_column(String(50))
    scraping_strategy: Mapped[str] = mapped_column(String(50), default='CSS')
    selector: Mapped[str] = mapped_column(Text, nullable=False)
    target_price: Mapped[float] = mapped_column(Numeric(12, 2), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    status: Mapped[str] = mapped_column(String(50), default='activo')

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now(datetime.timezone.utc),
                                                          onupdate=datetime.datetime.now(datetime.timezone.utc))
    
    prices: Mapped[List['PriceHistorical']] = relationship(back_populates='product', cascade='all, delete-orphan')
    logs: Mapped[List['Log']] = relationship(back_populates='product', cascade='all, delete-orphan')
