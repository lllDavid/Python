import json
import pytest

from api import app, posts

def initial_posts():
    return [
        {'id': 1, 'title': 'First Post', 'body': 'This is the first post.'},
        {'id': 2, 'title': 'Second Post', 'body': 'This is the second post.'},
        {'id': 3, 'title': 'Third Post', 'body': 'This is the third post.'},
        {'id': 4, 'title': 'Fourth Post', 'body': 'This is the fourth post.'},
        {'id': 5, 'title': 'Fifth Post', 'body': 'This is the fifth post.'}
    ]

@pytest.fixture(autouse=True)
def reset_posts():
    posts.clear()
    posts.extend(initial_posts())
    yield

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_posts(client):
    response = client.get('/posts')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 5

def test_get_post_success(client):
    response = client.get('/posts/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert data['title'] == 'First Post'

def test_get_post_not_found(client):
    response = client.get('/posts/999')
    assert response.status_code == 404
    data = response.get_json()
    assert data['message'] == 'Post not found'

def test_create_post(client):
    new_post = {'title': 'New Post', 'body': 'New body'}
    response = client.post('/posts', data=json.dumps(new_post), content_type='application/json')
    assert response.status_code == 201
    data = response.get_json()
    assert data['id'] == 6
    assert data['title'] == 'New Post'
    assert len(posts) == 6

def test_update_post_success(client):
    update_data = {'title': 'Updated Title'}
    response = client.put('/posts/1', data=json.dumps(update_data), content_type='application/json')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 1
    assert data['title'] == 'Updated Title'

def test_update_post_not_found(client):
    update_data = {'title': 'No Title'}
    response = client.put('/posts/999', data=json.dumps(update_data), content_type='application/json')
    assert response.status_code == 404
    data = response.get_json()
    assert data['message'] == 'Post not found'

def test_delete_post(client):
    response = client.delete('/posts/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Post with ID 1 deleted'
    assert all(post['id'] != 1 for post in posts)

def test_delete_post_nonexistent(client):
    response = client.delete('/posts/999')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Post with ID 999 deleted'
    assert len(posts) == 5
