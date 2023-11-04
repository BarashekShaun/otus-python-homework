"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio
import json

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_users_data(): 
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_DATA_URL) as resp:
            user_data = await resp.json()
    
        return user_data
    

async def fetch_posts_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(POSTS_DATA_URL) as resp:
            user_posts = await resp.json()
    
        return user_posts


def main():
    asyncio.run(fetch_users_data())
    asyncio.run(fetch_posts_data())



if __name__ == '__main__':
    main()
