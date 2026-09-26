import asyncio
from asyncio import Lock
import aiohttp

cache = dict() # Shared cache to avoid repeated remote calls
lock = Lock() # Lock ensures only one coroutine updates the cache at a time

async def request_remote():
    print("Will request the website to get status.")
    async with aiohttp.ClientSession() as session:
        # Simulate a remote call to fetch status
        response = await session.get("https://www.example.com")
        return response.status

async def get_value(key: str):
     # Prevent race conditions when multiple tasks access the cache
    async with lock:
        if key not in cache:
            print(f"The value of key {key} is not in cache.")
            # First time: fetch from remote and store
            value = await request_remote()
            cache[key] = value
        else:
            print(f"The value of key {key} is already in cache.")        
            # Subsequent calls: reuse cached value    
            value = cache[key]
        print(f"The value of {key} is {value}")
        return value


async def main():
    # Two tasks request the same key concurrently
    task_one = asyncio.create_task(get_value("status"))
    task_two = asyncio.create_task(get_value("status"))

    # Run both tasks together; lock ensures only one fetch happens
    await asyncio.gather(task_one, task_two)

if __name__ == "__main__":
    asyncio.run(main())