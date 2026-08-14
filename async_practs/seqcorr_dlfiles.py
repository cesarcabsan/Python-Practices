import asyncio
import time

## Simulates downloading 3 files. 
# Do it sequentially (taking 3 seconds total) and then use asyncio.gather() to do it concurrently (taking 1 second total).

async def download_file(name, delay):
    print(f"Starting download: {name}...")
    await asyncio.sleep(delay)
    print(f"Finished download: {name}")


async def sequential_downloads():
    start = time.perf_counter()
    await download_file("File 1", 1)
    await download_file("File 2", 1)
    await download_file("File 3", 1)
    end = time.perf_counter()
    print(f"Sequential downloads took {end - start:.2f} seconds\n")


async def concurrent_downloads():
    start = time.perf_counter()
    await asyncio.gather(
        download_file("File 1", 1),
        download_file("File 2", 1),
        download_file("File 3", 1),
        return_exceptions=True
    )
    end = time.perf_counter()
    print(f"Concurrent downloads took {end - start:.2f} seconds\n")

async def main():
    print("====Sequential====")
    await sequential_downloads()
    print("====Concurrent====")
    await concurrent_downloads()

asyncio.run(main())