# SQL - More queries

This project focuses on advanced SQL concepts in MySQL 8.0, including user management, table constraints, subqueries, and various types of joins (INNER, LEFT). 

## Learning Objectives
- Creating and managing MySQL users and their privileges.
- Understanding and implementing constraints: `PRIMARY KEY`, `FOREIGN KEY`, `UNIQUE`, `NOT NULL`.
- Retrieving data from multiple tables using `JOIN` and `UNION`.
- Using subqueries for complex filtering.

## Files
### User Management
- `0-privileges.sql`: Lists all privileges of specific users.
- `1-create_user.sql`: Creates a user with all privileges.
- `2-create_read_user.sql`: Creates a user with read-only access to a database.

### Table Constraints & Relationships
- `3-force_name.sql`: Table with `NOT NULL` constraint.
- `4-never_empty.sql`: Table with `DEFAULT` value.
- `5-unique_id.sql`: Table with `UNIQUE` and `DEFAULT` value.
- `6-states.sql`: Table with `PRIMARY KEY` and `AUTO_INCREMENT`.
- `7-cities.sql`: Table with `FOREIGN KEY` relationship.

### Complex Queries
- `8-cities_of_california_subquery.sql`: Uses a subquery to list cities.
- `9-cities_by_state_join.sql`: Uses `JOIN` to list cities and states.
- `10-16`: Advanced queries on a TV shows database using multiple joins, grouping, and filtering.
