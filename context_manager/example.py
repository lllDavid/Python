from sqlite3 import connect

# Mock Database workflow with __enter__ and __exit__
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        print(f"Connecting to database: {self.db_name}")
        self.conn = connect(self.db_name)
        self.cursor = self.conn.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users
                               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
        self.conn.commit()

        return self.cursor  

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            print("Committing transaction")
            self.conn.commit()
        else:
            print(f"Rolling back transaction due to {exc_type.__name__}: {exc_value}")
            self.conn.rollback()

        self.conn.close()
        print("Connection closed.")

with DatabaseConnection(':memory:') as cursor:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Bob", 25))
    print("Data inserted successfully.")

with DatabaseConnection(':memory:') as cursor:
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Charlie", 35))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("David", "wrong_age"))
    print("Data inserted successfully.")
