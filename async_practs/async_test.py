import asyncio
import time

# Test: Two coroutines with different delays.
async def task_one():
    print("Task one starting...")
    # Do NOT use time.sleep() or request.get() inside a async function, because they will freeze the entire loop
    await asyncio.sleep(2)
    print("Task one done in 2 seconds.")

async def task_two():
    print("Task two starting...")
    await asyncio.sleep(3)
    print("Task two done in 3 seconds.")

async def main():
    start = time.time()
    await asyncio.gather(task_one(), task_two())
    end = time.time()
    print(f"Total runtime: {end - start:.2f} seconds")

asyncio.run(main())