import requests

def download_sitemap(url, filename):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Write the content of the response to a file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Sitemap downloaded successfully and saved as {filename}")
        else:
            print(f"Failed to retrieve the sitemap. HTTP Status Code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
sitemap_url = "https://app.instaffo.com/sitemap.xml"  # Replace with the URL of the sitemap
filename = "sitemap.xml"  # The local file where the sitemap will be saved

download_sitemap(sitemap_url, filename)
