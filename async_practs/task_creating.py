import asyncio
import time

# Simulated async function to fetch data
async def fetch_data(source: str, delay: int):
    print(f"Starting fetch from {source}...")
    await asyncio.sleep(delay)  # simulate network delay
    print(f"Finished fetch from {source}")
    return f"Data from {source}"

async def main():
    weather_task = asyncio.create_task(fetch_data("Weather API", 2))
    stocks_task = asyncio.create_task(fetch_data("Stocks API", 3))
    news_task = asyncio.create_task(fetch_data("News API", 1))

    # Gather results concurrently
    results = await asyncio.gather(weather_task, stocks_task, news_task)

    print("\nAll results collected:")
    for result in results:
        print(result)

# Measure total runtime
start = time.perf_counter()
asyncio.run(main())
end = time.perf_counter()

print(f"\nTotal running time: {end - start:.2f} seconds")