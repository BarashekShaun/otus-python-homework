from sqlalchemy.orm import Mapped, mapped_column
from .database import db


class Story(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str | None]
    description: Mapped[str]