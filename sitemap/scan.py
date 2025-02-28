import requests
from urllib.parse import urlparse

def check_sitemap(url):
    # Get the base domain of the URL
    parsed_url = urlparse(url)
    base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

    # List of common sitemap locations
    possible_sitemaps = [
        f"{base_url}/sitemap.xml",
        f"{base_url}/sitemap_index.xml",
        f"{base_url}/sitemap1.xml",
        f"{base_url}/robots.txt"
    ]

    # Check each possible location for a sitemap
    for sitemap_url in possible_sitemaps:
        try:
            response = requests.get(sitemap_url, timeout=10)

            # Check if the response is valid (status code 200)
            if response.status_code == 200:
                print(f"Sitemap found at: {sitemap_url}")
                if sitemap_url.endswith('robots.txt'):
                    # Check if a sitemap is declared inside robots.txt
                    if 'Sitemap:' in response.text:
                        print("Sitemap found in robots.txt")
                else:
                    # It's an XML sitemap, you can parse it here if needed
                    print(f"Sitemap XML content:\n{response.text[:200]}...")  # Display first 200 chars
                return
            else:
                print(f"No sitemap found at: {sitemap_url}")

        except requests.RequestException as e:
            print(f"Error while checking {sitemap_url}: {e}")

    print("No sitemap found on the website.")

# Test the function with a URL
url_to_check = ""
check_sitemap(url_to_check)
