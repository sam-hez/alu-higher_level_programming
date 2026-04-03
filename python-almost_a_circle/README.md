# Python - Almost a circle

This project is a comprehensive review of Python's Higher Level Programming concepts, specifically focused on Object-Oriented Programming (OOP). It serves as a foundation for more complex projects by covering classes, inheritance, private attributes, serialization, and unittesting.

## Learning Objectives

At the end of this project, you should be able to explain:
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

## Requirements

### Python Scripts
- Ubuntu 20.04 LTS using `python3` (v3.8.5)
- All files end with a newline and are executable
- PEP 8 (pycodestyle 2.7.*)
- All modules, classes, and functions are documented

### Unit Tests
- Tests are inside a `tests/` folder
- Uses the `unittest` module
- Files and folders start with `test_`
- Command to run all tests: `python3 -m unittest discover tests`

## Tasks

### Core Classes
- **Base**: Manages IDs and provides static/class methods for JSON serialization and instance creation.
- **Rectangle**: Inherits from `Base`, implements private attributes with validation, area calculation, and display methods.
- **Square**: Inherits from `Rectangle`, manages size as a single property for both width and height.

### Serialization & Deserialization
- **to_json_string**: Converts a list of dictionaries to a JSON string.
- **save_to_file**: Writes the JSON string representation of objects to a file.
- **from_json_string**: Converts a JSON string to a list of dictionaries.
- **create**: Returns an instance with attributes already set from a dictionary.
- **load_from_file**: Returns a list of instances from a JSON file.
