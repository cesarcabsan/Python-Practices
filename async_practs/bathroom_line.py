import asyncio
import random

bathroom_lock = asyncio.Lock()

async def use_bathroom(person):
    print(f"Person {person} arrived at the bathroom.")

    # Check if someone is already inside
    if bathroom_lock.locked():
        print(f"Person {person} is waiting its turn...")

    async with bathroom_lock:
        print(f"Person {person} entered the bathroom and locked the door.")

        time_spend = random.uniform(1, 3)
        await asyncio.sleep(time_spend)

        print(f"User {person} left after {time_spend:.1f}s and UNLOCKED the door.")

async def main():
    await asyncio.gather(*(use_bathroom(i) for i in range(1, 6)))

asyncio.run(main())