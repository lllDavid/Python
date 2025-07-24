import aiohttp
import asyncio

class URLFetcher:
    def __init__(self, urls, session):
        self.urls = urls
        self.session = session
        self._index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index >= len(self.urls):
            raise StopAsyncIteration

        url = self.urls[self._index]
        self._index += 1

        async with self.session.get(url) as resp:
            text = await resp.text()
            return f"{url} → {len(text)} chars"

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]

    async with aiohttp.ClientSession() as session:
        async for result in URLFetcher(urls, session):
            print(result)

asyncio.run(main())