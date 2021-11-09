# this code taken from the python 3 docs. Just running it on my machine to get a feel for it.
# https://docs.python.org/3/library/asyncio-task.html

import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# calling main just schedules the coroutine to be run, it doesn't run it.
asyncio.run(main())