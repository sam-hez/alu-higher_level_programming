# Python - Inheritance

This project covers the fundamental concepts of inheritance in Python, including how to define subclasses, override methods, and use built-in functions like `isinstance`, `issubclass`, `type`, and `super`.

## Learning Objectives
- Understanding superclasses, base classes, and subclasses.
- Listing all attributes and methods of a class or instance.
- Inheriting from multiple base classes.
- Method overriding and the `super` function.
- Validation logic in inherited classes.

## Files
### Object Inspection
- `0-lookup.py`: Returns a list of available attributes and methods of an object.
- `1-my_list.py`: A class `MyList` that inherits from `list` with a `print_sorted` method.
- `tests/1-my_list.txt`: Doctest for `MyList`.

### Type and Class Checks
- `2-is_same_class.py`: Checks if an object is exactly an instance of a class.
- `3-is_kind_of_class.py`: Checks if an object is an instance or inherited from a class.
- `4-inherits_from.py`: Checks if an object is an instance of a class that inherited from another.

### Geometry Hierarchy
- `5-base_geometry.py`: Empty class `BaseGeometry`.
- `6-base_geometry.py`: `BaseGeometry` with `area()` method.
- `7-base_geometry.py`: `BaseGeometry` with `integer_validator()` method.
- `tests/7-base_geometry.txt`: Doctest for `integer_validator`.
- `8-rectangle.py`: `Rectangle` class inheriting from `BaseGeometry`.
- `9-rectangle.py`: `Rectangle` class with `area()` and `__str__`.
- `10-square.py`: `Square` class inheriting from `Rectangle`.
- `11-square.py`: `Square` class with specific `__str__`.
