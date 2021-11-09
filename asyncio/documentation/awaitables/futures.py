# futures represent the eventual result of an async operation

# when a future is awaited it means the coroutine will wait until the future is resolved elsewhere
# ^ but what does that mean?
# necessary for callback-based code ot be used w/ async/await
# at app level no need for it

# example
async def main():
    await funciton_that_returns_a_future_object()

    #this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )

# this one is definitely a little opaque to me at this point.
# I think what they're saying is that when you actually await something it creates a future
# object which is held until the result of the task or coroutine is obtained.
# maybe future examples or more low-level api will provide clarity