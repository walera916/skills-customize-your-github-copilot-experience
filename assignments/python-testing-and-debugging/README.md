# 📘 Assignment: Python Testing and Debugging

## 🎯 Objective

Learn how to write unit tests and use debugging techniques to verify and fix Python code.

## 📝 Tasks

### 🛠️ Write Unit Tests for Functions

#### Description

Use Python's built-in `unittest` module to create test cases for a set of functions.

#### Requirements
Completed program should:

- Define a `TestMathFunctions` test class that inherits from `unittest.TestCase`
- Include tests for `add_numbers()`, `is_even()`, and `format_greeting()` functions
- Use `assertEqual()`, `assertTrue()`, and `assertFalse()` in your test methods
- Run tests with `python -m unittest starter-code.py`
- Ensure all tests pass successfully

### 🛠️ Debug a Broken Function

#### Description

Fix the implementation of a function that contains a logic error and verify the fix with tests.

#### Requirements
Completed program should:

- Identify the bug in `calculate_discount()`
- Correct the logic so it returns the proper discounted price
- Add at least one unit test covering the fixed behavior
- Include a short comment describing the bug and how you fixed it
