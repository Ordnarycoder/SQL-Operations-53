# SQLite Database Operations with Python

This project demonstrates basic SQLite database operations using Python, including creating a database, performing CRUD (Create, Read, Update, Delete) operations, and handling data effectively.

## Project Overview

The Python script in this project performs the following database operations:

- **Connecting** to an SQLite database (creates a new database if it doesn't exist).
- **Creating** a table (`employees`) with fields for ID, name, department, and salary.
- **Inserting** sample data into the database.
- **Querying** data to display contents of the database.
- **Updating** specific records.
- **Deleting** records from the database.

## Project Structure

```
project-folder/
├── database_operations.py
├── sample_database.db (generated after running the script)
└── README.md
```

## Requirements

No additional libraries are required. Python's built-in `sqlite3` library is sufficient.

## How to Run the Project

1. Clone or download the project.
2. Navigate to the project directory:

```bash
cd project-folder
```

3. Run the Python script:

```bash
python sql_operations.py
```

The script will display the initial data in the table and the updated data after performing update and delete operations.

## Sample Output

```
Initial data in employees table:
(1, 'Alice', 'HR', 50000.0)
(2, 'Bob', 'Engineering', 80000.0)
(3, 'Charlie', 'Marketing', 60000.0)
(4, 'Eyüp', 'Engineering', 70000.0)

Data in employees table after update and deletion:
(2, 'Bob', 'Engineering', 85000.0)
(3, 'Charlie', 'Marketing', 60000.0)
(4, 'Eyüp', 'Engineering', 70000.0)
```

## License

This project is open source and available under the [MIT License](LICENSE).

