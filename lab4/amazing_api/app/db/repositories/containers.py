from sqlalchemy.orm import Session
from sqlalchemy.future import select

from app.models import models
from app.schemas.containers import Container


class ContainerRepository:
    # Implements Create and Read operations for container objects
    def __init__(self, db_session: Session) -> None:
        self.db_session = db_session

    def create_container(self, container: Container) -> models.Container:
        db_container = models.Container(weight=container.weight, type=container.type, item_ids=container.item_ids)
        self.db_session.add(db_container)
        self.db_session.commit()
        self.db_session.refresh(db_container)
        return db_container

    def get_by_id(self, container_id: int) -> models.Container:
        container = self.db_session.execute(
            select(models.Container).filter(models.Container.container_id == container_id)
        )
        return container.scalars().first()

    def get_all_containers(self):
        containers = self.db_session.execute(select(models.Container).order_by(models.Container.container_id))
        return containers.scalars().all()
