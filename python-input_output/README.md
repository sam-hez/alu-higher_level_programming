# Python - Input/Output

This project is part of the Higher Level Programming curriculum at ALU. It covers basic and advanced file handling in Python, including reading, writing, appending, and working with JSON for serialization and deserialization.

## Learning Objectives

At the end of this project, you are expected to be able to explain:
- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with` statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements

### Python Scripts
- Interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files end with a new line
- The first line of all files is exactly `#!/usr/bin/python3`
- Code uses `pycodestyle` (version 2.7.*)
- All files are executable

## Tasks

0. **Read file**: Function that reads a text file (UTF8) and prints it to stdout.
1. **Write to a file**: Function that writes a string to a text file (UTF8) and returns the number of characters written.
2. **Append to a file**: Function that appends a string at the end of a text file (UTF8) and returns the number of characters added.
3. **To JSON string**: Function that returns the JSON representation of an object (string).
4. **From JSON string to Object**: Function that returns an object (Python data structure) represented by a JSON string.
5. **Save Object to a file**: Function that writes an Object to a text file, using a JSON representation.
6. **Create object from a JSON file**: Function that creates an Object from a “JSON file”.
7. **Load, add, save**: Script that adds all arguments to a Python list, and then saves them to a file.
8. **Class to JSON**: Function that returns the dictionary description with simple data structure for JSON serialization of an object.
9. **Student to JSON**: `Student` class that defines a student and has a `to_json` method.
10. **Student to JSON with filter**: `Student` class with filtered `to_json` method.
11. **Student to disk and reload**: `Student` class with `reload_from_json` method.
12. **Pascal's Triangle**: Function that returns a list of lists of integers representing the Pascal’s triangle.
