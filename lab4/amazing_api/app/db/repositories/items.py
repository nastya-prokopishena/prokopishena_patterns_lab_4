from sqlalchemy.orm import Session
from sqlalchemy.future import select
from app.models import models
from app.schemas.items import Item


class ItemRepository:
    # Implements Create and Read operations for item objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_item(self, item: Item) -> models.Item:
        db_item = models.Item(
            weight=item.weight,
            count=item.count,
            container_id=item.container_id,
            type=item.type,
            specific_attribute=item.specific_attribute
        )
        self.db_session.add(db_item)
        self.db_session.commit()
        self.db_session.refresh(db_item)
        return db_item

    def get_by_id(self, item_id: int) -> models.Item:
        item = self.db_session.execute(
            select(models.Item).filter(models.Item.item_id == item_id)
        )
        return item.scalars().first()

    def get_all_items(self):
        items = self.db_session.execute(select(models.Item).order_by(models.Item.item_id))
        return items.scalars().all()
