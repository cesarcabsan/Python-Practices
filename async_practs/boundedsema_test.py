import asyncio
import random

async def access_resource(task_id, semaphore):
    # 'async with' automatically acquires the semaphore and releases it when done
    async with semaphore:
        print(f"[Task {task_id}] Acquired slot. Processing...")

    # Simulate variable I/O operations (like a database or API call) 
    await asyncio.sleep(random.uniform(0.5, 1.5))

    print(f"[Task {task_id}] Done. Releasing slot.")

"""""
# Error demonstration
async def error_demonstration():
    sem = asyncio.BoundedSemaphore(1) # Limit of 1

    await sem.acquire()
    sem.release() # Makes counter go back to 1

    # Accidental duplicate release call
    try:
        sem.release()
    except ValueError as e:
        print(f"Caught expected error: {e}")

asyncio.run(error_demonstration()) # Output: Caught expected error: BoundedSemaphore released too many times
"""""

async def main():
     # Initialize the bounded semaphore with a maximum limit of 2 concurrent slots
     semaphore = asyncio.BoundedSemaphore(2)

     # Create a batch of 5 concurrent tasks
     tasks = [access_resource(i, semaphore) for i in range(1, 6)]

     # Run all tasks concurrently
     await asyncio.gather(*tasks)

asyncio.run(main())
