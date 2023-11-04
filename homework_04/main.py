"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.pyhttps://jsonplaceholder.typicode.com/poststhon.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from models import (
    Base,
    engine,
    async_session,
    User,
    Post,
)
from jsonplaceholder_requests import (
    fetch_posts_data,
    fetch_users_data,
)


async def create_users(
        session: AsyncSession,
        username: str,
        email: str,
        name: str,
        user_id: int
) -> User:
    user = User(username=username, email=email, name=name, id=user_id)
    session.add(user)
    await session.commit()
    print("user", username, "value:", user)
    return user


async def create_posts(
        session: AsyncSession,
        title: str,
        body: str,
        user: User
) -> Post:
    post = Post(
        title=title,
        user_id=user.id,
        body=body
    )
    session.add(post)
    await session.commit()
    print("created", post)
    return post



async def run_queries():
    users, posts = await asyncio.gather(
    fetch_users_data(),
    fetch_posts_data(),
    )
    async with async_session() as session:
        result = await asyncio.gather(
        *[
            create_users(
            session=session,
            username=i['username'],
            email=i['email'],
            name=i['name'],
            user_id=int(i['id'])) for i in users
        ],

        *[
            create_posts(
            session=session,
            title=i['title'],
            body=i['body'],
            user=User) for i in posts
        ]  
        )



async def async_main():
    # async with engine.begin() as conn:
    #     #     await conn.run_sync(Base.metadata.drop_all)
    #     #     await conn.run_sync(Base.metadata.create_all)
    await asyncio.gather(run_queries())


def main():
    asyncio.run(async_main())
    

if __name__ == "__main__":
    main()
