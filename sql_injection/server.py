from flask import Flask, request, g
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
                role TEXT
            )
        ''')
        users = [
            ('alice', 'alice@example.com', 'user'),
            ('bob', 'bob@example.com', 'user'),
            ('charlie', 'charlie@example.com', 'user'),
        ]
        cursor.executemany("INSERT INTO users (username, email, role) VALUES (?, ?, ?)", users)
        db.commit()

@app.route('/students')
def students():
    user_id = request.args.get('id', '')
    db = get_db()
    cursor = db.cursor()

    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    print(f"[DEBUG] Executing query: {query}")
    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            return f"User found: ID={result['id']}, Name={result['username']}, Email={result['email']}, Role={result['role']}"
        else:
            return "No user found"
    except Exception as e:
        return f"SQL error: {e}"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
