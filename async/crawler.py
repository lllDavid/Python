import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetch_page(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                print(f"Fetched {url}")
                return await response.text()
            else:
                print(f"Failed to fetch {url}: {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

async def parse_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    links = []
    for link in soup.find_all('a', href=True):
        links.append(link['href'])
    return links

async def crawl(session, url, visited, depth=0):
    if depth > 2 or url in visited:
        return
    visited.add(url)
    print(f"Crawling {url} at depth {depth}...")
    html = await fetch_page(session, url)
    if html:
        links = await parse_links(html)
        for link in links:
            if link.startswith('http'):
                await crawl(session, link, visited, depth + 1)

async def main():
    start_url = 'https://example.com'
    visited = set()
    async with aiohttp.ClientSession() as session:
        await crawl(session, start_url, visited)
    print("\nCrawling finished.")

asyncio.run(main())
