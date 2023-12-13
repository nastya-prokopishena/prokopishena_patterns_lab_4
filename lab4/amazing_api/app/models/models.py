from sqlalchemy import Column, ForeignKey, String, Float, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from typing import List

from app.db.database import Base


class Container(Base):
    __tablename__ = "containers"
    container_id = Column(Integer, primary_key=True, index=True)
    weight = Column(Integer)
    type = Column(String)
    item_ids = Column(String)

    items = relationship("Item", back_populates="container")


class Item(Base):
    __tablename__ = "items"

    item_id = Column(Integer, primary_key=True, index=True)
    weight = Column(Float)
    count = Column(Integer)
    container_id = Column(Integer, ForeignKey("containers.container_id"))
    type = Column(String)
    specific_attribute = Column(String)
    container = relationship("Container", back_populates="items")


class Port(Base):
    __tablename__ = "ports"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title = Column(String(80), nullable=False, unique=True, index=True)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    ships: Mapped[List["Ship"]] = relationship(back_populates="port")


class Ship(Base):
    __tablename__ = "ships"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    total_weight_capacity = Column(Integer)
    max_number_of_all_containers = Column(Integer)
    max_number_of_heavy_containers = Column(Integer)
    max_number_of_refrigerated_containers = Column(Integer)
    max_number_of_liquid_containers = Column(Integer)
    fuel_consumption_per_km = Column(Float)
    fuel = Column(Float)
    port_id = Column(Integer, ForeignKey("ports.id"))
    weight = Column(String)



