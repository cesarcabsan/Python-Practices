import time
import asyncio

### Synchronous version
def sync_sleep():
    for i in range(3):
        print(f"Sync: Sleeping {i+1}...")
        time.sleep(2)  # blocks the entire program for 2 seconds
    print("Sync: Done!")

start = time.time()
sync_sleep()
end = time.time()
print(f"Sync total runtime: {end - start:.2f} seconds") # Expected runtime ~ 6 seconds (since each sleep is sequential)


### Asynchronous version
async def async_sleep_task(n):
    print(f"Async: Sleeping {n}...")
    await asyncio.sleep(2)  # non-blocking sleep
    print(f"Async: Done sleeping {n}!")

async def main():
    # Launch 3 tasks concurrently
    tasks = [async_sleep_task(i+1) for i in range(3)]
    await asyncio.gather(*tasks)

start = time.time()
asyncio.run(main())
end = time.time()
print(f"Async total runtime: {end - start:.2f} seconds") # Expected runtime ~ 2.01 seconds (all three sleeps overlap)
# -------------------------------
# Runtime comparison:
# Sync version: ~6 seconds
# Async version: ~2.01 seconds
# Async is faster because tasks run concurrently, in contrast of Sync who runs them sequentially.
