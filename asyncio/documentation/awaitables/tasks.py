import asyncio

async def nested():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())
    # create tasks won't run intially, but they run together when you call await on them as opposed
    # to coroutines which seem to run immediately if await called on them
    print( await task)

asyncio.run(main())

# we use tasks to schedule coroutines to run concurrently