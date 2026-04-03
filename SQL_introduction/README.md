# SQL - Introduction

This project introduces basic SQL concepts using MySQL 8.0. It covers database management (creating, listing, deleting) and data manipulation (CRUD operations, aggregation, and filtering).

## Learning Objectives
- Understanding relational databases and SQL.
- Difference between DDL (Data Definition Language) and DML (Data Manipulation Language).
- Creating and managing databases and tables.
- Querying data with filters, sorting, and aggregation functions.
- Performing basic data modification (INSERT, UPDATE, DELETE).

## Files
### Database Management
- `0-list_databases.sql`: Lists all databases.
- `1-create_database_if_missing.sql`: Creates `hbtn_0c_0` if not exists.
- `2-remove_database.sql`: Deletes `hbtn_0c_0` if exists.
- `3-list_tables.sql`: Lists tables in a database.

### Table Operations
- `4-first_table.sql`: Creates `first_table`.
- `5-full_table.sql`: Prints full description of `first_table`.
- `6-list_values.sql`: Lists all rows of `first_table`.
- `7-insert_value.sql`: Inserts a new row into `first_table`.
- `8-count_89.sql`: Counts records with `id = 89`.

### Data Manipulation & Aggregation
- `9-full_creation.sql`: Creates `second_table` and inserts multiple rows.
- `10-top_score.sql`: Lists records by score (top first).
- `11-best_score.sql`: Filter records with score >= 10.
- `12-no_cheating.sql`: Updates Bob's score to 10.
- `13-change_class.sql`: Removes records with score <= 5.
- `14-average.sql`: Computes score average.
- `15-groups.sql`: Lists number of records with the same score.
- `16-no_link.sql`: Lists records with names, sorted by score.
