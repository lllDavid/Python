import sqlite3
import csv

def export_query_to_csv(db_path, sql_query, output_csv):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(sql_query)
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        writer.writerows(rows)

    cursor.close()
    conn.close()

export_query_to_csv('example.db', 'SELECT * FROM users', 'data.csv')