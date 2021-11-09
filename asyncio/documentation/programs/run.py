# use asyncio.run(coroutine, *, debug=False) to run an asynchronous program
# this also manages asyncio event loop doing low level stuff that i'll learn later
import asyncio

async def main():
    await asyncio.sleep(1)
    print('hello')

asyncio.run(main())