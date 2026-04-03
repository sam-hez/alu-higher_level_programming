# Python - Object-relational mapping

This project integrates Python with MySQL databases using two distinct approaches: direct SQL queries with `MySQLdb` and Object-Relational Mapping (ORM) with `SQLAlchemy`.

## Learning Objectives

At the end of this project, you should be able to explain:
- How to connect to a MySQL database from a Python script
- How to SELECT and INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
- How to use SQLAlchemy to interact with a database without writing SQL

## Requirements

### General
- Ubuntu 20.04 LTS using `python3` (v3.8.5)
- `MySQLdb` version 2.0.x
- `SQLAlchemy` version 1.4.x
- PEP 8 (pycodestyle 2.7.*)
- All files end with a newline and are executable
- All modules, classes, and functions are documented

## Tasks

### Part 1: MySQLdb (Direct SQL)
- **0-select_states.py**: List all states from `hbtn_0e_0_usa`.
- **1-filter_states.py**: List states starting with 'N'.
- **2-my_filter_states.py**: Filter states by user input (formatted).
- **3-my_safe_filter_states.py**: Filter states by user input (safe from SQL injection).
- **4-cities_by_state.py**: List all cities with their state names.
- **5-filter_cities.py**: List cities of a specific state.

### Part 2: SQLAlchemy (ORM)
- **model_state.py**: Definition of the `State` class.
- **7-model_state_fetch_all.py**: List all `State` objects.
- **8-model_state_fetch_first.py**: Fetch the first `State` object.
- **9-model_state_filter_a.py**: Filter states containing the letter 'a'.
- **10-model_state_my_get.py**: Fetch a state by its name.
- **11-model_state_insert.py**: Insert a new `State` object.
- **12-model_state_update_id_2.py**: Update a `State` object's name.
- **13-model_state_delete_a.py**: Delete states containing the letter 'a'.

### Part 3: Relationships
- **model_city.py**: Definition of the `City` class with a foreign key to `states`.
- **14-model_city_fetch_by_state.py**: Fetch all cities grouped by their state.
