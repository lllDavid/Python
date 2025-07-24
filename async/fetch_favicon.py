import aiohttp
import asyncio
from os import makedirs
from typing import Optional, Tuple, List

async def fetch_favicon(session: aiohttp.ClientSession, url: str) -> Tuple[str, Optional[bytes]]:
    try:
        async with session.get(url) as response:
            if response.status == 200 and 'image' in response.headers.get('Content-Type', ''):
                content = await response.read()
                return url, content
    except Exception as e:
        pass
    return url, None

async def fetch_favicon_from_multiple(urls: List[str]) -> List[Tuple[str, Optional[bytes]]]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_favicon(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        return results

async def main() -> None:
    urls = []

    makedirs("favicons", exist_ok=True)

    results = await fetch_favicon_from_multiple(urls)

    for i, (url, favicon) in enumerate(results):
        if favicon:
            filename = f"favicons/favicon_{i}.ico"
            with open(filename, "wb") as f:
                f.write(favicon)
            print(f"Favicon saved for {url} as {filename}")
        else:
            print(f"No favicon found at: {url}")

if __name__ == "__main__":
    asyncio.run(main())