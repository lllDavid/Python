from flask import Flask, jsonify, request

app = Flask(__name__)

posts = [
    {'id': 1, 'title': 'First Post', 'body': 'This is the first post.'},
    {'id': 2, 'title': 'Second Post', 'body': 'This is the second post.'},
    {'id': 3, 'title': 'Third Post', 'body': 'This is the third post.'},
    {'id': 4, 'title': 'Fourth Post', 'body': 'This is the fourth post.'},
    {'id': 5, 'title': 'Fifth Post', 'body': 'This is the fifth post.'}
]

@app.route('/posts', methods=['POST'])
def create_post():
    new_post = request.get_json()
    new_post['id'] = len(posts) + 1  
    posts.append(new_post)
    return jsonify(new_post), 201

@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts), 200

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return jsonify({'message': 'Post not found'}), 404
    return jsonify(post), 200

@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post is None:
        return jsonify({'message': 'Post not found'}), 404
    updated_data = request.get_json()
    post.update(updated_data)
    return jsonify(post), 200

@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    posts[:] = [post for post in posts if post['id'] != post_id]
    return jsonify({'message': f'Post with ID {post_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
