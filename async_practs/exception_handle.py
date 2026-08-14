import asyncio

async def square_num(n):
    for i in range(1, n+1):
        print(f"Square of {i} is {i**2}")
        await asyncio.sleep(0.001)

async def square_root(n):
    print(f"Square root of {n} rounded to the nearest integer is ", round(n**.5))

async def divide(dnum1, dnum2):
    if dnum2 == 0:
        raise Exception("Number can't be divided by zero.")
    else:
        print(dnum1/dnum2)
        

# Handling exceptions with Taskgroup
async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(square_num(5))
            tg.create_task(square_root(21))
            tg.create_task(square_root(14))
            ## tasks for testing exception handling
            tg.create_task(divide(10, 0))
            tg.create_task(square_num('five'))
            tg.create_task(square_root('ae'))
    except* TypeError as te:
        for errors in te.exceptions:
            print(errors)
    except* Exception as ex:
        print(ex.exceptions)

    print("All different tasks from task_group() have executed successfully!!")

### Handling exceptions with asyncio.gather()
async def gather_main():
    tasks = asyncio.gather(
        square_num(7),
        square_root(49),
        divide(2, 0),
        square_root('twenty five')
    )
    await tasks

print("Output of Taskgroup with Exception:")
asyncio.run(main())

print("\nOutput of asyncio.gather():")
asyncio.run(gather_main())