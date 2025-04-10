import sqlite3

# 1. Connect to the database file (or create it if it doesn't exist)
connection = sqlite3.connect('sample_database.db')
cursor = connection.cursor()

# 2. Create the employees table
create_table_query = """
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    department TEXT NOT NULL,
    salary REAL
)
"""
cursor.execute(create_table_query)
connection.commit()

# 3. Insert sample data
insert_query = "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)"
sample_data = [
    ('Alice', 'HR', 50000),
    ('Bob', 'Engineering', 80000),
    ('Charlie', 'Marketing', 60000),
    ('Eyüp', 'Engineering', 70000),
]
cursor.executemany(insert_query, sample_data)
connection.commit()

# 4. Query and display initial data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("Initial data in employees table:")
for row in rows:
    print(row)

# 5. Update and delete records
cursor.execute("UPDATE employees SET salary = ? WHERE name = ?", (85000, 'Bob'))
cursor.execute("DELETE FROM employees WHERE name = ?", ('Alice',))
connection.commit()

# 6. Query and display updated data
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
print("\nData in employees table after update and deletion:")
for row in rows:
    print(row)

# 7. Close the connection
connection.close()
