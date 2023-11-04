"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio
from datetime import datetime

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    declared_attr,
    sessionmaker,
    relationship,
)
from sqlalchemy import (
    Column,
    String,
    Text,
    DateTime,
    ForeignKey,
    Integer,
    func
)
from config import DB_URL, DB_ECHO


engine = create_async_engine(url=DB_URL, echo=DB_ECHO)

async_session = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession,
)

Base = declarative_base()




class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    name = Column(String(40), nullable=True, unique=False)
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return (f"User(id={self.id}, username={self.username!r}, "
                f"email={self.email!r}, is_staff={self.name})")

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(
        String(120),
        nullable=False,
        unique=False,
    )
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default="",
    )
    published_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )

    user = relationship(
        "User",
        back_populates="posts",
        uselist=False,
    )

    @property
    def body_len(self):
        return len(self.body)

    def __str__(self):
        return f"Post(id={self.id}, title={self.title!r})"

    def __repr__(self):
        """
        :return:
        """
        return str(self)



