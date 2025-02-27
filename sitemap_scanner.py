import requests
from bs4 import BeautifulSoup
import urllib.parse
import time

def get_all_links(url):
    internal_links = set()
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    for a_tag in soup.find_all('a', href=True):
        link = a_tag['href']
        if link.startswith('/') or link.startswith(url):
            full_url = urllib.parse.urljoin(url, link)
            internal_links.add(full_url)
    
    return internal_links

def create_sitemap(url):
    visited = set()
    sitemap = set()

    def crawl(current_url):
        if current_url in visited:
            return
        visited.add(current_url)
        print(f"Crawling: {current_url}")
        links = get_all_links(current_url)
        sitemap.add(current_url)
        for link in links:
            time.sleep(1)
            crawl(link)

    crawl(url)

    with open('sitemap.xml', 'w') as file:
        file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        file.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in sitemap:
            file.write(f'  <url>\n')
            file.write(f'    <loc>{url}</loc>\n')
            file.write(f'  </url>\n')
        file.write('</urlset>\n')

website_url = 'https://example.com'
create_sitemap(website_url)
