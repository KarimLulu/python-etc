import asyncio


URLS = ['google.com', 'github.com', 't.me']


async def check_alive(url):
    print(f'started {url}')
    i = URLS.index(url)
    await asyncio.sleep(3 - i)
    print(f'finished {url}')
    return i


async def main():
    coros = [check_alive(url) for url in URLS]
    statuses = await asyncio.gather(*coros)
    for url, alive in zip(URLS, statuses):
        print(url, alive)

asyncio.run(main())
