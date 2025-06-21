import sqlite3
import os
import shutil

from manager import AtomicTransaction

def remove_file(path):
    if os.path.exists(path):
        os.remove(path)

def main():
    conn = sqlite3.connect("data.db")
    file_path = "text.txt"
    temp_path = "text.txt.bak"

    try:
        with AtomicTransaction() as txn:
            shutil.copy(file_path, temp_path)
            txn.add_rollback(lambda: shutil.move(temp_path, file_path))

            with open(file_path, 'w') as f:
                f.write("updated content")

            cursor = conn.cursor()
            cursor.execute("BEGIN")
            txn.add_rollback(conn.rollback)

            cursor.execute("UPDATE settings SET value=? WHERE key=?", ("new", "config"))
            cursor.close()
            conn.commit()

            txn.commit()
        print("Update succeeded")
    except Exception as e:
        print("Update failed:", e)

main()