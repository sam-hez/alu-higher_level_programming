# Python - Test-driven development

This project focuses on the importance of testing in Python development. It covers `doctest` for interactive documentation-based tests and `unittest` for more comprehensive unit testing.

## Learning Objectives

At the end of this project, you should be able to explain:
- Why tests are important
- How to write Docstrings to create tests
- How to find edge cases
- The basic option flags to create tests
- What an interactive test is

## Requirements

### Python Scripts
- Ubuntu 20.04 LTS using `python3` (v3.8.5)
- All files end with a newline and are executable
- PEP 8 (pycodestyle 2.7.*)
- Modules and functions must have descriptive documentation

### Test Cases
- Tests are inside a `tests/` folder
- `doctest` files are `.txt`
- `unittest` files are `.py`
- Command for doctests: `python3 -m doctest ./tests/*`
- Command for unittests: `python3 -m unittest tests.6-max_integer_test`

## Tasks

0. **Integers addition**: `add_integer(a, b=98)` with validation and float casting.
1. **Divide a matrix**: `matrix_divided(matrix, div)` with validation and rounding.
2. **Say my name**: `say_my_name(first_name, last_name="")` with type checking.
3. **Print square**: `print_square(size)` with validation and `#` printing.
4. **Text indentation**: `text_indentation(text)` with specific punctuation handling.
5. **Max integer - Unittest**: Unit tests for `max_integer(list=[])`.
