import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results

async def main():
    urls = ["https://example.com", "https://example.org", "https://example.net"]
    responses = await fetch_all(urls)
    for response in responses:
        print(response[:100])

asyncio.run(main())