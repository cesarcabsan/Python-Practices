import asyncio

async def worker(worker_id, semaphore):
    # Request a permit from the semaphore
    async with semaphore:
        print(f"Worker {worker_id} has adquired a permit and now its running")

        # Simulate an I/O operation
        await asyncio.sleep(1) 

        # The permit is automatically released here when exiting the 'async with' block
        print(f"Worker {worker_id} is done and releasing its permit") 


async def main():
    # Task limit concurrency  
    sem = asyncio.Semaphore(3)

    # Create a batch of tasks 
    tasks = [worker(i, sem) for i in range(1, 6)]

    ## Run all tasks concurrently
    await asyncio.gather(*tasks)

asyncio.run(main())