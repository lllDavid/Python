import requests

BASE_URL = 'http://127.0.0.1:5000'

def create_resource(data):
    url = f'{BASE_URL}/posts'
    response = requests.post(url, json=data)
    if response.status_code == 201:
        print(f"Resource created: {response.json()}")
    else:
        print(f"Failed to create resource: {response.status_code}")

def read_resource(resource_id):
    url = f'{BASE_URL}/posts/{resource_id}'
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Resource retrieved: {response.json()}")
    else:
        print(f"Failed to retrieve resource: {response.status_code}")

def update_resource(resource_id, updated_data):
    url = f'{BASE_URL}/posts/{resource_id}'
    response = requests.put(url, json=updated_data)
    if response.status_code == 200:
        print(f"Resource updated: {response.json()}")
    else:
        print(f"Failed to update resource: {response.status_code}")

def delete_resource(resource_id):
    url = f'{BASE_URL}/posts/{resource_id}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(f"Resource with ID {resource_id} deleted successfully.")
    else:
        print(f"Failed to delete resource: {response.status_code}")

if __name__ == '__main__':
    new_post_data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    create_resource(new_post_data)

    read_resource(1)

    updated_post_data = {
        'title': 'updated title',
        'body': 'updated body',
        'userId': 1
    }
    update_resource(1, updated_post_data)

    delete_resource(1)
