# Complete Python Tutorial for Beginners

## Table of Contents
1. [Python Syntax](#python-syntax)
2. [Python Comments](#python-comments)
3. [Python Variables](#python-variables)
4. [Python Data Types](#python-data-types)
5. [Python Numbers](#python-numbers)
6. [Python Casting](#python-casting)
7. [Python Strings](#python-strings)
   - [Slicing Strings](#slicing-strings)
   - [Modify Strings](#modify-strings)
   - [Concatenate Strings](#concatenate-strings)
   - [Format Strings](#format-strings)
   - [Escape Characters](#escape-characters)
   - [String Methods](#string-methods)
   - [String Exercises](#string-exercises)
8. [Python Booleans](#python-booleans)
9. [Python Operators](#python-operators)

---

## Python Syntax

Python syntax refers to the set of rules that defines how Python programs are written and interpreted. Think of syntax as the "grammar" of programming - just like English has rules for sentence structure, Python has rules for code structure.

### Key Characteristics of Python Syntax:

**1. Indentation (Most Important!)**
Unlike other programming languages that use curly braces `{}`, Python uses indentation (spaces or tabs) to define code blocks.

```python
# Correct indentation
if 5 > 2:
    print("Five is greater than two!")
    
# Wrong indentation (will cause an error)
if 5 > 2:
print("This will cause an IndentationError!")
```

**2. Case Sensitivity**
Python distinguishes between uppercase and lowercase letters.

```python
name = "John"
Name = "Jane"
NAME = "Bob"
# These are three different variables!
```

**3. No Semicolons Required**
Unlike languages like JavaScript or C++, Python doesn't require semicolons at the end of statements.

```python
print("Hello World")  # Correct
print("Hello World"); # Also works, but not necessary
```

**4. Comments Use #**
```python
# This is a comment
print("Hello World")  # This is also a comment
```

### Your First Python Program:

```python
print("Hello, World!")
```

This simple line does the following:
- `print()` is a built-in function that displays output
- The parentheses `()` contain what we want to print
- The quotes `""` indicate that we're printing text (a string)

---

## Python Comments

Comments are lines in your code that Python ignores when running the program. They're like notes you leave for yourself and other programmers to explain what the code does.

### Why Use Comments?
1. **Explain complex logic**: Help others understand your thinking
2. **Document functions**: Describe what a piece of code does
3. **Temporary disable code**: Turn off code without deleting it
4. **Leave reminders**: Note things to fix or improve later

### Types of Comments:

**1. Single-line Comments**
Use `#` to create a comment that lasts until the end of the line.

```python
# This is a single-line comment
print("Hello World")  # This comment explains this line

# You can use multiple single-line comments
# to create a multi-line explanation
# like this paragraph
```

**2. Multi-line Comments**
Python doesn't have a dedicated multi-line comment syntax, but you can use triple quotes:

```python
"""
This is a multi-line comment.
You can write as much as you want here.
It's often used for documentation.
"""

'''
You can also use single quotes
for multi-line comments.
Both work the same way.
'''
```

**3. Docstrings (Special Comments)**
These are used to document functions, classes, and modules:

```python
def greet(name):
    """
    This function greets a person with their name.
    
    Parameters:
    name (str): The name of the person to greet
    
    Returns:
    str: A greeting message
    """
    return f"Hello, {name}!"
```

### Best Practices for Comments:

```python
# Good: Explains WHY, not just WHAT
# Calculate tax rate based on income bracket
tax_rate = 0.25 if income > 50000 else 0.15

# Bad: Just repeats what the code does
# Set tax_rate to 0.25
tax_rate = 0.25

# Good: Explains complex logic
# Use binary search because the list is already sorted
# This reduces time complexity from O(n) to O(log n)
result = binary_search(sorted_list, target)
```

---

## Python Variables

Think of variables as labeled boxes where you can store different types of information. Just like you might have a box labeled "Books" and another labeled "Toys", variables have names and hold different types of data.

### Creating Variables (Assignment)

In Python, you create a variable by simply assigning a value to it:

```python
# Creating variables
name = "Alice"        # Text (string)
age = 25             # Number (integer)
height = 5.6         # Decimal number (float)
is_student = True    # True/False (boolean)

# You can print variables
print(name)          # Output: Alice
print(age)           # Output: 25
```

### Variable Naming Rules

**Must Follow:**
1. Start with a letter (a-z, A-Z) or underscore (_)
2. Can contain letters, numbers, and underscores
3. Case-sensitive (`name` and `Name` are different)
4. Cannot use Python keywords (like `if`, `for`, `while`)

```python
# Valid variable names
first_name = "John"
age2 = 30
_private = "secret"
firstName = "John"  # CamelCase (less common in Python)

# Invalid variable names
# 2age = 30        # Cannot start with a number
# first-name = ""  # Cannot use hyphens
# if = 5           # Cannot use Python keywords
```

### Variable Naming Conventions (Best Practices)

```python
# Use snake_case (recommended in Python)
student_name = "Bob"
total_score = 95
is_logged_in = False

# Use descriptive names
# Good
user_email = "user@example.com"
monthly_salary = 5000

# Bad
x = "user@example.com"  # What does 'x' represent?
s = 5000               # What is 's'?
```

### Multiple Assignment

```python
# Assign same value to multiple variables
x = y = z = 10
print(x, y, z)  # Output: 10 10 10

# Assign different values in one line
name, age, city = "Alice", 25, "New York"
print(name)     # Output: Alice
print(age)      # Output: 25
print(city)     # Output: New York

# Swap variables easily
a = 5
b = 10
a, b = b, a  # Swap values
print(a)     # Output: 10
print(b)     # Output: 5
```

### Variables Are Dynamic

Python variables can change their type during execution:

```python
# Start with a number
my_var = 42
print(my_var, type(my_var))  # Output: 42 <class 'int'>

# Change to text
my_var = "Hello"
print(my_var, type(my_var))  # Output: Hello <class 'str'>

# Change to a list
my_var = [1, 2, 3]
print(my_var, type(my_var))  # Output: [1, 2, 3] <class 'list'>
```

### Global vs Local Variables

```python
# Global variable (accessible everywhere)
global_var = "I'm global"

def my_function():
    # Local variable (only accessible inside this function)
    local_var = "I'm local"
    print(global_var)  # Can access global variable
    print(local_var)   # Can access local variable

my_function()
print(global_var)      # Can access global variable
# print(local_var)     # This would cause an error!
```

---

## Python Data Types

Data types specify what kind of data a variable can hold. Think of them as categories - like sorting items into boxes labeled "Numbers", "Text", "True/False", etc.

### Built-in Data Types Overview

Python has several built-in data types organized into categories:

**Text Type:**
- `str` (string)

**Numeric Types:**
- `int` (integer)
- `float` (floating-point number)
- `complex` (complex number)

**Sequence Types:**
- `list`
- `tuple`
- `range`

**Mapping Type:**
- `dict` (dictionary)

**Set Types:**
- `set`
- `frozenset`

**Boolean Type:**
- `bool`

**Binary Types:**
- `bytes`
- `bytearray`
- `memoryview`

### Checking Data Types

Use the `type()` function to check what type a variable is:

```python
name = "Alice"
age = 25
height = 5.6
is_student = True
grades = [85, 90, 92]

print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(is_student)) # <class 'bool'>
print(type(grades))    # <class 'list'>
```

### Detailed Look at Each Type

**1. String (str) - Text Data**
```python
# Different ways to create strings
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a
multi-line string"""

print(type(single_quotes))  # <class 'str'>
```

**2. Integer (int) - Whole Numbers**
```python
positive = 42
negative = -17
zero = 0

print(type(positive))  # <class 'int'>

# Python can handle very large integers
big_number = 12345678901234567890
print(big_number)  # Python handles this easily!
```

**3. Float - Decimal Numbers**
```python
price = 19.99
temperature = -5.5
scientific = 2.5e-4  # Scientific notation (0.00025)

print(type(price))  # <class 'float'>
```

**4. Boolean (bool) - True or False**
```python
is_raining = True
is_sunny = False

print(type(is_raining))  # <class 'bool'>

# Booleans are actually a subtype of integers
print(int(True))   # Output: 1
print(int(False))  # Output: 0
```

**5. List - Ordered Collection**
```python
# Lists can hold multiple items of different types
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, True]
empty_list = []

print(type(fruits))  # <class 'list'>

# Lists are mutable (can be changed)
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']
```

**6. Tuple - Ordered, Unchangeable Collection**
```python
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single-item tuple

print(type(coordinates))  # <class 'tuple'>

# Tuples are immutable (cannot be changed)
# coordinates[0] = 15  # This would cause an error!
```

**7. Dictionary (dict) - Key-Value Pairs**
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(type(student))  # <class 'dict'>
print(student["name"])  # Access value by key: Alice
```

**8. Set - Unordered Collection of Unique Items**
```python
unique_numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14}

print(type(unique_numbers))  # <class 'set'>

# Sets automatically remove duplicates
numbers_with_duplicates = {1, 2, 2, 3, 3, 3}
print(numbers_with_duplicates)  # {1, 2, 3}
```

### Type Conversion Preview

You can convert between types (we'll cover this in detail in the Casting section):

```python
# String to integer
age_str = "25"
age_int = int(age_str)
print(age_int, type(age_int))  # 25 <class 'int'>

# Integer to string
number = 42
number_str = str(number)
print(number_str, type(number_str))  # 42 <class 'str'>
```

---

## Python Numbers

Numbers are fundamental in programming. Python provides three numeric types to handle different kinds of mathematical operations and precision requirements.

### Types of Numbers in Python

**1. Integers (int)** - Whole numbers
**2. Floats (float)** - Decimal numbers  
**3. Complex numbers (complex)** - Numbers with real and imaginary parts

### Integers (int)

Integers are whole numbers without decimal points. They can be positive, negative, or zero.

```python
# Basic integers
positive_int = 42
negative_int = -17
zero = 0

# Python can handle arbitrarily large integers
huge_number = 123456789012345678901234567890
print(huge_number)  # Python handles this without overflow!

# Different number systems
binary = 0b1010        # Binary (base 2) = 10 in decimal
octal = 0o12           # Octal (base 8) = 10 in decimal
hexadecimal = 0x0A     # Hexadecimal (base 16) = 10 in decimal

print(binary, octal, hexadecimal)  # All output: 10 10 10
```

### Floats (float)

Floats are numbers with decimal points. They're used for precise calculations.

```python
# Basic floats
price = 19.99
temperature = -5.5
small_number = 0.0001

# Scientific notation
large_number = 2.5e6    # 2.5 × 10^6 = 2,500,000
small_number = 3.2e-4   # 3.2 × 10^-4 = 0.00032

print(large_number)     # 2500000.0
print(small_number)     # 0.00032

# Float precision (important to understand!)
result = 0.1 + 0.2
print(result)           # 0.30000000000000004 (not exactly 0.3!)

# This happens because of how computers store decimal numbers
# For precise decimal calculations, use the decimal module
```

### Complex Numbers (complex)

Complex numbers have real and imaginary parts. They're used in advanced mathematics and engineering.

```python
# Creating complex numbers
z1 = 3 + 4j    # 3 is real part, 4j is imaginary part
z2 = complex(2, -3)  # Another way to create: 2 - 3j

print(z1)       # (3+4j)
print(z2)       # (2-3j)

# Accessing parts
print(z1.real)  # 3.0 (real part)
print(z1.imag)  # 4.0 (imaginary part)

# Complex number operations
z3 = z1 + z2
print(z3)       # (5+1j)
```

### Number Operations

**Basic Arithmetic:**
```python
a = 10
b = 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.3333333333333335
print(a // b)   # Floor division: 3 (integer division)
print(a % b)    # Modulus (remainder): 1
print(a ** b)   # Exponentiation: 1000 (10^3)
```

**Understanding Division Types:**
```python
# Regular division always returns a float
print(10 / 2)   # 5.0 (float, even though result is whole)
print(10 / 3)   # 3.3333333333333335

# Floor division returns the floor of the division
print(10 // 3)  # 3 (removes decimal part)
print(-10 // 3) # -4 (floors towards negative infinity)

# Modulus gives the remainder
print(10 % 3)   # 1 (10 = 3*3 + 1)
print(15 % 4)   # 3 (15 = 4*3 + 3)
```

### Built-in Number Functions

```python
# Absolute value
print(abs(-5))      # 5
print(abs(3.14))    # 3.14

# Rounding
print(round(3.14159))     # 3
print(round(3.14159, 2))  # 3.14 (round to 2 decimal places)

# Min and Max
print(min(5, 2, 8, 1))    # 1
print(max(5, 2, 8, 1))    # 8

# Power
print(pow(2, 3))          # 8 (same as 2**3)
print(pow(2, 3, 5))       # 3 (2^3 mod 5 = 8 mod 5 = 3)
```

### Math Module for Advanced Operations

```python
import math

# Constants
print(math.pi)      # 3.141592653589793
print(math.e)       # 2.718281828459045

# Trigonometric functions (angles in radians)
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.tan(math.pi/4))  # 1.0

# Logarithms
print(math.log(10))         # Natural logarithm: 2.302585092994046
print(math.log10(100))      # Base-10 logarithm: 2.0

# Square root
print(math.sqrt(16))        # 4.0

# Ceiling and floor
print(math.ceil(4.3))       # 5 (round up)
print(math.floor(4.7))      # 4 (round down)

# Factorial
print(math.factorial(5))    # 120 (5! = 5×4×3×2×1)
```

### Random Numbers

```python
import random

# Random float between 0 and 1
print(random.random())

# Random integer between 1 and 10 (inclusive)
print(random.randint(1, 10))

# Random choice from a list
colors = ["red", "blue", "green", "yellow"]
print(random.choice(colors))

# Random float between 1.5 and 10.5
print(random.uniform(1.5, 10.5))
```

### Type Checking and Conversion

```python
# Check if a variable is a number
x = 42
print(isinstance(x, int))     # True
print(isinstance(x, float))   # False
print(isinstance(x, (int, float)))  # True (check multiple types)

# Convert between number types
integer_num = 42
float_num = float(integer_num)    # 42.0
print(type(float_num))            # <class 'float'>

float_num = 3.14
integer_num = int(float_num)      # 3 (truncates decimal)
print(integer_num)                # 3
```

### Practical Examples

**1. Calculate compound interest:**
```python
# A = P(1 + r/n)^(nt)
principal = 1000        # Initial amount
rate = 0.05            # 5% annual interest rate
compounds_per_year = 12 # Monthly compounding
years = 5

amount = principal * (1 + rate/compounds_per_year) ** (compounds_per_year * years)
print(f"After {years} years: ${amount:.2f}")
```

**2. Distance between two points:**
```python
import math

# Points (x1, y1) and (x2, y2)
x1, y1 = 1, 2
x2, y2 = 4, 6

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"Distance: {distance:.2f}")
```

---

## Python Casting

Casting (also called type conversion) is the process of converting one data type to another. It's like translating between different languages - you're taking information in one format and expressing it in another format.

### Why Do We Need Casting?

1. **User Input**: Input from users is always text, but you might need it as a number
2. **Data Processing**: Different operations require specific data types
3. **Display**: Converting numbers to text for better output formatting
4. **File Operations**: Reading from files often gives you strings that need conversion

### Types of Casting

**1. Implicit Casting (Automatic)**
Python automatically converts types when it's safe to do so:

```python
# Python automatically converts int to float when needed
integer_num = 5
float_num = 2.5
result = integer_num + float_num  # int + float = float
print(result, type(result))       # 7.5 <class 'float'>

# Boolean to integer (automatic in arithmetic)
print(True + 5)   # True becomes 1: 1 + 5 = 6
print(False * 10) # False becomes 0: 0 * 10 = 0
```

**2. Explicit Casting (Manual)**
You explicitly convert types using built-in functions:

### String Casting - str()

Converting other types to strings:

```python
# Number to string
age = 25
age_str = str(age)
print("I am " + age_str + " years old")  # Concatenation works now

# Boolean to string
is_student = True
status = str(is_student)
print("Student status: " + status)  # "Student status: True"

# List to string
numbers = [1, 2, 3]
numbers_str = str(numbers)
print("Numbers: " + numbers_str)    # "Numbers: [1, 2, 3]"

# Float to string
price = 19.99
print("Price: $" + str(price))      # "Price: $19.99"
```

### Integer Casting - int()

Converting other types to integers:

```python
# String to integer (string must contain valid number)
age_str = "25"
age_int = int(age_str)
print(age_int + 5)      # 30

# Float to integer (truncates decimal part)
price = 19.99
price_int = int(price)
print(price_int)        # 19 (not rounded, just truncated)

# Boolean to integer
print(int(True))        # 1
print(int(False))       # 0

# String with different bases
binary_str = "1010"
decimal_from_binary = int(binary_str, 2)  # Convert from base 2
print(decimal_from_binary)  # 10

hex_str = "FF"
decimal_from_hex = int(hex_str, 16)  # Convert from base 16
print(decimal_from_hex)     # 255
```

### Float Casting - float()

Converting other types to floating-point numbers:

```python
# String to float
price_str = "19.99"
price_float = float(price_str)
print(price_float)      # 19.99

# Integer to float
age = 25
age_float = float(age)
print(age_float)        # 25.0

# Boolean to float
print(float(True))      # 1.0
print(float(False))     # 0.0

# Scientific notation strings
sci_str = "2.5e-3"
sci_float = float(sci_str)
print(sci_float)        # 0.0025
```

### Boolean Casting - bool()

Converting other types to boolean:

```python
# Numbers to boolean
print(bool(0))          # False (zero is False)
print(bool(42))         # True (any non-zero number is True)
print(bool(-5))         # True (negative numbers are also True)
print(bool(0.0))        # False (zero float is False)

# Strings to boolean
print(bool(""))         # False (empty string is False)
print(bool("Hello"))    # True (any non-empty string is True)
print(bool("False"))    # True (even the string "False" is True!)

# Collections to boolean
print(bool([]))         # False (empty list is False)
print(bool([1, 2, 3]))  # True (non-empty list is True)
print(bool({}))         # False (empty dictionary is False)
print(bool({"key": "value"}))  # True (non-empty dictionary is True)

# None to boolean
print(bool(None))       # False (None is always False)
```

### List Casting - list()

Converting other types to lists:

```python
# String to list (splits into characters)
word = "hello"
char_list = list(word)
print(char_list)        # ['h', 'e', 'l', 'l', 'o']

# Tuple to list
coordinates = (10, 20, 30)
coord_list = list(coordinates)
print(coord_list)       # [10, 20, 30]

# Range to list
numbers = list(range(5))
print(numbers)          # [0, 1, 2, 3, 4]

# Set to list (order may vary)
unique_nums = {3, 1, 4, 1, 5}
num_list = list(unique_nums)
print(num_list)         # [1, 3, 4, 5] (duplicates removed, order may vary)
```

### Common Casting Errors and How to Handle Them

**1. Invalid String to Number Conversion:**
```python
# This will cause a ValueError
# age = int("hello")  # Error: invalid literal for int()

# Safe conversion with error handling
user_input = "hello"
try:
    age = int(user_input)
    print(f"Age: {age}")
except ValueError:
    print("Please enter a valid number!")
```

**2. Float to Int Loss of Precision:**
```python
# Be aware of truncation, not rounding
price = 19.99
price_int = int(price)
print(price_int)        # 19, not 20!

# If you want rounding, use round() first
price_rounded = int(round(price))
print(price_rounded)    # 20
```

### Practical Examples

**1. User Input Validation:**
```python
# Get user's age (input() always returns a string)
user_input = input("Enter your age: ")

try:
    age = int(user_input)
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
except ValueError:
    print("Please enter a valid number for age.")
```

**2. Calculating Average:**
```python
# Scores as strings (maybe from a file or web form)
score_strings = ["85", "92", "78", "96", "87"]

# Convert to integers and calculate average
scores = [int(score) for score in score_strings]
average = sum(scores) / len(scores)

print(f"Average score: {average:.1f}")
```

**3. Formatting Output:**
```python
# Calculate total price with tax
price = 19.99
tax_rate = 0.08
total = price * (1 + tax_rate)

# Convert to string for formatted output
print("Item price: $" + str(price))
print("Tax rate: " + str(int(tax_rate * 100)) + "%")
print("Total: $" + str(round(total, 2)))
```

**4. Working with Mixed Data:**
```python
# Mixed data from different sources
data = ["Alice", "25", "85.5", "True", "2023"]

name = str(data[0])      # "Alice" (already string, but being explicit)
age = int(data[1])       # 25
gpa = float(data[2])     # 85.5
is_enrolled = bool(data[3])  # True (non-empty string is True)
year = int(data[4])      # 2023

print(f"{name} is {age} years old")
print(f"GPA: {gpa}")
print(f"Enrolled: {is_enrolled}")
print(f"Year: {year}")
```

### Type Checking Before Casting

```python
def safe_int_convert(value):
    """Safely convert a value to integer"""
    if isinstance(value, int):
        return value
    elif isinstance(value, float):
        return int(value)
    elif isinstance(value, str):
        if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
            return int(value)
        else:
            raise ValueError(f"Cannot convert '{value}' to integer")
    else:
        raise TypeError(f"Cannot convert {type(value)} to integer")

# Test the function
print(safe_int_convert(42))      # 42
print(safe_int_convert(3.14))    # 3
print(safe_int_convert("123"))   # 123
print(safe_int_convert("-45"))   # -45
```

---

## Python Strings

Strings are sequences of characters - essentially text data. Think of a string as a chain of individual characters linked together. In Python, strings are incredibly versatile and powerful.

### Creating Strings

**Different Quote Types:**
```python
# Single quotes
single_quote = 'Hello World'

# Double quotes  
double_quote = "Hello World"

# Triple quotes for multi-line strings
multi_line = """This is a
multi-line string that
spans several lines"""

# Triple single quotes also work
another_multi = '''Another way to create
multi-line strings'''

print(single_quote)
print(multi_line)
```

**When to Use Each Type:**
```python
# Use single quotes for simple strings
name = 'Alice'

# Use double quotes when string contains single quotes
message = "It's a beautiful day!"

# Use triple quotes for long text or docstrings
description = """
This product is amazing!
It has many features:
- Feature 1
- Feature 2  
- Feature 3
"""
```

### String as Character Sequences

Strings are sequences, meaning you can access individual characters:

```python
word = "Python"

# Accessing characters by index (starting from 0)
print(word[0])    # 'P' (first character)
print(word[1])    # 'y' (second character)
print(word[-1])   # 'n' (last character)
print(word[-2])   # 'o' (second to last)

# Get string length
print(len(word))  # 6

# Check if character exists in string
print('P' in word)     # True
print('x' in word)     # False
print('py' in word)    # False (case sensitive)
print('Python' in word) # True
```

### String Properties

**Strings are Immutable:**
```python
text = "Hello"
# text[0] = 'h'  # This would cause an error!

# Instead, create a new string
text = 'h' + text[1:]  # "hello"
print(text)
```

**Strings are Iterable:**
```python
word = "Hello"

# Loop through each character
for char in word:
    print(char)
# Output: H, e, l, l, o (each on a new line)

# Create list of characters
char_list = list(word)
print(char_list)  # ['H', 'e', 'l', 'l', 'o']
```

---

## Slicing Strings

String slicing allows you to extract portions of a string. It's like cutting a piece of rope at specific points to get the section you want.

### Basic Slicing Syntax

The syntax is: `string[start:stop:step]`

- **start**: Where to begin (inclusive)
- **stop**: Where to end (exclusive)
- **step**: How many characters to skip (default is 1)

```python
text = "Programming"

# Basic slicing
print(text[0:4])    # "Prog" (characters 0, 1, 2, 3)
print(text[2:7])    # "ogram" (characters 2, 3, 4, 5, 6)
print(text[:4])     # "Prog" (start from beginning)
print(text[4:])     # "ramming" (go to end)
print(text[:])      # "Programming" (entire string)

# Negative indexing
print(text[-4:])    # "ming" (last 4 characters)
print(text[:-4])    # "Program" (all except last 4)
print(text[-7:-2])  # "rammi" (from 7th last to 2nd last)
```

### Advanced Slicing with Step

```python
text = "Programming"

# Using step
print(text[::2])    # "Pormmn" (every 2nd character)
print(text[1::2])   # "rgain" (every 2nd character starting from index 1)
print(text[::3])    # "Porm" (every 3rd character)

# Reverse string
print(text[::-1])   # "gnimmargorP" (entire string backwards)
print(text[5:1:-1]) # "marg" (from index 5 to 1, backwards)

# Extract every other character from a substring
print(text[2:8:2])  # "orm" (from index 2 to 8, every 2nd char)
```

### Practical Slicing Examples

```python
# Extract file extension
filename = "document.pdf"
extension = filename[-4:]  # ".pdf"
name = filename[:-4]       # "document"
print(f"Name: {name}, Extension: {extension}")

# Extract domain from email
email = "user@example.com"
at_index = email.find('@')
username = email[:at_index]    # "user"
domain = email[at_index+1:]    # "example.com"
print(f"Username: {username}, Domain: {domain}")

# Get first and last word
sentence = "The quick brown fox jumps"
words = sentence.split()
first_word = words[0]     # "The"
last_word = words[-1]     # "jumps"
print(f"First: {first_word}, Last: {last_word}")
```

---

## Modify Strings

Since strings are immutable, "modifying" actually means creating new strings with the changes you want.

### Changing Case

```python
text = "Hello World"

# Convert to different cases
print(text.upper())       # "HELLO WORLD"
print(text.lower())       # "hello world"
print(text.capitalize())  # "Hello world" (first letter only)
print(text.title())       # "Hello World" (title case)
print(text.swapcase())    # "hELLO wORLD" (swap case)

# Check case
print(text.isupper())     # False
print(text.islower())     # False
print(text.istitle())     # True
```

### Removing Whitespace

```python
# Text with extra whitespace
messy_text = "  Hello World  \n\t  "

print(f"'{messy_text}'")              # '  Hello World  \n\t  '
print(f"'{messy_text.strip()}'")      # 'Hello World' (both ends)
print(f"'{messy_text.lstrip()}'")     # 'Hello World  \n\t  ' (left side)
print(f"'{messy_text.rstrip()}'")     # '  Hello World' (right side)

# Remove specific characters
text = "...Hello World!!!"
print(text.strip('.!'))               # "Hello World"
```

### Replacing Text

```python
sentence = "I love cats and cats love me"

# Replace all occurrences
new_sentence = sentence.replace("cats", "dogs")
print(new_sentence)  # "I love dogs and dogs love me"

# Replace only first occurrence
limited_replace = sentence.replace("cats", "dogs", 1)
print(limited_replace)  # "I love dogs and cats love me"

# Replace multiple spaces with single space
messy = "Hello    world    python"
clean = messy.replace("    ", " ")
print(clean)  # "Hello world python"
```

### Splitting and Joining

```python
# Split strings into lists
sentence = "apple,banana,cherry,date"
fruits = sentence.split(",")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# Split on whitespace (default)
words = "Hello world Python".split()
print(words)  # ['Hello', 'world', 'Python']

# Limit splits
limited = "a-b-c-d-e".split("-", 2)
print(limited)  # ['a', 'b', 'c-d-e']

# Join lists into strings
word_list = ['Hello', 'world', 'Python']
sentence = " ".join(word_list)
print(sentence)  # "Hello world Python"

# Join with different separator
csv_format = ",".join(fruits)
print(csv_format)  # "apple,banana,cherry,date"
```

### Advanced String Modifications

```python
# Remove specific words
text = "I really really love Python programming"
words = text.split()
cleaned_words = [word for word in words if word != "really"]
result = " ".join(cleaned_words)
print(result)  # "I love Python programming"

# Reverse words in a sentence
sentence = "Hello world Python"
words = sentence.split()
reversed_sentence = " ".join(words[::-1])
print(reversed_sentence)  # "Python world Hello"

# Remove vowels
text = "Hello World"
vowels = "aeiouAEIOU"
no_vowels = "".join([char for char in text if char not in vowels])
print(no_vowels)  # "Hll Wrld"
```

---

## Concatenate Strings

String concatenation means joining strings together. There are several ways to do this in Python, each with its own advantages.

### Basic Concatenation with +

```python
first_name = "John"
last_name = "Doe"

# Simple concatenation
full_name = first_name + " " + last_name
print(full_name)  # "John Doe"

# Concatenating with numbers (need to convert)
age = 25
message = "I am " + str(age) + " years old"
print(message)  # "I am 25 years old"

# Multiple concatenations
greeting = "Hello" + ", " + "World" + "!"
print(greeting)  # "Hello, World!"
```

### Concatenation with += Operator

```python
# Building a string incrementally
result = ""
result += "Hello"
result += " "
result += "World"
print(result)  # "Hello World"

# Building a long string
story = ""
story += "Once upon a time, "
story += "there was a programmer "
story += "who loved Python."
print(story)
```

### Join Method (Efficient for Multiple Strings)

```python
# Join list of strings
words = ["Python", "is", "awesome"]
sentence = " ".join(words)
print(sentence)  # "Python is awesome"

# Join with different separators
items = ["apple", "banana", "cherry"]
print(", ".join(items))     # "apple, banana, cherry"
print(" | ".join(items))    # "apple | banana | cherry"
print("".join(items))       # "applebananacherry"

# Join numbers (need to convert to strings first)
numbers = [1, 2, 3, 4, 5]
number_string = "-".join(str(num) for num in numbers)
print(number_string)  # "1-2-3-4-5"
```

### Performance Comparison

```python
# Inefficient for many concatenations (creates new string each time)
result = ""
for i in range(1000):
    result += str(i)  # Not recommended for large loops

# Efficient for many concatenations
numbers = []
for i in range(1000):
    numbers.append(str(i))
result = "".join(numbers)  # Much faster
```

---

## Format Strings

String formatting allows you to create dynamic strings by inserting variables and expressions into predefined templates.

### 1. f-strings (Formatted String Literals) - Modern and Recommended

```python
name = "Alice"
age = 30
height = 5.6

# Basic f-string usage
message = f"My name is {name} and I am {age} years old"
print(message)  # "My name is Alice and I am 30 years old"

# Expressions inside f-strings
print(f"Next year I will be {age + 1}")  # "Next year I will be 31"
print(f"My height is {height} feet")

# Formatting numbers
price = 19.99999
print(f"Price: ${price:.2f}")  # "Price: $19.00" (2 decimal places)

# Multiple variables
print(f"{name} is {age} years old and {height} feet tall")
```

**Advanced f-string formatting:**
```python
# Number formatting
number = 1234567.89
print(f"{number:,.2f}")      # "1,234,567.89" (thousands separator)
print(f"{number:e}")         # "1.234568e+06" (scientific notation)

# Percentage formatting
ratio = 0.875
print(f"Success rate: {ratio:.1%}")  # "Success rate: 87.5%"

# Padding and alignment
name = "Bob"
print(f"|{name:>10}|")      # "|       Bob|" (right-aligned, width 10)
print(f"|{name:<10}|")      # "|Bob       |" (left-aligned, width 10)
print(f"|{name:^10}|")      # "|   Bob    |" (center-aligned, width 10)

# Date and time formatting
from datetime import datetime
now = datetime.now()
print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")
```

### 2. .format() Method

```python
name = "Alice"
age = 30

# Basic format usage
message = "My name is {} and I am {} years old".format(name, age)
print(message)

# Positional arguments
template = "Hello {0}, you are {1} years old. Nice to meet you {0}!"
print(template.format(name, age))

# Keyword arguments
template = "Hello {name}, you are {age} years old"
print(template.format(name="Bob", age=25))

# Mixed arguments
template = "{0} is {age} years old and lives in {1}"
print(template.format("Charlie", "New York", age=35))
```

**Advanced .format() usage:**
```python
# Number formatting
price = 19.99
print("Price: ${:.2f}".format(price))  # "Price: $19.99"

# Padding and alignment
name = "Alice"
print("|{:>10}|".format(name))         # "|     Alice|"
print("|{:<10}|".format(name))         # "|Alice     |"
print("|{:^10}|".format(name))         # "|  Alice   |"

# Custom padding character
print("|{:*^10}|".format(name))        # "|**Alice***|"
```

### 3. % Formatting (Old Style - Still Useful)

```python
name = "Alice"
age = 30
gpa = 3.14159

# Basic % formatting
message = "My name is %s and I am %d years old" % (name, age)
print(message)

# Different format specifiers
print("Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))

# Single value (no tuple needed)
print("Hello %s!" % name)
```

**Format specifiers:**
```python
number = 42
decimal = 3.14159

print("%d" % number)        # "42" (integer)
print("%f" % decimal)       # "3.141590" (float)
print("%.2f" % decimal)     # "3.14" (2 decimal places)
print("%e" % 1000000)       # "1.000000e+06" (scientific)
print("%x" % 255)           # "ff" (hexadecimal)
print("%o" % 8)             # "10" (octal)
```

### Practical Formatting Examples

**1. Creating Reports:**
```python
students = [
    ("Alice", 85, 92, 78),
    ("Bob", 92, 88, 95),
    ("Charlie", 78, 85, 90)
]

print("Student Report")
print("-" * 40)
print(f"{'Name':<10} {'Math':<6} {'Science':<8} {'English':<8} {'Average'}")
print("-" * 40)

for name, math, science, english in students:
    average = (math + science + english) / 3
    print(f"{name:<10} {math:<6} {science:<8} {english:<8} {average:.1f}")
```

**2. Progress Bar:**
```python
def show_progress(current, total):
    percentage = current / total
    bar_length = 20
    filled_length = int(bar_length * percentage)
    
    bar = "█" * filled_length + "-" * (bar_length - filled_length)
    print(f"\rProgress: |{bar}| {percentage:.1%} ({current}/{total})", end="")

# Example usage
for i in range(101):
    show_progress(i, 100)
    # time.sleep(0.05)  # Simulate work being done
```

**3. Table Formatting:**
```python
products = [
    ("Laptop", 999.99, 5),
    ("Mouse", 29.99, 50),
    ("Keyboard", 79.99, 25)
]

print(f"{'Product':<15} {'Price':<10} {'Stock':<10} {'Total Value'}")
print("-" * 50)

total_value = 0
for product, price, stock in products:
    value = price * stock
    total_value += value
    print(f"{product:<15} ${price:<9.2f} {stock:<10} ${value:.2f}")

print("-" * 50)
print(f"{'Total Inventory Value:':<35} ${total_value:.2f}")
```

---

## Escape Characters

Escape characters are special characters that are difficult or impossible to type directly into a string. They start with a backslash (`\`) followed by a character that represents the special meaning.

### Common Escape Characters

```python
# Newline (\n) - Creates a new line
print("Hello\nWorld")
# Output:
# Hello
# World

# Tab (\t) - Creates a tab space
print("Name:\tAlice\nAge:\t25")
# Output:
# Name:    Alice
# Age:     25

# Backslash (\\) - Literal backslash
print("C:\\Users\\Documents")  # C:\Users\Documents

# Single quote (\') - Single quote in single-quoted string
print('It\'s a beautiful day')  # It's a beautiful day

# Double quote (\") - Double quote in double-quoted string
print("She said \"Hello\" to me")  # She said "Hello" to me

# Carriage return (\r) - Returns cursor to beginning of line
print("Hello\rWorld")  # World (overwrites "Hello")

# Backspace (\b) - Removes previous character
print("Hello\b World")  # Hell World

# Form feed (\f) and vertical tab (\v) - Rarely used
print("Line 1\fLine 2")  # Form feed
print("Line 1\vLine 2")  # Vertical tab
```

### Practical Uses of Escape Characters

**1. File Paths:**
```python
# Windows file path
windows_path = "C:\\Users\\Alice\\Documents\\file.txt"
print(windows_path)

# Alternative: Use raw strings (we'll cover this below)
windows_path_raw = r"C:\Users\Alice\Documents\file.txt"
print(windows_path_raw)
```

**2. Formatted Output:**
```python
# Creating aligned columns
print("Name\t\tAge\tCity")
print("Alice\t\t25\tNew York")
print("Bob\t\t30\tLos Angeles")
print("Charlie\t\t35\tChicago")
```

**3. Multi-line Text:**
```python
# Poetry or long text
poem = "Roses are red,\nViolets are blue,\nPython is awesome,\nAnd so are you!"
print(poem)

# Menu display
menu = "1. New Game\n2. Load Game\n3. Settings\n4. Exit"
print(menu)
```

### Unicode Escape Characters

```python
# Unicode characters using \u (4 digits) or \U (8 digits)
print("\u2764")    # ❤ (heart symbol)
print("\u03B1")    # α (alpha)
print("\u03C0")    # π (pi)
print("\U0001F600") # 😀 (grinning face emoji)

# Hexadecimal escape
print("\x48\x65\x6C\x6C\x6F")  # "Hello" in hex
```

### Raw Strings (Avoiding Escapes)

Sometimes you want to use backslashes literally without them being interpreted as escape characters:

```python
# Regular string (escapes are interpreted)
regular = "C:\new\file.txt"  # \n becomes newline!
print(regular)  # Produces unexpected output

# Raw string (escapes are literal)
raw = r"C:\new\file.txt"
print(raw)      # C:\new\file.txt

# Useful for regular expressions
import re
pattern = r"\d{3}-\d{2}-\d{4}"  # Social security number pattern
print(pattern)  # \d{3}-\d{2}-\d{4}

# Useful for Windows paths
path = r"C:\Users\Alice\Desktop\my_file.txt"
print(path)
```

### Triple-Quoted Strings for Multi-line

```python
# Triple quotes preserve formatting and newlines
long_text = """
This is a long piece of text
that spans multiple lines.

It preserves all the formatting,
    including indentation
        and spacing.

No need for \n escape characters!
"""
print(long_text)

# Useful for SQL queries
sql_query = """
SELECT name, age, email
FROM users
WHERE age > 18
    AND active = 1
ORDER BY name;
"""
print(sql_query)
```

### Escape Character Examples in Practice

**1. Creating a Simple ASCII Art:**
```python
ascii_art = """
    /\\_/\\  
   ( o.o ) 
    > ^ <  
"""
print(ascii_art)

# Or using escape characters
cat = "    /\\_/\\\n   ( o.o )\n    > ^ <"
print(cat)
```

**2. Progress Indicator:**
```python
import time

def loading_animation():
    for i in range(10):
        print(f"\rLoading{'.' * (i % 4):<3}", end="")
        time.sleep(0.5)
    print("\rDone!   ")

# loading_animation()  # Uncomment to see animation
```

**3. Formatted Receipt:**
```python
def print_receipt(items):
    print("=" * 40)
    print("           RECEIPT")
    print("=" * 40)
    
    total = 0
    for item, price in items:
        print(f"{item:<25} ${price:>8.2f}")
        total += price
    
    print("-" * 40)
    print(f"{'TOTAL':<25} ${total:>8.2f}")
    print("=" * 40)
    print("Thank you for your purchase!\n")

# Example usage
items = [
    ("Coffee", 3.50),
    ("Sandwich", 7.99),
    ("Cookie", 2.25)
]
print_receipt(items)
```

---

## String Methods

Python strings come with many built-in methods that make text processing powerful and easy. These methods return new strings (remember, strings are immutable) and don't modify the original string.

### Case Methods

```python
text = "Hello World Python"

# Case conversion
print(text.upper())         # "HELLO WORLD PYTHON"
print(text.lower())         # "hello world python"
print(text.capitalize())    # "Hello world python"
print(text.title())         # "Hello World Python"
print(text.swapcase())      # "hELLO wORLD pYTHON"

# Case checking
print(text.isupper())       # False
print(text.islower())       # False
print(text.istitle())       # True
print("HELLO".isupper())    # True
print("hello".islower())    # True
```

### Search and Check Methods

```python
sentence = "The quick brown fox jumps over the lazy dog"

# Finding substrings
print(sentence.find("fox"))        # 16 (index where "fox" starts)
print(sentence.find("cat"))        # -1 (not found)
print(sentence.rfind("the"))       # 31 (last occurrence of "the")
print(sentence.index("fox"))       # 16 (like find, but raises error if not found)

# Counting occurrences
print(sentence.count("the"))       # 2
print(sentence.count("o"))         # 4

# Checking start and end
print(sentence.startswith("The"))  # True
print(sentence.startswith("the"))  # False (case sensitive)
print(sentence.endswith("dog"))    # True
print(sentence.endswith("."))      # False

# Checking membership (alternative to 'in' operator)
print("fox" in sentence)           # True
print("cat" in sentence)           # False
```

### Character Type Checking

```python
# Different types of strings for testing
alpha_text = "HelloWorld"
numeric_text = "12345"
alnum_text = "Hello123"
space_text = "   "
mixed_text = "Hello World!"

# Check character types
print(alpha_text.isalpha())     # True (only letters)
print(numeric_text.isdigit())   # True (only digits)
print(alnum_text.isalnum())     # True (letters and numbers)
print(space_text.isspace())     # True (only whitespace)

# More specific checks
print("123".isdecimal())        # True (decimal numbers)
print("½".isnumeric())          # True (numeric characters)
print("hello".isidentifier())   # True (valid Python identifier)
print("2hello".isidentifier())  # False (can't start with number)

# ASCII check
print("Hello".isascii())        # True
print("Héllo".isascii())        # False (contains accented character)
```

### Cleaning and Trimming Methods

```python
# Text with various whitespace
messy_text = "   Hello World   \n\t  "

# Trimming whitespace
print(f"'{messy_text.strip()}'")    # 'Hello World'
print(f"'{messy_text.lstrip()}'")   # 'Hello World   \n\t  '
print(f"'{messy_text.rstrip()}'")   # '   Hello World'

# Trimming specific characters
text_with_chars = "...Hello World!!!"
print(text_with_chars.strip(".!"))  # "Hello World"

# Remove prefix/suffix (Python 3.9+)
url = "https://www.example.com"
if url.startswith("https://"):
    clean_url = url.removeprefix("https://")
    print(clean_url)  # www.example.com

filename = "document.pdf"
if filename.endswith(".pdf"):
    name_only = filename.removesuffix(".pdf")
    print(name_only)  # document
```

### Splitting and Joining Methods

```python
# Different ways to split strings
sentence = "apple,banana,cherry,date"
csv_data = "name;age;city"
paragraph = "Line 1\nLine 2\nLine 3"

# Split on specific character
fruits = sentence.split(",")
print(fruits)  # ['apple', 'banana', 'cherry', 'date']

# Split on whitespace (default)
words = "Hello world Python".split()
print(words)  # ['Hello', 'world', 'Python']

# Limit number of splits
limited = "a-b-c-d-e".split("-", 2)
print(limited)  # ['a', 'b', 'c-d-e']

# Split from the right
right_split = "one.two.three.four".rsplit(".", 2)
print(right_split)  # ['one.two', 'three', 'four']

# Split into lines
lines = paragraph.splitlines()
print(lines)  # ['Line 1', 'Line 2', 'Line 3']

# Partition (split into exactly 3 parts)
email = "user@example.com"
parts = email.partition("@")
print(parts)  # ('user', '@', 'example.com')
```

### Replacement Methods

```python
text = "I love cats and cats love me"

# Replace all occurrences
new_text = text.replace("cats", "dogs")
print(new_text)  # "I love dogs and dogs love me"

# Replace with limit
limited_replace = text.replace("cats", "dogs", 1)
print(limited_replace)  # "I love dogs and cats love me"

# Translation table for character replacement
vowels = "aeiou"
numbers = "12345"
translation_table = str.maketrans(vowels, numbers)

text = "hello world"
translated = text.translate(translation_table)
print(translated)  # "h2ll4 w4rld"

# Remove characters using translation
text = "Hello, World!"
remove_punctuation = str.maketrans("", "", ",!")
clean_text = text.translate(remove_punctuation)
print(clean_text)  # "Hello World"
```

### Alignment and Padding Methods

```python
text = "Python"

# Center alignment
print(text.center(20))          # "       Python       "
print(text.center(20, "*"))     # "*******Python*******"

# Left alignment (padding on right)
print(text.ljust(15))           # "Python         "
print(text.ljust(15, "-"))      # "Python---------"

# Right alignment (padding on left)
print(text.rjust(15))           # "         Python"
print(text.rjust(15, "-"))      # "---------Python"

# Zero padding for numbers
number = "42"
print(number.zfill(5))          # "00042"
print("-42".zfill(5))           # "-0042"
```

### Advanced String Methods

```python
# Expanding tabs
text_with_tabs = "Hello\tWorld\tPython"
expanded = text_with_tabs.expandtabs(4)  # Tab size = 4
print(expanded)  # "Hello   World   Python"

# Encoding/Decoding
text = "Hello World"
encoded = text.encode('utf-8')
print(encoded)  # b'Hello World'
decoded = encoded.decode('utf-8')
print(decoded)  # "Hello World"

# Format mapping
template = "Hello {name}, you are {age} years old"
data = {"name": "Alice", "age": 30}
formatted = template.format_map(data)
print(formatted)  # "Hello Alice, you are 30 years old"
```

### Practical Examples Using String Methods

**1. Email Validation (Basic):**
```python
def is_valid_email(email):
    # Basic email validation
    email = email.strip().lower()
    
    if not email:
        return False
    
    if email.count("@") != 1:
        return False
    
    local, domain = email.split("@")
    
    if not local or not domain:
        return False
    
    if not domain.count(".") >= 1:
        return False
    
    return True

# Test emails
emails = ["user@example.com", "invalid.email", "user@", "@domain.com"]
for email in emails:
    print(f"{email}: {is_valid_email(email)}")
```

**2. Text Processing Pipeline:**
```python
def clean_text(text):
    """Clean and normalize text for processing"""
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    punctuation = ".,!?;:\"'()[]{}=-+*/\\|`~@#$%^&"
    for p in punctuation:
        text = text.replace(p, "")
    
    return text.strip()

# Example usage
messy_text = "  Hello,    WORLD!!!   How are you???  "
clean = clean_text(messy_text)
print(f"Original: '{messy_text}'")
print(f"Cleaned:  '{clean}'")  # "hello world how are you"
```

**3. Password Strength Checker:**
```python
def check_password_strength(password):
    """Check password strength and provide feedback"""
    if len(password) < 8:
        return "Too short (minimum 8 characters)"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if score == 4:
        return "Strong password"
    elif score == 3:
        return "Good password"
    elif score == 2:
        return "Weak password"
    else:
        return "Very weak password"

# Test passwords
passwords = ["password", "Password1", "Password1!", "P@ssw0rd!"]
for pwd in passwords:
    print(f"'{pwd}': {check_password_strength(pwd)}")
```

**4. Word Frequency Counter:**
```python
def word_frequency(text):
    """Count word frequency in text"""
    # Clean and split text
    text = text.lower()
    # Remove punctuation
    for p in ".,!?;:\"'()[]{}":
        text = text.replace(p, "")
    
    words = text.split()
    frequency = {}
    
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

# Example usage
sample_text = "Python is great. Python is powerful. Python is easy to learn."
freq = word_frequency(sample_text)
for word, count in sorted(freq.items()):
    print(f"{word}: {count}")
```

---

## String Exercises

Let's practice what we've learned with hands-on exercises. Try to solve these yourself before looking at the solutions!

### Exercise 1: Basic String Operations
**Problem:** Create a program that takes a user's full name and displays it in different formats.

```python
# Solution
def format_name(full_name):
    """Format name in different ways"""
    # Clean the input
    name = full_name.strip()
    
    # Split into parts
    parts = name.split()
    
    if len(parts) < 2:
        return "Please enter at least first and last name"
    
    first = parts[0]
    last = parts[-1]
    
    print(f"Original: {name}")
    print(f"Uppercase: {name.upper()}")
    print(f"Lowercase: {name.lower()}")
    print(f"Title Case: {name.title()}")
    print(f"Initials: {first[0].upper()}.{last[0].upper()}.")
    print(f"Last, First: {last}, {first}")
    print(f"Length: {len(name)} characters")

# Test it
format_name("john doe smith")
```

### Exercise 2: Text Analysis
**Problem:** Create a function that analyzes a paragraph of text.

```python
# Solution
def analyze_text(text):
    """Analyze various aspects of text"""
    # Basic counts
    char_count = len(text)
    char_no_spaces = len(text.replace(" ", ""))
    word_count = len(text.split())
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    paragraph_count = text.count('\n\n') + 1
    
    # Character analysis
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    
    # Most common word
    words = text.lower().split()
    word_freq = {}
    for word in words:
        # Remove punctuation
        clean_word = word.strip(".,!?;:")
        word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
    
    most_common = max(word_freq, key=word_freq.get) if word_freq else "None"
    
    # Results
    print("TEXT ANALYSIS")
    print("-" * 30)
    print(f"Characters (with spaces): {char_count}")
    print(f"Characters (no spaces): {char_no_spaces}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")
    print(f"Paragraphs: {paragraph_count}")
    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Most common word: '{most_common}' ({word_freq[most_common]} times)")
    
    if word_count > 0:
        avg_word_length = char_no_spaces / word_count
        print(f"Average word length: {avg_word_length:.1f} characters")

# Test it
sample_text = """
Python is a powerful programming language. It is easy to learn and fun to use.
Python can be used for web development, data analysis, and artificial intelligence.
Many companies use Python for their projects.
"""
analyze_text(sample_text.strip())
```

### Exercise 3: String Manipulation Challenge
**Problem:** Create a function that implements a simple cipher (Caesar cipher).

```python
# Solution
def caesar_cipher(text, shift, mode="encrypt"):
    """
    Encrypt or decrypt text using Caesar cipher
    shift: number of positions to shift (positive for encrypt, negative for decrypt)
    mode: 'encrypt' or 'decrypt'
    """
    if mode == "decrypt":
        shift = -shift
    
    result = ""
    
    for char in text:
        if char.isalpha():
            # Handle uppercase letters
            if char.isupper():
                shifted = ord(char) - ord('A')
                shifted = (shifted + shift) % 26
                result += chr(shifted + ord('A'))
            # Handle lowercase letters
            else:
                shifted = ord(char) - ord('a')
                shifted = (shifted + shift) % 26
                result += chr(shifted + ord('a'))
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

# Test the cipher
original = "Hello World! Python is Amazing."
encrypted = caesar_cipher(original, 3, "encrypt")
decrypted = caesar_cipher(encrypted, 3, "decrypt")

print(f"Original:  {original}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
```

### Exercise 4: Palindrome Checker
**Problem:** Create a function that checks if a string is a palindrome (reads the same forwards and backwards).

```python
# Solution
def is_palindrome(text, ignore_case=True, ignore_spaces=True, ignore_punctuation=True):
    """
    Check if text is a palindrome with various options
    """
    # Clean the text based on options
    clean_text = text
    
    if ignore_case:
        clean_text = clean_text.lower()
    
    if ignore_spaces:
        clean_text = clean_text.replace(" ", "")
    
    if ignore_punctuation:
        punctuation = ".,!?;:\"'()-[]{}@#$%^&*+=|\\`~"
        for p in punctuation:
            clean_text = clean_text.replace(p, "")
    
    # Check if it's the same forwards and backwards
    return clean_text == clean_text[::-1]

# Test cases
test_cases = [
    "racecar",
    "A man a plan a canal Panama",
    "race a car",
    "hello",
    "Madam, I'm Adam",
    "12321",
    "Was it a car or a cat I saw?"
]

print("PALINDROME CHECKER")
print("-" * 40)
for test in test_cases:
    result = is_palindrome(test)
    print(f"'{test}' -> {result}")
```

### Exercise 5: Text Formatter
**Problem:** Create a text formatter that can justify text, add line numbers, and create word wrapping.

```python
# Solution
def format_text(text, width=50, justify="left", add_numbers=False, wrap_words=True):
    """
    Format text with various options
    """
    # Split text into paragraphs
    paragraphs = text.split('\n\n')
    formatted_paragraphs = []
    
    line_number = 1
    
    for paragraph in paragraphs:
        if wrap_words:
            # Word wrapping
            words = paragraph.split()
            lines = []
            current_line = ""
            
            for word in words:
                if len(current_line + " " + word) <= width:
                    if current_line:
                        current_line += " " + word
                    else:
                        current_line = word
                else:
                    if current_line:
                        lines.append(current_line)
                        current_line = word
                    else:
                        lines.append(word)  # Word is longer than width
            
            if current_line:
                lines.append(current_line)
        else:
            lines = [paragraph]
        
        # Justify lines
        justified_lines = []
        for line in lines:
            if justify == "center":
                justified_line = line.center(width)
            elif justify == "right":
                justified_line = line.rjust(width)
            else:  # left justify (default)
                justified_line = line.ljust(width)
            
            # Add line numbers if requested
            if add_numbers:
                justified_line = f"{line_number:3d}. {justified_line}"
                line_number += 1
            
            justified_lines.append(justified_line)
        
        formatted_paragraphs.append("\n".join(justified_lines))
    
    return "\n\n".join(formatted_paragraphs)

# Test the formatter
sample_text = """Python is a high-level programming language that emphasizes code readability and simplicity. It was created by Guido van Rossum and first released in 1991.

Python supports multiple programming paradigms including procedural, object-oriented, and functional programming. Its extensive standard library and active community make it ideal for various applications."""

print("ORIGINAL:")
print(sample_text)
print("\n" + "="*60 + "\n")

print("FORMATTED (Center, 40 chars, with line numbers):")
formatted = format_text(sample_text, width=40, justify="center", add_numbers=True)
print(formatted)
```

### Exercise 6: Password Generator
**Problem:** Create a password generator with customizable options.

```python
import random
import string

# Solution
def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                     include_digits=True, include_symbols=True, 
                     exclude_ambiguous=False, custom_chars=""):
    """
    Generate a random password with specified criteria
    """
    if length < 1:
        return "Password length must be at least 1"
    
    # Build character set
    chars = ""
    
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_digits:
        chars += string.digits
    if include_symbols:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    if custom_chars:
        chars += custom_chars
    
    if exclude_ambiguous:
        # Remove confusing characters
        ambiguous = "0O1lI|"
        chars = "".join(c for c in chars if c not in ambiguous)
    
    if not chars:
        return "No character types selected"
    
    # Generate password ensuring at least one character from each selected type
    password = []
    
    # Add at least one character from each selected type
    if include_lowercase:
        password.append(random.choice(string.ascii_lowercase))
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_symbols:
        password.append(random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?"))
    
    # Fill the rest randomly
    for _ in range(length - len(password)):
        password.append(random.choice(chars))
    
    # Shuffle the password to avoid predictable patterns
    random.shuffle(password)
    
    return "".join(password)

# Test password generator
def test_password_generator():
    print("PASSWORD GENERATOR TESTS")
    print("-" * 40)
    
    configs = [
        {"length": 8, "include_symbols": False},
        {"length": 12, "exclude_ambiguous": True},
        {"length": 16, "include_uppercase": True, "include_lowercase": True, 
         "include_digits": True, "include_symbols": True},
        {"length": 10, "custom_chars": "αβγδε"}
    ]
    
    for i, config in enumerate(configs, 1):
        password = generate_password(**config)
        print(f"Password {i}: {password}")
        print(f"Config: {config}")
        print()

test_password_generator()
```

### Exercise 7: Log Parser
**Problem:** Create a function that parses log entries and extracts useful information.

```python
import re
from datetime import datetime

# Solution
def parse_log_entry(log_line):
    """
    Parse a log entry and extract structured information
    Expected format: [TIMESTAMP] LEVEL: MESSAGE
    Example: [2023-12-01 14:30:25] ERROR: Database connection failed
    """
    # Regular expression to match log format
    pattern = r'\[([^\]]+)\]\s+([A-Z]+):\s+(.+)'
    match = re.match(pattern, log_line)
    
    if not match:
        return {"error": "Invalid log format", "raw": log_line}
    
    timestamp_str, level, message = match.groups()
    
    # Parse timestamp
    try:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        timestamp = None
    
    return {
        "timestamp": timestamp,
        "level": level,
        "message": message,
        "raw": log_line
    }

def analyze_logs(log_text):
    """
    Analyze multiple log entries and provide summary
    """
    lines = log_text.strip().split('\n')
    parsed_logs = []
    level_counts = {}
    error_messages = []
    
    for line in lines:
        if line.strip():
            parsed = parse_log_entry(line.strip())
            parsed_logs.append(parsed)
            
            if 'level' in parsed:
                level = parsed['level']
                level_counts[level] = level_counts.get(level, 0) + 1
                
                if level == 'ERROR':
                    error_messages.append(parsed['message'])
    
    print("LOG ANALYSIS SUMMARY")
    print("-" * 50)
    print(f"Total log entries: {len(parsed_logs)}")
    
    print("\nLevel Distribution:")
    for level, count in sorted(level_counts.items()):
        print(f"  {level}: {count}")
    
    if error_messages:
        print(f"\nError Messages:")
        for i, error in enumerate(error_messages[:5], 1):  # Show first 5 errors
            print(f"  {i}. {error}")
        if len(error_messages) > 5:
            print(f"  ... and {len(error_messages) - 5} more errors")
    
    return parsed_logs

# Test log parser
sample_logs = """
[2023-12-01 10:15:30] INFO: Application started successfully
[2023-12-01 10:15:31] DEBUG: Loading configuration file
[2023-12-01 10:15:32] INFO: Database connection established
[2023-12-01 10:20:45] WARNING: High memory usage detected
[2023-12-01 10:25:10] ERROR: Failed to process user request
[2023-12-01 10:25:11] ERROR: Database timeout occurred
[2023-12-01 10:30:00] INFO: Backup process started
[2023-12-01 10:35:15] INFO: Backup completed successfully
"""

analyze_logs(sample_logs)
```

### Challenge Exercise: Advanced Text Processor
**Problem:** Create a comprehensive text processor that can handle multiple operations.

```python
# Solution
class TextProcessor:
    """
    A comprehensive text processing class
    """
    
    def __init__(self, text=""):
        self.text = text
        self.history = [text]  # Keep history of changes
    
    def set_text(self, text):
        """Set new text"""
        self.text = text
        self.history.append(text)
        return self
    
    def to_upper(self):
        """Convert to uppercase"""
        self.text = self.text.upper()
        self.history.append(self.text)
        return self
    
    def to_lower(self):
        """Convert to lowercase"""
        self.text = self.text.lower()
        self.history.append(self.text)
        return self
    
    def to_title(self):
        """Convert to title case"""
        self.text = self.text.title()
        self.history.append(self.text)
        return self
    
    def reverse(self):
        """Reverse the text"""
        self.text = self.text[::-1]
        self.history.append(self.text)
        return self
    
    def remove_vowels(self):
        """Remove all vowels"""
        vowels = "aeiouAEIOU"
        self.text = "".join(char for char in self.text if char not in vowels)
        self.history.append(self.text)
        return self
    
    def pig_latin(self):
        """Convert to pig latin"""
        words = self.text.split()
        pig_words = []
        
        for word in words:
            if word and word[0].lower() in "aeiou":
                pig_words.append(word + "way")
            elif word:
                pig_words.append(word[1:] + word[0] + "ay")
            else:
                pig_words.append(word)
        
        self.text = " ".join(pig_words)
        self.history.append(self.text)
        return self
    
    def count_words(self):
        """Count words in text"""
        return len(self.text.split())
    
    def count_characters(self, include_spaces=True):
        """Count characters"""
        if include_spaces:
            return len(self.text)
        else:
            return len(self.text.replace(" ", ""))
    
    def find_longest_word(self):
        """Find the longest word"""
        words = self.text.split()
        if not words:
            return ""
        return max(words, key=len)
    
    def get_history(self):
        """Get processing history"""
        return self.history.copy()
    
    def undo(self):
        """Undo last operation"""
        if len(self.history) > 1:
            self.history.pop()
            self.text = self.history[-1]
        return self
    
    def reset(self):
        """Reset to original text"""
        if self.history:
            self.text = self.history[0]
            self.history = [self.text]
        return self
    
    def __str__(self):
        return self.text
    
    def __repr__(self):
        return f"TextProcessor('{self.text}')"

# Test the TextProcessor
def test_text_processor():
    print("TEXT PROCESSOR DEMO")
    print("=" * 50)
    
    # Create processor with initial text
    processor = TextProcessor("Hello World Python Programming")
    
    print(f"Original: {processor}")
    
    # Chain operations
    result = (processor
              .to_lower()
              .reverse()
              .to_title())
    
    print(f"After lower->reverse->title: {result}")
    
    # Show history
    print("\nProcessing History:")
    for i, step in enumerate(processor.get_history()):
        print(f"  {i}: {step}")
    
    # Test more operations
    processor.set_text("Hello World")
    print(f"\nNew text: {processor}")
    print(f"Pig Latin: {processor.pig_latin()}")
    
    processor.set_text("Programming is fun and exciting")
    print(f"\nAnother text: {processor}")
    print(f"Without vowels: {processor.remove_vowels()}")
    
    # Undo operation
    print(f"After undo: {processor.undo()}")
    
    # Statistics
    processor.set_text("Python is a powerful programming language")
    print(f"\nText: {processor}")
    print(f"Words: {processor.count_words()}")
    print(f"Characters: {processor.count_characters()}")
    print(f"Characters (no spaces): {processor.count_characters(False)}")
    print(f"Longest word: {processor.find_longest_word()}")

test_text_processor()
```

These exercises cover a wide range of string operations and help you practice:
- Basic string manipulation
- Text analysis and statistics
- Encryption/decryption algorithms
- Pattern matching and validation
- Text formatting and alignment
- Object-oriented programming with strings
- Chaining operations
- History management

Try to solve these exercises step by step, and don't hesitate to experiment with variations and improvements!

---

## Python Booleans

Booleans represent one of two values: `True` or `False`. They're named after George Boole, a mathematician who worked with logic. Think of booleans as yes/no, on/off, or 1/0 switches in your programs.

### Boolean Values

```python
# Boolean literals
is_sunny = True
is_raining = False

print(is_sunny)    # True
print(is_raining)  # False
print(type(is_sunny))  # <class 'bool'>

# Booleans are actually a subclass of integers
print(int(True))   # 1
print(int(False))  # 0
print(True + True) # 2
print(True * 5)    # 5
```

### Boolean from Comparisons

Most boolean values come from comparing things:

```python
# Comparison operators return booleans
age = 25
print(age > 18)        # True
print(age < 18)        # False
print(age == 25)       # True
print(age != 30)       # True
print(age >= 25)       # True
print(age <= 24)       # False

# Comparing strings
name1 = "Alice"
name2 = "Bob"
print(name1 == name2)  # False
print(name1 < name2)   # True (alphabetical order)

# Comparing different types
print(5 == "5")        # False (different types)
print(5 == 5.0)        # True (numeric equality)
```

### Truthiness - What Python Considers True or False

In Python, every value can be evaluated as either `True` or `False` in a boolean context:

**Values that are considered `False` (Falsy):**
```python
# Numbers
print(bool(0))         # False
print(bool(0.0))       # False
print(bool(0j))        # False (complex zero)

# Empty collections
print(bool([]))        # False (empty list)
print(bool({}))        # False (empty dictionary)
print(bool(set()))     # False (empty set)
print(bool(()))        # False (empty tuple)
print(bool(""))        # False (empty string)

# Special value
print(bool(None))      # False
```

**Everything else is considered `True` (Truthy):**
```python
# Non-zero numbers
print(bool(1))         # True
print(bool(-1))        # True
print(bool(3.14))      # True

# Non-empty collections
print(bool([1, 2, 3])) # True
print(bool("hello"))   # True
print(bool({"a": 1}))  # True

# Even these are True!
print(bool("False"))   # True (non-empty string)
print(bool([0]))       # True (non-empty list, even with False-y content)
```

### Boolean Operators

**Logical AND (`and`):**
```python
# Both conditions must be True
age = 25
has_license = True

can_rent_car = age >= 21 and has_license
print(can_rent_car)  # True

# Short-circuit evaluation: if first is False, second isn't checked
print(False and print("This won't print"))  # False (print not executed)
print(True and print("This will print"))    # This will print, then None
```

**Logical OR (`or`):**
```python
# At least one condition must be True
is_weekend = False
is_holiday = True

can_sleep_in = is_weekend or is_holiday
print(can_sleep_in)  # True

# Short-circuit evaluation: if first is True, second isn't checked
print(True or print("This won't print"))   # True (print not executed)
print(False or print("This will print"))   # This will print, then None
```

**Logical NOT (`not`):**
```python
# Reverses the boolean value
is_raining = False
is_sunny = not is_raining
print(is_sunny)      # True

# not with truthiness
print(not "")        # True (empty string is falsy)
print(not "hello")   # False (non-empty string is truthy)
print(not [])        # True (empty list is falsy)
print(not [1, 2])    # False (non-empty list is truthy)
```

### Operator Precedence

```python
# Order of operations: not, and, or (from highest to lowest precedence)
result = not False or True and False
print(result)  # True

# Step by step:
# 1. not False = True
# 2. True and False = False  
# 3. True or False = True

# Use parentheses for clarity
result = (not False) or (True and False)
print(result)  # True - same result, but clearer
```

### Membership Operators

```python
# 'in' and 'not in' return booleans
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)      # True
print("grape" in fruits)      # False
print("grape" not in fruits)  # True

# Works with strings too
sentence = "Python is awesome"
print("Python" in sentence)      # True
print("Java" not in sentence)    # True

# Works with dictionaries (checks keys)
person = {"name": "Alice", "age": 30}
print("name" in person)       # True
print("height" in person)     # False
```

### Identity Operators

```python
# 'is' and 'is not' check if objects are the same in memory
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)   # True (same content)
print(a is b)   # False (different objects in memory)
print(a is c)   # True (same object)

# Special case with small integers and strings (Python optimization)
x = 5
y = 5
print(x is y)   # True (Python reuses small integer objects)

# With None (always use 'is' with None)
value = None
print(value is None)     # True (correct way)
print(value == None)     # True (works, but not recommended)
```

### Boolean Functions

```python
# any() - True if any element is truthy
numbers = [0, 0, 1, 0]
print(any(numbers))      # True (1 is truthy)

empty_list = []
print(any(empty_list))   # False (empty iterable)

# all() - True if all elements are truthy
numbers = [1, 2, 3, 4]
print(all(numbers))      # True (all non-zero)

mixed_numbers = [1, 2, 0, 4]
print(all(mixed_numbers)) # False (0 is falsy)

empty_list = []
print(all(empty_list))   # True (vacuously true - all elements of empty set satisfy condition)
```

### Practical Examples

**1. Input Validation:**
```python
def validate_age(age_str):
    """Validate age input"""
    # Check if it's a digit
    if not age_str.isdigit():
        return False, "Age must be a number"
    
    age = int(age_str)
    
    # Check age range
    if age < 0 or age > 150:
        return False, "Age must be between 0 and 150"
    
    return True, "Valid age"

# Test validation
test_ages = ["25", "-5", "abc", "200", "30"]
for age in test_ages:
    is_valid, message = validate_age(age)
    print(f"Age '{age}': {is_valid} - {message}")
```

**2. Access Control System:**
```python
def can_access_system(user_age, has_permission, is_business_hours, is_emergency=False):
    """Determine if user can access the system"""
    
    # Must be adult
    is_adult = user_age >= 18
    
    # Normal access conditions
    normal_access = is_adult and has_permission and is_business_hours
    
    # Emergency access (relaxed rules)
    emergency_access = is_emergency and has_permission
    
    return normal_access or emergency_access

# Test different scenarios
scenarios = [
    {"age": 25, "perm": True, "hours": True, "emergency": False},    # Normal access
    {"age": 16, "perm": True, "hours": True, "emergency": False},    # Too young
    {"age": 25, "perm": False, "hours": True, "emergency": False},   # No permission
    {"age": 25, "perm": True, "hours": False, "emergency": False},   # After hours
    {"age": 25, "perm": True, "hours": False, "emergency": True},    # Emergency access
]

for i, scenario in enumerate(scenarios, 1):
    access = can_access_system(
        scenario["age"], 
        scenario["perm"], 
        scenario["hours"], 
        scenario["emergency"]
    )
    print(f"Scenario {i}: {'GRANTED' if access else 'DENIED'}")
    print(f"  Age: {scenario['age']}, Permission: {scenario['perm']}, "
          f"Business Hours: {scenario['hours']}, Emergency: {scenario['emergency']}")
```

**3. Data Filtering:**
```python
def filter_products(products, min_price=0, max_price=float('inf'), 
                   in_stock_only=False, categories=None):
    """Filter products based on criteria"""
    filtered = []
    
    for product in products:
        # Price check
        price_ok = min_price <= product['price'] <= max_price
        
        # Stock check
        stock_ok = not in_stock_only or product['stock'] > 0
        
        # Category check
        category_ok = categories is None or product['category'] in categories
        
        # All conditions must be true
        if price_ok and stock_ok and category_ok:
            filtered.append(product)
    
    return filtered

# Sample data
products = [
    {'name': 'Laptop', 'price': 999, 'stock': 5, 'category': 'Electronics'},
    {'name': 'Book', 'price': 15, 'stock': 0, 'category': 'Education'},
    {'name': 'Phone', 'price': 699, 'stock': 10, 'category': 'Electronics'},
    {'name': 'Desk', 'price': 200, 'stock': 3, 'category': 'Furniture'},
]

# Filter examples
print("All products under $500:")
cheap_products = filter_products(products, max_price=500)
for p in cheap_products:
    print(f"  {p['name']}: ${p['price']}")

print("\nElectronics in stock:")
electronics_in_stock = filter_products(
    products, 
    in_stock_only=True, 
    categories=['Electronics']
)
for p in electronics_in_stock:
    print(f"  {p['name']}: ${p['price']} (Stock: {p['stock']})")
```

**4. Form Validation:**
```python
def validate_registration_form(data):
    """Validate user registration form"""
    errors = []
    
    # Check required fields
    required_fields = ['username', 'email', 'password']
    for field in required_fields:
        if not data.get(field) or not data[field].strip():
            errors.append(f"{field.capitalize()} is required")
    
    # Username validation
    username = data.get('username', '')
    if username:
        if len(username) < 3:
            errors.append("Username must be at least 3 characters")
        if not username.isalnum():
            errors.append("Username must contain only letters and numbers")
    
    # Email validation (basic)
    email = data.get('email', '')
    if email:
        if '@' not in email or email.count('@') != 1:
            errors.append("Invalid email format")
        elif not email.split('@')[1]:
            errors.append("Email domain is required")
    
    # Password validation
    password = data.get('password', '')
    if password:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        if not (has_upper and has_lower and has_digit):
            errors.append("Password must contain uppercase, lowercase, and digit")
    
    # Age validation
    age = data.get('age')
    if age is not None:
        try:
            age_int = int(age)
            if age_int < 13 or age_int > 120:
                errors.append("Age must be between 13 and 120")
        except (ValueError, TypeError):
            errors.append("Age must be a valid number")
    
    # Return validation result
    is_valid = len(errors) == 0
    return is_valid, errors

# Test form validation
test_forms = [
    {
        'username': 'alice123',
        'email': 'alice@example.com',
        'password': 'SecurePass1',
        'age': '25'
    },
    {
        'username': 'ab',  # Too short
        'email': 'invalid-email',  # Invalid format
        'password': 'weak',  # Too simple
        'age': 'not-a-number'  # Invalid age
    },
    {
        'username': '',  # Empty
        'email': '',     # Empty
        'password': '',  # Empty
    }
]

for i, form_data in enumerate(test_forms, 1):
    print(f"\nTesting Form {i}:")
    is_valid, errors = validate_registration_form(form_data)
    
    if is_valid:
        print("✓ Form is valid!")
    else:
        print("✗ Form has errors:")
        for error in errors:
            print(f"  - {error}")
```

---

## Python Operators

Operators are special symbols that perform operations on variables and values. Think of them as the verbs in your code - they tell Python what actions to perform.

### Arithmetic Operators

These perform mathematical calculations:

```python
a = 15
b = 4

# Basic arithmetic
print(a + b)    # Addition: 19
print(a - b)    # Subtraction: 11
print(a * b)    # Multiplication: 60
print(a / b)    # Division: 3.75 (always returns float)
print(a // b)   # Floor division: 3 (integer division)
print(a % b)    # Modulus (remainder): 3
print(a ** b)   # Exponentiation: 50625 (15^4)

# Order of operations (PEMDAS)
result = 2 + 3 * 4 ** 2
print(result)   # 50 (not 400: 2 + 3 * 16 = 2 + 48 = 50)

# Use parentheses to change order
result = (2 + 3) * 4 ** 2
print(result)   # 80 (5 * 16 = 80)
```

**Practical Examples:**
```python
# Calculate compound interest
principal = 1000
rate = 0.05  # 5%
time = 3     # years

compound_interest = principal * (1 + rate) ** time
print(f"Amount after {time} years: ${compound_interest:.2f}")

# Check if number is even or odd
number = 17
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# Calculate circle area
import math
radius = 5
area = math.pi * radius ** 2
print(f"Circle area: {area:.2f}")
```

### Assignment Operators

These assign values to variables:

```python
# Basic assignment
x = 10
print(x)  # 10

# Augmented assignment operators (modify and assign)
x += 5   # Same as: x = x + 5
print(x)  # 15

x -= 3   # Same as: x = x - 3
print(x)  # 12

x *= 2   # Same as: x = x * 2
print(x)  # 24

x /= 4   # Same as: x = x / 4
print(x)  # 6.0

x //= 2  # Same as: x = x // 2
print(x)  # 3.0

x %= 2   # Same as: x = x % 2
print(x)  # 1.0

x **= 3  # Same as: x = x ** 3
print(x)  # 1.0

# Multiple assignment
a, b, c = 1, 2, 3
print(a, b, c)  # 1 2 3

# Swap variables
a, b = b, a
print(a, b)  # 2 1

# Chain assignment
x = y = z = 0
print(x, y, z)  # 0 0 0
```

### Comparison Operators

These compare values and return boolean results:

```python
a = 10
b = 20

# Equality and inequality
print(a == b)   # False (equal to)
print(a != b)   # True (not equal to)

# Magnitude comparisons
print(a < b)    # True (less than)
print(a > b)    # False (greater than)
print(a <= 10)  # True (less than or equal to)
print(a >= 10)  # True (greater than or equal to)

# String comparisons (lexicographical order)
print("apple" < "banana")    # True
print("Apple" < "apple")     # True (uppercase comes first in ASCII)
print("10" < "9")           # True (string comparison, not numeric!)

# Comparing different types (be careful!)
print(5 == "5")             # False (different types)
print(5 == 5.0)             # True (numeric equality)

# Chained comparisons
age = 25
print(18 <= age < 65)       # True (elegant range check)
print(0 < a <= 10)          # True (same as: 0 < a and a <= 10)
```

### Logical Operators

These work with boolean values:

```python
# AND operator (both conditions must be True)
age = 25
has_license = True
print(age >= 18 and has_license)  # True

# OR operator (at least one condition must be True)
is_weekend = False
is_holiday = True
print(is_weekend or is_holiday)   # True

# NOT operator (reverses boolean value)
is_raining = False
print(not is_raining)             # True

# Complex logical expressions
temperature = 75
humidity = 60
is_sunny = True

comfortable = (temperature >= 70 and temperature <= 80 and 
               humidity < 70 and is_sunny)
print(f"Weather is comfortable: {comfortable}")

# Short-circuit evaluation
def expensive_operation():
    print("This is expensive!")
    return True

# First condition is False, so second function never runs
result = False and expensive_operation()
print(result)  # False (and "This is expensive!" is not printed)

# First condition is True, so second function never runs
result = True or expensive_operation()
print(result)  # True (and "This is expensive!" is not printed)
```

### Bitwise Operators

These work on binary representations of numbers:

```python
# Binary representations
a = 60   # 111100 in binary
b = 13   # 001101 in binary

# AND: both bits must be 1
print(a & b)    # 12 (001100 in binary)

# OR: at least one bit must be 1  
print(a | b)    # 61 (111101 in binary)

# XOR: exactly one bit must be 1
print(a ^ b)    # 49 (110001 in binary)

# NOT: flip all bits (returns -(x+1))
print(~a)       # -61

# Left shift: multiply by 2^n
print(a << 2)   # 240 (multiply by 2^2 = 4)

# Right shift: divide by 2^n
print(a >> 2)   # 15 (divide by 2^2 = 4)

# Practical use: checking if number is even (last bit is 0)
number = 42
if number & 1 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

### Identity Operators

These check if objects are the same in memory:

```python
# Two lists with same content but different objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2)   # True (same content)
print(list1 is list2)   # False (different objects)
print(list1 is list3)   # True (same object)

# Python optimizes small integers and some strings
a = 5
b = 5
print(a is b)           # True (Python reuses small integer objects)

a = 1000
b = 1000
print(a is b)           # May be False (depends on Python implementation)

# Always use 'is' with None
value = None
print(value is None)     # Correct way
print(value == None)     # Works but not recommended

# Check for singleton objects
print([] is [])         # False (different empty list objects)
print(None is None)     # True (None is a singleton)
```

### Membership Operators

These check if a value exists in a sequence:

```python
# Lists and tuples
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# Strings
sentence = "Python is awesome"
print("Python" in sentence)    # True
print("Java" not in sentence)  # True

# Dictionaries (checks keys, not values)
person = {"name": "Alice", "age": 30}
print("name" in person)        # True
print("Alice" in person)       # False (Alice is a value, not a key)
print("Alice" in person.values())  # True (check values explicitly)

# Sets
numbers = {1, 2, 3, 4, 5}
print(3 in numbers)            # True
print(6 not in numbers)        # True

# Ranges
print(5 in range(10))          # True
print(15 in range(10))         # False
```

### Operator Precedence (Order of Operations)

```python
# Precedence from highest to lowest:
# 1. () - Parentheses
# 2. ** - Exponentiation
# 3. +x, -x, ~x - Unary plus, minus, bitwise NOT
# 4. *, /, //, % - Multiplication, division, floor division, modulus
# 5. +, - - Addition, subtraction
# 6. <<, >> - Bitwise shifts
# 7. & - Bitwise AND
# 8. ^ - Bitwise XOR
# 9. | - Bitwise OR
# 10. ==, !=, <, <=, >, >=, is, is not, in, not in - Comparisons
# 11. not - Logical NOT
# 12. and - Logical AND
# 13. or - Logical OR

# Examples
result = 2 + 3 * 4
print(result)  # 14 (not 20: multiplication before addition)

result = 2 ** 3 ** 2
print(result)  # 512 (not 64: exponentiation is right-associative: 2^(3^2) = 2^9)

result = not False or True and False
print(result)  # True (not False = True, True and False = False, True or False = True)

# Use parentheses for clarity
result = (not False) or (True and False)
print(result)  # Same result, but much clearer

# Complex example
x, y, z = 5, 10, 15
result = x < y and y < z or x == z
print(result)  # True (and has higher precedence than or)

# Equivalent with explicit parentheses
result = (x < y and y < z) or (x == z)
print(result)  # Same result, clearer intention
```

### Ternary Operator (Conditional Expression)

Python's version of the ternary operator provides a concise way to choose between two values:

```python
# Basic syntax: value_if_true if condition else value_if_false
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # "adult"

# Traditional if-else equivalent
if age >= 18:
    status = "adult"
else:
    status = "minor"

# More examples
temperature = 75
clothing = "shorts" if temperature > 70 else "jacket"
print(f"Wear {clothing}")

# With function calls
def get_discount(is_member):
    return 0.10 if is_member else 0.0

discount = get_discount(True)
print(f"Discount: {discount * 100}%")

# Nested ternary (use sparingly!)
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Grade: {grade}")

# Better as regular if-elif-else for readability
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

### Practical Operator Examples

**1. Calculator Program:**
```python
def calculator(num1, operator, num2):
    """Simple calculator using operators"""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operator == "//":
        return num1 // num2 if num2 != 0 else "Error: Division by zero"
    elif operator == "%":
        return num1 % num2 if num2 != 0 else "Error: Division by zero"
    elif operator == "**":
        return num1 ** num2
    else:
        return "Error: Unknown operator"

# Test calculator
print(calculator(10, "+", 5))   # 15
print(calculator(10, "/", 3))   # 3.3333333333333335
print(calculator(10, "//", 3))  # 3
print(calculator(10, "%", 3))   # 1
print(calculator(2, "**", 8))   # 256
```

**2. Grade Calculator:**
```python
def calculate_grade(scores):
    """Calculate letter grade from numeric scores"""
    if not scores:
        return "No scores provided"
    
    average = sum(scores) / len(scores)
    
    # Using comparison operators and logical operators
    if average >= 97:
        letter = "A+"
    elif average >= 93:
        letter = "A"
    elif average >= 90:
        letter = "A-"
    elif average >= 87:
        letter = "B+"
    elif average >= 83:
        letter = "B"
    elif average >= 80:
        letter = "B-"
    elif average >= 77:
        letter = "C+"
    elif average >= 73:
        letter = "C"
    elif average >= 70:
        letter = "C-"
    elif average >= 67:
        letter = "D+"
    elif average >= 65:
        letter = "D"
    else:
        letter = "F"
    
    # Determine if passing (using ternary operator)
    passing = "PASS" if average >= 65 else "FAIL"
    
    return f"Average: {average:.1f}, Grade: {letter}, Status: {passing}"

# Test grade calculator
test_scores = [85, 92, 78, 88, 95]
result = calculate_grade(test_scores)
print(result)

# Test edge cases
print(calculate_grade([100, 100, 100]))  # Perfect scores
print(calculate_grade([50, 55, 60]))     # Failing scores
print(calculate_grade([]))               # No scores
```

**3. Access Control System:**
```python
def check_access(user_id, user_role, time_of_day, is_emergency=False):
    """
    Determine access level using multiple operators
    """
    # Define access rules using various operators
    is_admin = user_role == "admin"
    is_manager = user_role == "manager" 
    is_employee = user_role == "employee"
    
    # Business hours check (9 AM to 6 PM)
    is_business_hours = 9 <= time_of_day <= 18
    
    # Different access levels
    full_access = is_admin or (is_emergency and (is_manager or is_admin))
    
    limited_access = (is_employee and is_business_hours) or \
                    (is_manager and (is_business_hours or is_emergency))
    
    no_access = not (full_access or limited_access)
    
    # Determine access level using ternary operators
    access_level = "FULL" if full_access else \
                   "LIMITED" if limited_access else \
                   "DENIED"
    
    return {
        "user_id": user_id,
        "access_level": access_level,
        "can_access_admin": is_admin,
        "can_override_hours": is_admin or is_emergency,
        "timestamp": f"{time_of_day}:00"
    }

# Test access control
test_cases = [
    ("EMP001", "employee", 14, False),    # Employee during business hours
    ("EMP001", "employee", 20, False),    # Employee after hours
    ("MGR001", "manager", 20, True),      # Manager emergency access
    ("ADM001", "admin", 3, False),        # Admin anytime
]

for user_id, role, time, emergency in test_cases:
    result = check_access(user_id, role, time, emergency)
    print(f"User {user_id} ({role}) at {time}:00 {'(EMERGENCY)' if emergency else ''}")
    print(f"  Access: {result['access_level']}")
    print(f"  Admin privileges: {result['can_access_admin']}")
    print(f"  Can override hours: {result['can_override_hours']}")
    print()
```

This comprehensive coverage of Python operators gives you the tools to perform calculations, make comparisons, control program flow, and implement complex logic in your programs. Practice using these operators in different combinations to build more sophisticated programs!