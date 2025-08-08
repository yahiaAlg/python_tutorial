# Complete Python Tutorial for Beginners

## Table of Contents
1. [Python Booleans](#python-booleans)
2. [Python Operators](#python-operators)
3. [Python Lists](#python-lists)
4. [Python Tuples](#python-tuples)
5. [Python Sets](#python-sets)
6. [Python Dictionaries](#python-dictionaries)
7. [Python If...Else](#python-ifelse)
8. [Python Match](#python-match)
9. [Python While Loops](#python-while-loops)
10. [Python For Loops](#python-for-loops)
11. [Python Functions](#python-functions)
12. [Python Lambda](#python-lambda)
13. [Python Arrays](#python-arrays)

---

## Python Booleans

Boolean values are one of the fundamental data types in Python, representing truth values: `True` or `False`.

### Understanding Booleans

Booleans are used to represent logical values and are essential for decision-making in programs.

```python
# Boolean values
is_sunny = True
is_raining = False

print(is_sunny)    # Output: True
print(is_raining)  # Output: False
print(type(is_sunny))  # Output: <class 'bool'>
```

### Boolean Evaluation

Python can evaluate expressions and return Boolean values:

```python
# Comparison operations return Booleans
age = 18
print(age >= 18)  # Output: True
print(age < 16)   # Output: False

# String comparisons
name = "Alice"
print(name == "Alice")  # Output: True
print(name == "Bob")    # Output: False
```

### Truthy and Falsy Values

In Python, values can be evaluated as `True` or `False` in Boolean contexts:

**Falsy values (evaluate to False):**
- `False`
- `None`
- `0` (zero)
- `""` (empty string)
- `[]` (empty list)
- `{}` (empty dictionary)
- `()` (empty tuple)

```python
# Testing truthiness
print(bool(0))      # False
print(bool(""))     # False
print(bool([]))     # False
print(bool(None))   # False

# Truthy values
print(bool(1))      # True
print(bool("Hello")) # True
print(bool([1, 2]))  # True
```

---

## Python Operators

Operators are symbols that perform operations on variables and values.

### Arithmetic Operators

```python
a = 10
b = 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor division: 3
print(a % b)    # Modulus (remainder): 1
print(a ** b)   # Exponentiation: 1000
```

### Comparison Operators

```python
x = 5
y = 10

print(x == y)   # Equal to: False
print(x != y)   # Not equal to: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less than or equal: True
print(x >= y)   # Greater than or equal: False
```

### Logical Operators

```python
# and, or, not operators
a = True
b = False

print(a and b)  # False (both must be True)
print(a or b)   # True (at least one must be True)
print(not a)    # False (opposite of a)

# Practical example
age = 25
has_license = True
print(age >= 18 and has_license)  # True (can drive)
```

### Assignment Operators

```python
x = 10
x += 5   # Same as: x = x + 5
print(x)  # 15

x -= 3   # Same as: x = x - 3
print(x)  # 12

x *= 2   # Same as: x = x * 2
print(x)  # 24

x /= 4   # Same as: x = x / 4
print(x)  # 6.0
```

---

## Python Lists

Lists are ordered, mutable collections that can store multiple items of different data types.

### Creating Lists

```python
# Empty list
empty_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

print(fruits)   # ['apple', 'banana', 'orange']
print(numbers)  # [1, 2, 3, 4, 5]
```

### Accessing List Elements

```python
fruits = ["apple", "banana", "orange", "grape"]

# Positive indexing (starts from 0)
print(fruits[0])    # apple
print(fruits[1])    # banana

# Negative indexing (starts from -1)
print(fruits[-1])   # grape (last item)
print(fruits[-2])   # orange (second to last)
```

### List Slicing

```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:5])    # [2, 3, 4] (from index 2 to 4)
print(numbers[:3])     # [0, 1, 2] (from start to index 2)
print(numbers[5:])     # [5, 6, 7, 8, 9] (from index 5 to end)
print(numbers[::2])    # [0, 2, 4, 6, 8] (every 2nd element)
print(numbers[::-1])   # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (reversed)
```

### Modifying Lists

```python
fruits = ["apple", "banana", "orange"]

# Changing items
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'orange']

# Adding items
fruits.append("grape")         # Add to end
print(fruits)  # ['apple', 'mango', 'orange', 'grape']

fruits.insert(1, "kiwi")       # Insert at specific position
print(fruits)  # ['apple', 'kiwi', 'mango', 'orange', 'grape']

# Removing items
fruits.remove("mango")         # Remove specific item
print(fruits)  # ['apple', 'kiwi', 'orange', 'grape']

popped = fruits.pop()          # Remove and return last item
print(popped)  # grape
print(fruits)  # ['apple', 'kiwi', 'orange']

del fruits[0]                  # Delete by index
print(fruits)  # ['kiwi', 'orange']
```

### Useful List Methods

```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))        # Length: 8
print(numbers.count(1))    # Count occurrences of 1: 2
print(numbers.index(4))    # Find index of first occurrence of 4: 2

numbers.sort()             # Sort in place
print(numbers)  # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.reverse()          # Reverse in place
print(numbers)  # [9, 6, 5, 4, 3, 2, 1, 1]

# List comprehension (advanced)
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
```

---

## Python Tuples

Tuples are ordered, immutable collections similar to lists but cannot be changed after creation.

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()

# Tuple with items
coordinates = (3, 5)
colors = ("red", "green", "blue")
mixed = ("hello", 42, True)

# Single item tuple (note the comma)
single = (5,)  # or single = 5,

print(coordinates)  # (3, 5)
print(type(coordinates))  # <class 'tuple'>
```

### Accessing Tuple Elements

```python
point = (10, 20, 30)

print(point[0])    # 10
print(point[-1])   # 30 (last element)

# Unpacking tuples
x, y, z = point
print(f"x={x}, y={y}, z={z}")  # x=10, y=20, z=30

# Partial unpacking with *
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print(first)   # 1
print(second)  # 2
print(rest)    # [3, 4, 5]
```

### Tuple Methods and Operations

```python
numbers = (1, 2, 3, 2, 4, 2)

print(len(numbers))        # Length: 6
print(numbers.count(2))    # Count occurrences: 3
print(numbers.index(3))    # Find index: 2

# Tuples are immutable
# numbers[0] = 10  # This would cause an error!

# But you can create new tuples
new_numbers = numbers + (5, 6)
print(new_numbers)  # (1, 2, 3, 2, 4, 2, 5, 6)
```

### When to Use Tuples vs Lists

Use tuples when:
- Data shouldn't change (coordinates, RGB values, etc.)
- You need a hashable type (for dictionary keys)
- Returning multiple values from functions

```python
def get_name_age():
    return "Alice", 25

name, age = get_name_age()
print(f"{name} is {age} years old")
```

---

## Python Sets

Sets are unordered collections of unique elements.

### Creating Sets

```python
# Empty set
empty_set = set()  # Note: {} creates an empty dictionary!

# Set with items
fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# From a list (removes duplicates)
list_with_dupes = [1, 2, 2, 3, 3, 3, 4]
unique_numbers = set(list_with_dupes)
print(unique_numbers)  # {1, 2, 3, 4}
```

### Set Operations

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all unique elements)
print(set1 | set2)        # {1, 2, 3, 4, 5, 6}
print(set1.union(set2))   # Same as above

# Intersection (common elements)
print(set1 & set2)               # {3, 4}
print(set1.intersection(set2))   # Same as above

# Difference
print(set1 - set2)               # {1, 2}
print(set1.difference(set2))     # Same as above

# Symmetric difference (elements in either set, but not both)
print(set1 ^ set2)                        # {1, 2, 5, 6}
print(set1.symmetric_difference(set2))    # Same as above
```

### Modifying Sets

```python
fruits = {"apple", "banana"}

# Adding elements
fruits.add("orange")
print(fruits)  # {'apple', 'banana', 'orange'}

fruits.update(["grape", "kiwi"])
print(fruits)  # {'apple', 'banana', 'orange', 'grape', 'kiwi'}

# Removing elements
fruits.remove("banana")  # Raises error if not found
print(fruits)

fruits.discard("mango")  # No error if not found

# Pop removes and returns arbitrary element
popped = fruits.pop()
print(f"Removed: {popped}")
```

### Set Membership and Methods

```python
colors = {"red", "green", "blue"}

print("red" in colors)      # True
print("yellow" in colors)   # False
print(len(colors))          # 3

# Check relationships
set_a = {1, 2}
set_b = {1, 2, 3, 4}

print(set_a.issubset(set_b))    # True
print(set_b.issuperset(set_a))  # True
print(set_a.isdisjoint({5, 6})) # True (no common elements)
```

---

## Python Dictionaries

Dictionaries store data in key-value pairs and are unordered, mutable collections.

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}

# Dictionary with items
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using dict() constructor
grades = dict(math=95, english=87, science=92)

print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(grades)  # {'math': 95, 'english': 87, 'science': 92}
```

### Accessing Dictionary Values

```python
person = {"name": "Bob", "age": 25, "occupation": "Engineer"}

# Access by key
print(person["name"])        # Bob
print(person.get("age"))     # 25

# get() method with default
print(person.get("salary", "Not specified"))  # Not specified

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'occupation'])
print(person.values())  # dict_values(['Bob', 25, 'Engineer'])
print(person.items())   # dict_items([('name', 'Bob'), ('age', 25), ('occupation', 'Engineer')])
```

### Modifying Dictionaries

```python
student = {"name": "Charlie", "grade": "A"}

# Adding/updating items
student["age"] = 20
student["grade"] = "A+"
print(student)  # {'name': 'Charlie', 'grade': 'A+', 'age': 20}

# Update with another dictionary
student.update({"school": "MIT", "year": 2})
print(student)

# Removing items
del student["year"]           # Remove specific key
popped = student.pop("age")   # Remove and return value
print(f"Removed age: {popped}")

# Clear all items
# student.clear()  # Would empty the dictionary
```

### Dictionary Methods and Operations

```python
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

# Check if key exists
print("apples" in inventory)     # True
print("grapes" in inventory)     # False

# Get copy of dictionary
inventory_copy = inventory.copy()

# Dictionary comprehension
squared = {x: x**2 for x in range(5)}
print(squared)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested dictionaries
students = {
    "Alice": {"math": 95, "english": 87},
    "Bob": {"math": 88, "english": 92}
}
print(students["Alice"]["math"])  # 95
```

---

## Python If...Else

Conditional statements allow your program to make decisions and execute different code based on conditions.

### Basic If Statement

```python
age = 18

if age >= 18:
    print("You are an adult")
    print("You can vote")

# Output: You are an adult
#         You can vote
```

### If...Else Statement

```python
temperature = 25

if temperature > 30:
    print("It's hot outside")
else:
    print("It's not too hot")

# Output: It's not too hot
```

### If...Elif...Else Statement

```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")  # Your grade is: B
```

### Nested If Statements

```python
age = 20
has_license = True

if age >= 18:
    print("You are an adult")
    if has_license:
        print("You can drive")
    else:
        print("You need a driver's license")
else:
    print("You are too young to drive")
```

### Complex Conditions

```python
username = "admin"
password = "secret123"
is_logged_in = False

# Multiple conditions with and/or
if username == "admin" and password == "secret123":
    is_logged_in = True
    print("Login successful")
else:
    print("Invalid credentials")

# Using 'in' operator
valid_users = ["admin", "user1", "user2"]
if username in valid_users:
    print("Valid username")

# Ternary operator (conditional expression)
status = "Adult" if age >= 18 else "Minor"
print(status)
```

### Checking Multiple Values

```python
day = "Saturday"

# Multiple conditions
if day == "Saturday" or day == "Sunday":
    print("It's weekend!")

# Using 'in' with tuple/list
if day in ("Saturday", "Sunday"):
    print("It's weekend!")

# Check if value is not something
if day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday"):
    print("Not a weekday")
```

---

## Python Match

The match statement (introduced in Python 3.10) provides pattern matching similar to switch statements in other languages.

### Basic Match Statement

```python
def describe_animal(animal):
    match animal:
        case "cat":
            return "Meows and purrs"
        case "dog":
            return "Barks and wags tail"
        case "bird":
            return "Flies and sings"
        case _:  # Default case
            return "Unknown animal"

print(describe_animal("cat"))  # Meows and purrs
print(describe_animal("fish")) # Unknown animal
```

### Match with Multiple Values

```python
def get_season(month):
    match month:
        case "December" | "January" | "February":
            return "Winter"
        case "March" | "April" | "May":
            return "Spring"
        case "June" | "July" | "August":
            return "Summer"
        case "September" | "October" | "November":
            return "Fall"
        case _:
            return "Invalid month"

print(get_season("July"))  # Summer
```

### Match with Conditions (Guards)

```python
def categorize_number(x):
    match x:
        case n if n < 0:
            return "Negative"
        case 0:
            return "Zero"
        case n if n > 0 and n <= 10:
            return "Small positive"
        case n if n > 10:
            return "Large positive"

print(categorize_number(-5))   # Negative
print(categorize_number(7))    # Small positive
print(categorize_number(15))   # Large positive
```

### Match with Data Structures

```python
def analyze_data(data):
    match data:
        case []:
            return "Empty list"
        case [x]:
            return f"List with one item: {x}"
        case [x, y]:
            return f"List with two items: {x}, {y}"
        case [x, y, *rest]:
            return f"List starting with {x}, {y} and {len(rest)} more items"
        case {"name": name, "age": age}:
            return f"Person: {name}, age {age}"
        case _:
            return "Unknown data structure"

print(analyze_data([1, 2, 3, 4]))  # List starting with 1, 2 and 2 more items
print(analyze_data({"name": "Alice", "age": 30}))  # Person: Alice, age 30
```

---

## Python While Loops

While loops execute a block of code repeatedly as long as a condition is true.

### Basic While Loop

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# Output:
# Count: 0
# Count: 1
# Count: 2
# Count: 3
# Count: 4
```

### User Input with While Loop

```python
# Keep asking until user enters 'quit'
while True:
    user_input = input("Enter a command (or 'quit' to exit): ")
    if user_input.lower() == 'quit':
        break
    print(f"You entered: {user_input}")

print("Goodbye!")
```

### While Loop with Else

```python
# The else block runs if the loop completes normally (no break)
search_list = [1, 3, 5, 7, 9]
target = 4
index = 0

while index < len(search_list):
    if search_list[index] == target:
        print(f"Found {target} at index {index}")
        break
    index += 1
else:
    print(f"{target} not found in the list")

# Output: 4 not found in the list
```

### Common While Loop Patterns

```python
# Countdown
countdown = 10
while countdown > 0:
    print(countdown)
    countdown -= 1
print("Blast off!")

# Processing items from a list
tasks = ["task1", "task2", "task3"]
while tasks:
    current_task = tasks.pop(0)  # Remove first item
    print(f"Processing: {current_task}")

# Accumulation
numbers = [1, 2, 3, 4, 5]
total = 0
i = 0
while i < len(numbers):
    total += numbers[i]
    i += 1
print(f"Sum: {total}")  # Sum: 15
```

### Continue and Break

```python
# Skip even numbers, stop at 15
num = 0
while num < 20:
    num += 1
    if num % 2 == 0:
        continue  # Skip rest of loop iteration
    if num > 15:
        break     # Exit loop completely
    print(num)

# Output: 1, 3, 5, 7, 9, 11, 13, 15
```

---

## Python For Loops

For loops iterate over sequences (lists, tuples, strings, etc.) or other iterable objects.

### Basic For Loop

```python
# Iterate over a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Output:
# I like apple
# I like banana
# I like orange
```

### For Loop with Range

```python
# range(stop)
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop)
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

### Iterating Over Different Data Types

```python
# String
for char in "Hello":
    print(char)  # H, e, l, l, o

# Dictionary
person = {"name": "Alice", "age": 30, "city": "NYC"}

# Keys only
for key in person:
    print(key)

# Keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# Values only
for value in person.values():
    print(value)

# Tuple
coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)
```

### Enumerate and Zip

```python
# enumerate() adds index to iteration
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# zip() combines multiple iterables
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")
```

### For Loop with Else

```python
# else block runs if loop completes normally (no break)
numbers = [1, 3, 5, 7, 9]
target = 4

for num in numbers:
    if num == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")
# Output: 4 not found
```

### List Comprehensions

```python
# Create new lists using for loops in a compact way
numbers = [1, 2, 3, 4, 5]

# Traditional approach
squares = []
for num in numbers:
    squares.append(num ** 2)

# List comprehension
squares = [num ** 2 for num in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# With condition
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print(even_squares)  # [4, 16]

# Dictionary comprehension
square_dict = {num: num ** 2 for num in numbers}
print(square_dict)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

### Nested For Loops

```python
# Multiplication table
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print()  # Empty line after each row

# Working with 2D lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
```

---

## Python Functions

Functions are reusable blocks of code that perform specific tasks.

### Defining and Calling Functions

```python
# Simple function
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")  # Output: Hello, Alice!

# Function with multiple parameters
def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(5, 3)  # Output: 5 + 3 = 8
```

### Return Values

```python
# Function that returns a value
def multiply(x, y):
    return x * y

result = multiply(4, 5)
print(result)  # 20

# Function returning multiple values
def get_name_and_age():
    name = "Bob"
    age = 30
    return name, age

person_name, person_age = get_name_and_age()
print(f"Name: {person_name}, Age: {person_age}")

# Function with conditional return
def absolute_value(number):
    if number >= 0:
        return number
    else:
        return -number

print(absolute_value(-5))  # 5
print(absolute_value(3))   # 3
```

### Default Parameters

```python
def introduce(name, age=25, city="Unknown"):
    print(f"Hi, I'm {name}, {age} years old, from {city}")

# Using all defaults
introduce("Alice")  # Hi, I'm Alice, 25 years old, from Unknown

# Overriding some defaults
introduce("Bob", 30)  # Hi, I'm Bob, 30 years old, from Unknown
introduce("Charlie", city="Paris")  # Hi, I'm Charlie, 25 years old, from Paris

# Overriding all
introduce("Diana", 28, "London")  # Hi, I'm Diana, 28 years old, from London
```

### Variable-Length Arguments

```python
# *args for variable positional arguments
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs for variable keyword arguments
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC

# Combining different parameter types
def complex_function(required, default_param="default", *args, **kwargs):
    print(f"Required: {required}")
    print(f"Default: {default_param}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

complex_function("hello", "world", 1, 2, 3, name="Alice", age=30)
```

### Local vs Global Scope

```python
# Global variable
global_var = "I'm global"

def my_function():
    # Local variable
    local_var = "I'm local"
    print(global_var)  # Can access global
    print(local_var)   # Can access local

my_function()
# print(local_var)  # This would cause an error!

# Modifying global variables
counter = 0

def increment():
    global counter
    counter += 1

print(counter)  # 0
increment()
print(counter)  # 1
```

### Docstrings and Documentation

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    
    Returns:
        float: The area of the rectangle
    
    Example:
        >>> calculate_area(5, 3)
        15
    """
    return length * width

# Access docstring
print(calculate_area.__doc__)

# Better example with error handling
def divide(a, b):
    """
    Divide two numbers safely.
    
    Args:
        a (float): The dividend
        b (float): The divisor
    
    Returns:
        float: The result of a/b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
```

---

## Python Lambda

Lambda functions are small, anonymous functions that can have any number of arguments but can only have one expression.

### Basic Lambda Functions

```python
# Regular function
def square(x):
    return x ** 2

# Equivalent lambda function
square_lambda = lambda x: x ** 2

print(square(5))        # 25
print(square_lambda(5)) # 25

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(multiply(3, 4))   # 12

# Lambda with default parameters
greet = lambda name, greeting="Hello": f"{greeting}, {name}!"
print(greet("Alice"))           # Hello, Alice!
print(greet("Bob", "Hi"))       # Hi, Bob!
```

### Lambda with Built-in Functions

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using lambda with filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4, 6, 8, 10]

# Using lambda with map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Using lambda with reduce() (need to import from functools)
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(product)  # 120 (1*2*3*4*5)

# Using lambda with sorted()
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78), ('Diana', 92)]
# Sort by grade (second element)
sorted_by_grade = sorted(students, key=lambda student: student[1])
print(sorted_by_grade)  # [('Charlie', 78), ('Alice', 85), ('Bob', 90), ('Diana', 92)]
```

### Lambda in Data Processing

```python
# Working with dictionaries
people = [
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 80000}
]

# Filter people with high salary
high_earners = list(filter(lambda person: person['salary'] > 60000, people))
print(high_earners)

# Get list of names
names = list(map(lambda person: person['name'], people))
print(names)  # ['Alice', 'Bob', 'Charlie']

# Sort by age
sorted_by_age = sorted(people, key=lambda person: person['age'])
print(sorted_by_age)

# Lambda with list comprehension alternative
# Lambda approach
squared_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
# List comprehension approach (more Pythonic)
squared_evens_comp = [x**2 for x in numbers if x % 2 == 0]
print(squared_evens)      # [4, 16, 36, 64, 100]
print(squared_evens_comp) # [4, 16, 36, 64, 100]
```

### When to Use Lambda vs Regular Functions

```python
# Good use of lambda: simple, one-line operations
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])  # Sort by string

# Bad use of lambda: complex logic
# Don't do this:
# complex_lambda = lambda x: x**2 if x > 0 else abs(x) if x < 0 else 0

# Do this instead:
def complex_function(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return abs(x)
    else:
        return 0

# Lambda functions cannot contain statements (only expressions)
# This won't work:
# invalid_lambda = lambda x: print(x)  # print is a statement

# But this works:
valid_lambda = lambda x: x if x > 0 else 0
```

---

## Python Arrays

While Python has built-in lists, arrays refer to more specialized data structures. We'll cover both NumPy arrays and Python's array module.

### Python's Built-in Array Module

```python
import array

# Create typed arrays (more memory efficient than lists)
# 'i' = signed integer, 'f' = float, 'd' = double
int_array = array.array('i', [1, 2, 3, 4, 5])
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4])

print(int_array)    # array('i', [1, 2, 3, 4, 5])
print(float_array)  # array('f', [1.1, 2.2, 3.3, 4.4])

# Array operations
int_array.append(6)
print(int_array)    # array('i', [1, 2, 3, 4, 5, 6])

int_array.extend([7, 8, 9])
print(int_array)    # array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9])

# Convert to list
as_list = int_array.tolist()
print(as_list)      # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Working with Lists as Arrays

```python
# 1D Array (List)
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])   # 1 (first element)
print(numbers[-1])  # 5 (last element)

# Slicing
print(numbers[1:4]) # [2, 3, 4]
print(numbers[::2]) # [1, 3, 5] (every 2nd element)

# 2D Array (List of Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in 2D array
print(matrix[0])    # [1, 2, 3] (first row)
print(matrix[1][2]) # 6 (row 1, column 2)

# Iterating through 2D array
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
```

### Array-like Operations with Lists

```python
# Mathematical operations (element-wise would require loops)
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Element-wise addition (manual)
result = []
for i in range(len(list1)):
    result.append(list1[i] + list2[i])
print(result)  # [6, 8, 10, 12]

# Using list comprehension
result_comp = [a + b for a, b in zip(list1, list2)]
print(result_comp)  # [6, 8, 10, 12]

# Finding max, min, sum
numbers = [3, 7, 2, 9, 1, 5, 8]
print(f"Max: {max(numbers)}")    # Max: 9
print(f"Min: {min(numbers)}")    # Min: 1
print(f"Sum: {sum(numbers)}")    # Sum: 35
print(f"Length: {len(numbers)}") # Length: 7

# Sorting
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 3, 5, 7, 8, 9]

# Reversing
reversed_numbers = numbers[::-1]
print(reversed_numbers)  # [8, 5, 1, 9, 2, 7, 3]
```

### Creating and Manipulating Multi-dimensional Arrays

```python
# Creating a 3x3 matrix with list comprehension
matrix_3x3 = [[0 for _ in range(3)] for _ in range(3)]
print(matrix_3x3)  # [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Filling with values
for i in range(3):
    for j in range(3):
        matrix_3x3[i][j] = i * 3 + j + 1

print(matrix_3x3)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Matrix operations (basic)
def matrix_add(matrix1, matrix2):
    """Add two matrices of the same size"""
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

matrix_a = [[1, 2], [3, 4]]
matrix_b = [[5, 6], [7, 8]]
sum_matrix = matrix_add(matrix_a, matrix_b)
print(sum_matrix)  # [[6, 8], [10, 12]]

# Transpose a matrix
def transpose(matrix):
    """Transpose a matrix"""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

original = [[1, 2, 3], [4, 5, 6]]
transposed = transpose(original)
print(f"Original: {original}")     # [[1, 2, 3], [4, 5, 6]]
print(f"Transposed: {transposed}") # [[1, 4], [2, 5], [3, 6]]
```

### Array Search and Manipulation

```python
# Searching in arrays
def linear_search(arr, target):
    """Find the index of target in array, return -1 if not found"""
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers = [3, 7, 2, 9, 1, 5, 8]
print(linear_search(numbers, 9))  # 3
print(linear_search(numbers, 4))  # -1

# Binary search (array must be sorted)
def binary_search(arr, target):
    """Binary search in sorted array"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_numbers = [1, 2, 3, 5, 7, 8, 9]
print(binary_search(sorted_numbers, 5))  # 3
print(binary_search(sorted_numbers, 4))  # -1

# Array manipulation functions
def rotate_array(arr, k):
    """Rotate array to the right by k positions"""
    n = len(arr)
    k = k % n  # Handle k > n
    return arr[-k:] + arr[:-k]

numbers = [1, 2, 3, 4, 5]
rotated = rotate_array(numbers, 2)
print(rotated)  # [4, 5, 1, 2, 3]

def remove_duplicates(arr):
    """Remove duplicates while preserving order"""
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

with_dupes = [1, 2, 2, 3, 3, 3, 4, 5, 5]
unique = remove_duplicates(with_dupes)
print(unique)  # [1, 2, 3, 4, 5]
```

---

## Practical Examples and Exercises

### Example 1: Student Grade Calculator

```python
def calculate_grade_statistics():
    """Calculate and display student grade statistics"""
    students = []
    
    # Input student data
    while True:
        name = input("Enter student name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        
        try:
            grade = float(input(f"Enter {name}'s grade: "))
            students.append({"name": name, "grade": grade})
        except ValueError:
            print("Please enter a valid number for the grade.")
    
    if not students:
        print("No students entered.")
        return
    
    # Calculate statistics
    grades = [student["grade"] for student in students]
    average = sum(grades) / len(grades)
    highest = max(grades)
    lowest = min(grades)
    
    # Display results
    print(f"\nClass Statistics:")
    print(f"Number of students: {len(students)}")
    print(f"Average grade: {average:.2f}")
    print(f"Highest grade: {highest}")
    print(f"Lowest grade: {lowest}")
    
    # Grade distribution
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}
    for grade in grades:
        if grade >= 90:
            grade_counts["A"] += 1
        elif grade >= 80:
            grade_counts["B"] += 1
        elif grade >= 70:
            grade_counts["C"] += 1
        elif grade >= 60:
            grade_counts["D"] += 1
        else:
            grade_counts["F"] += 1
    
    print(f"\nGrade Distribution:")
    for letter, count in grade_counts.items():
        print(f"{letter}: {count} students")

# Uncomment to run:
# calculate_grade_statistics()
```

### Example 2: Simple To-Do List Manager

```python
def todo_manager():
    """Simple command-line to-do list manager"""
    todos = []
    
    def show_menu():
        print("\n=== TO-DO LIST MANAGER ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Complete task")
        print("4. Remove task")
        print("5. Exit")
    
    def view_tasks():
        if not todos:
            print("No tasks in your list!")
            return
        
        print("\nYour tasks:")
        for i, task in enumerate(todos, 1):
            status = "✓" if task["completed"] else "○"
            print(f"{i}. {status} {task['description']}")
    
    def add_task():
        description = input("Enter task description: ").strip()
        if description:
            todos.append({"description": description, "completed": False})
            print(f"Added task: {description}")
        else:
            print("Task description cannot be empty!")
    
    def complete_task():
        view_tasks()
        if not todos:
            return
        
        try:
            task_num = int(input("Enter task number to complete: "))
            if 1 <= task_num <= len(todos):
                todos[task_num - 1]["completed"] = True
                print(f"Completed task: {todos[task_num - 1]['description']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    def remove_task():
        view_tasks()
        if not todos:
            return
        
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(todos):
                removed = todos.pop(task_num - 1)
                print(f"Removed task: {removed['description']}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")
    
    # Main loop
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option! Please choose 1-5.")

# Uncomment to run:
# todo_manager()
```

### Practice Exercises

Try these exercises to reinforce your learning:

1. **Number Guessing Game**: Create a game where the computer picks a random number and the user has to guess it.

2. **Word Counter**: Write a function that counts the frequency of words in a text string.

3. **Password Validator**: Create a function that checks if a password meets certain criteria (length, uppercase, lowercase, numbers, special characters).

4. **Simple Calculator**: Build a calculator that can perform basic arithmetic operations with error handling.

5. **List Manipulation**: Create functions to find the second largest number in a list, rotate a list, and merge two sorted lists.

---

## Summary

This tutorial covered the essential Python concepts:

- **Booleans**: Truth values and logical operations
- **Operators**: Arithmetic, comparison, logical, and assignment operators  
- **Lists**: Ordered, mutable collections with extensive methods
- **Tuples**: Ordered, immutable collections for fixed data
- **Sets**: Unordered collections of unique elements with set operations
- **Dictionaries**: Key-value pairs for mapping relationships
- **Conditionals**: If/elif/else and match statements for decision making
- **Loops**: While loops for condition-based iteration and for loops for sequence iteration
- **Functions**: Reusable code blocks with parameters, return values, and scope
- **Lambda**: Anonymous functions for simple operations
- **Arrays**: Working with array-like structures using lists and the array module

Each concept builds upon the previous ones, creating a solid foundation for Python programming. Practice with real projects and continue exploring Python's extensive standard library and ecosystem!