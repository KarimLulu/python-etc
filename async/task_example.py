import asyncio


async def my_coroutine():
    await asyncio.sleep(0)
    return "Hello, Future!"


async def main():
    future = asyncio.create_task(my_coroutine())
    future.add_done_callback(callback)
    await asyncio.gather(future)

# Add a callback to the future


def callback(fut):
    print("Callback:", fut.result())


asyncio.run(main())
