import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

def get_posts(user_id=None):
    params = {"userId": user_id} if user_id else {}
    try:
        response = requests.get(f"{BASE_URL}/posts", headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching posts:", e)
        return []

def create_post(title, body, user_id):
    payload = {
        "title": title,
        "body": body,
        "userId": user_id
    }
    try:
        response = requests.post(f"{BASE_URL}/posts", headers=HEADERS, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Error creating post:", e)
        return None

if __name__ == "__main__":
    print("Fetching posts by user ID 1...")
    posts = get_posts(user_id=1)
    for post in posts[:3]:  
        print(f"{post['id']}: {post['title']}")

    print("\nCreating a new post...")
    new_post = create_post("Hello", "This is a test post", user_id=1)
    print("Response:", new_post)
