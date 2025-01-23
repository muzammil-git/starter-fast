**README.md**
================

**Project Overview**
-------------------

This is a FastAPI application that creates a table in a database using SQLAlchemy. The application has two endpoints: one to create a table and another to display a hello message.

**Requirements**
---------------

* Python 3.11.8
* Poetry

**Installation**
---------------

To install the required dependencies, run the following command:

```bash
poetry install
```

**Running the Application**
---------------------------

To run the application, execute the following command:

```bash
python main.py
```

This will start the application on `http://127.0.0.1:5000`.

**Endpoints**
------------

### 1. Create Table

* **URL:** `/create-table`
* **Method:** `GET`
* **Description:** Creates a table named `users` in the database if it does not exist.
* **Response:** A JSON object with a success message or an error message if the table creation fails.

### 2. Root

* **URL:** `/`
* **Method:** `GET`
* **Description:** Displays a hello message.
* **Response:** A JSON object with a hello message.

**Database Configuration**
-------------------------

The application uses a database connection defined in the `database.py` file. You need to configure the database connection settings in this file to connect to your database.

