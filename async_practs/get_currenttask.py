import asyncio

# Example: Getting the Current Task From Another Coroutine
async def my_coroutine():
    print("Executing the coroutine.") # Start message
    my_task = asyncio.current_task() # Get current task
    print(my_task) # Report details

# Main coroutine  
async def main():
    print("Main coroutine started.")
    await my_coroutine()
    print("Main coroutine done.")

asyncio.run(main())

 