import asyncio

# Types of awaitables:
## coroutines
## Tasks
## Futures

async def nested():
    return 42

async def main():
    # Nothing happens if we just call "nested()".
    # A coroutine object is created but not awaited,
    # so it *won't run at all*.
    nested() # also causes a runtime warning

    # Let's do it differently now and await it:
    print(await nested()) # Will print "42".

asyncio.run(main())

# documentation says that coroutine can refer to:
## a coroutine function - async def function
## a coroutine object - an object returned by calling a coroutine function
