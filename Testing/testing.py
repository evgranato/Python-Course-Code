# ***TESTING***
# *OBJECTIVES*
# - Describe what tests are and why they are essential
# - Explain what Test Driven Development is
# - Test Python code using doctests
# - Test Python code using assert
# - Explain what unit testing is
# - Write unit tests using the unittest module
# - Remove code duplication using before and after hooks

# **WHY TEST?**
# THIS IS ESSENTIAL IF YOU ARE AT A LARGE COMPANY
# - Reduce bugs in existing code
# - Ensure bugs that are fixed stay fixed
# - Ensure that new features don't break old ones
# - Ensure that cleaning up code doesn't introduce new bugs
# - Makes development more fun!

# *TEST DRIVEN DEVELOPMENT*
# - Development begins by writing tests
# - Once tests are written, write code to make tests pass
# - Once tests pass, a feature is considered complete

# *RED, GREEN, REFACTOR*
# 1. Red - Write a test that fails
# 2. Green - Write the minimal amount of code necessary to make the test pass
# 3. Refactor - Clean up the code, while ensuring that tests still pass

# **ASSERTIONS**
# - We can make simple assertions with the assert keyword
# - assert accepts an expression
# - Returns None if the expression is truthy
# - Raises an AssertionError if the expression is falsy
# - Accepts an optional error message as a second argument

# def add_positive_numbers(x,y):
#     assert x > 0 and y > 0, "Both numbers must be positive!"
#     return x + y
# print(add_positive_numbers(1,1)) #2
# add_positive_numbers(1, -1) # AssertionError: Both numbers must be positive!
# ASSERT IS LIKE: IF NOT SOME_EXPRESSION: RAISE ASSERTIONERROR()

# def eat_junk(food):
#     assert food in [
#         "pizza", "ice cream", "candy", "fried butter"
#     ], "food must be a junk food!"
#     return f"NOM NOM NOM I am eating {food}"
# food = input("ENTER A FOOD PLEASE: ")
# print(eat_junk(food))

# *ASSERTIONS WARNING*
# - If a Python file is run with the -O flag, assertions will not be evaluated!
# python3 -O testing.py
# -O let any food pass as a junk food because assert was not run

# *doctests*
# - We can write tests for functions inside of the docstring
# - Write code that looks like it's inside of a REPL
# - EXAMPLE:
# def add(x,y):
#     """add together x and y
#
#     >>> add(1,2)
#     3
#     >>> add(8, "hi")
#     Traceback (most recent call list):
#         ...
#     TypeError: unsupported operand type(s) for +: 'int' and 'str
#     """

# def add(a, b):
#     """
#     >>> add(2,3)
#     5
#     >>> add(100, 200)
#     300
#     """
#     return a + b
# # RUN THIS LINE IN TERMINAL: python3 -m doctest -v testing.py

# def double(values):
#     """ double the values in a list
#
#     >>> double([1,2,3,4])
#     [2, 4, 6, 8]
#
#     >>> double([])
#     []
#
#     >>> double(['a', 'b', 'c'])
#     ['aa', 'bb', 'cc']
#
#     >>> double([True, None])
#     Traceback (most recent call last):
#         ...
#     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * element for element in values] # this fixed the problems in the code

# def say_hi():
#     """
#     >>> say_hi()
#     "hi"
#     """
#     return "hi"
# FAILED BECAUSE "" NOT ''. IT WANTS ''

# def true_that():
#     """
#     >>> true_that()
#     True
#     """
#     return True

# def make_dict(keys):
#     """
#     >>> make_dict(['a','b'])
#     {'a':True, 'b':True}
#     """
#     return {key: True for key in keys}

# *ISSUES WITH DOCTESTS*
# - Syntax is a little strange
# - Clutters up our function code
# - Lacks many features of larger testing tools
# - Tests are finicky

# *INTRODUCTION TO unittest*
# UNIT TESTING:
# - Test smallest parts of an application in isolation(e.g. units)
# - Good candidates for unit testing: individual classes, modules or functions
# - Bad candidates for unit testing: an entire application, dependencies across several classes or modules
# unittest
# - good documentation online with the module
# - Python comes with a built-in module called unittest
# - You can write unit tests encapsulated as classes that inherit from unittest.TestCase
# - This inheritance gives you access to many assertion helpers that let you test the behavior of your functions
# - You can run tests by calling unittest.main()

# *EXAMPLE*
# IN ACTIVITIES.PY
# def eat(food, is_healthy):
#     pass
# def nam(num_hours):
#     pass
# # IN TESTS.PY
# import unittest
# from activities import eat, nap
#
# class ActivityTests(unittest.TestCase)
#     pass
# if __name__ == "__main__":
#     unittest.main()

# *COMMENTING TESTS*
# comment with """ in there
# TO SEE COMMENTS, RUN python3 name_of_file.py -v

# **TYPES OF ASSERTIONS**
# - self.assertEqual(x,y)
# - self.assertNotEqual(x,y)
# - self.assertTrue(x)
# - self.assertFalse(x)
# - self.assertIsNotNone(x)
# - self.assertIn(x,y)
# - self.assertNotIn(x,y)
# - ...and more!

# *TESTING FOR ERRORS*
# import unittest
# class SomeTests(unittest.TestCase):
#     def testing_for_error(self):
#         """testing for an error"""
#         with self.assertRaises(IndexError):
#             l = [1,2,3]
#             l[100]

# *BEFORE AND AFTER HOOKS**
# setUp and tearDown:
# - For larger applications, you may want similar application state before running tests
# - setUp runs after each test method
# - tearDown runs after each test method
# - Common use cases: adding/removing data from a test database, creating instances of a class.
# EXAMPLE:
# class SomeTests(unittest,TestCase):
#
#     def setUp(self):
#         # do setup here
#         pass
#     def test_first(self):
#         # setUp runs before
#         # tearDown runs after
#         pass
#     def test_second(self):
#         # setUp runs before
#         # tearDown runs after
#         pass
#     def tearDown(self):
#         # do teardown here
#         pass

# class Robot:
#     def __init__(self, name, battery=100, skills=[]):
#         self.name = name
#         self.battery = battery
#         self.skills = skills
#
#     def charge(self):
#         self.battery = 100
#         return self
#
#     def say_name(self):
#         if self.battery > 0:
#             self.battery -= 1
#             return f"BEEP BOOP BEEP BOOP. I AM {self.name.upper()}"
#         return "Low power. Please charge and try again"
#
#     def learn_skill(self, new_skill, cost_to_learn):
#         if self.battery  >= cost_to_learn:
#             self.battery -= cost_to_learn
#             self.skills.append(new_skill)
#             return f"WOAH. I KNOW {new_skill.upper()}"
#         return "Insufficient battery. Please charge and try again"