from flask import Flask, jsonify, request, g
import sqlite3

app = Flask(__name__)
DATABASE = 'test.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('DROP TABLE IF EXISTS users')
        cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                email TEXT,
                password_hash TEXT,
                role TEXT
            )
        ''')
        users = [
            ('alice', 'alice@example.com', 'pbkdf2:sha256:600000$eV5vUqTWXGBDE9Ac$dc5127c8b84e6debc7cfe1450a3141d7768d10f63f0f92c49ebbc38c2adac943', 'user'),
            ('bob', 'bob@example.com', 'pbkdf2:sha256:600000$aZpL7NDyBQ7bshJL$8180a382c68a7613c4568e11304c2096d3c4e2c69736c0fa4b0de73597a35803', 'user'),
            ('charlie', 'charlie@example.com', 'pbkdf2:sha256:600000$ZqOYDKs0a0zD8DRT$0ffdd85894dc930c92066011b427fc1898c3346d3a4b0ae35588f64e1dbe284c', 'user'),
        ]
        cursor.executemany("INSERT INTO users (username, email, password_hash, role) VALUES (?, ?, ?, ?)", users)
        db.commit()

# Intentionally vulnerable
@app.route('/students')
def students():
    user_id = request.args.get('id', '')
    db = get_db()
    cursor = db.cursor()

    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return f"User found: ID={result['id']}, Name={result['username']}, Email={result['email']}, Password={result['password_hash']}, Role={result['role']}"
        else:
            return "No user found"
    except Exception as e:
        return f"SQL error: {e}"
    
# Parameterized
@app.route('/students2', methods=['GET'])
def students2():
    user_id = request.args.get('id')
    if not user_id or not user_id.isdigit():
        return jsonify({"error": "Invalid user ID"}), 400

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT id, username, email, role FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if user:
            return jsonify(dict(user)), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": "Database error"}), 500
    
# Intentionally vulnerable
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    db = get_db()
    cursor = db.cursor()
    
    query = f"SELECT * FROM users WHERE username = '{username}' AND password_hash = '{password}'"
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return f"Login success! Welcome, {user['username']}."
        else:
            return "Invalid username or password."
    except Exception as e:
        return f"SQL error: {e}"

# Parameterized
@app.route('/login_safe', methods=['POST'])
def login_safe():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute(
            "SELECT username FROM users WHERE username = ? AND password_hash = ?",
            (username, password)
        )
        user = cursor.fetchone()
        if user:
            return jsonify({"message": f"Login success! Welcome, {user['username']}."}), 200
        else:
            return jsonify({"error": "Invalid username or password."}), 401
    except Exception:
        return jsonify({"error": "Database error"}), 500


if __name__ == '__main__':
    init_db()
    app.run(debug=True)