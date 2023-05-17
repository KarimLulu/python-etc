import asyncio
import time


async def main():
    start = time.time()
    await asyncio.sleep(2)
    return int(time.time() - start)

asyncio.run(main())
