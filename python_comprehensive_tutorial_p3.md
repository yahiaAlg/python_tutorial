# Complete Python Tutorial: From Basics to File Handling

## Table of Contents
1. [Python User Input](#python-user-input)
2. [Python String Formatting](#python-string-formatting)
3. [Python Math](#python-math)
4. [Python Dates](#python-dates)
5. [Python Modules](#python-modules)
6. [Python JSON](#python-json)
7. [Python RegEx](#python-regex)
8. [Python PIP](#python-pip)
9. [Python Try...Except](#python-tryexcept)
10. [Python VirtualEnv](#python-virtualenv)
11. [File Handling](#file-handling)
    - [Python File Handling](#python-file-handling)
    - [Python Read Files](#python-read-files)
    - [Python Write/Create Files](#python-writecreate-files)
    - [Python Delete Files](#python-delete-files)

---

## Python User Input

User input is how your program communicates with people. Think of it as asking questions and waiting for answers.

### Basic Input

```python
# Getting input from user
name = input("What's your name? ")
print(f"Hello, {name}!")
```

The `input()` function always returns a **string**, even if the user types numbers.

### Converting Input Types

```python
# Getting a number - need to convert from string
age_str = input("How old are you? ")
age = int(age_str)  # Convert string to integer

# Or do it in one line
age = int(input("How old are you? "))

# For decimal numbers
height = float(input("What's your height in meters? "))
```

### Handling Multiple Inputs

```python
# Getting multiple values
first_name = input("First name: ")
last_name = input("Last name: ")
full_name = first_name + " " + last_name

# Creating a simple calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print(f"The sum is: {result}")
```

**Key Points:**
- Always assume user input is a string initially
- Convert to appropriate type when needed
- Always validate input in real applications

---

## Python String Formatting

String formatting is like creating templates for text where you can insert variables.

### Old Style Formatting (% operator)

```python
name = "Alice"
age = 25
print("My name is %s and I am %d years old" % (name, age))
```

### .format() Method

```python
name = "Bob"
age = 30
# Positional arguments
print("My name is {} and I am {} years old".format(name, age))

# Named arguments
print("My name is {name} and I am {age} years old".format(name=name, age=age))

# With formatting options
price = 49.95
print("The price is ${:.2f}".format(price))  # 2 decimal places
```

### f-strings (Modern and Preferred)

```python
name = "Charlie"
age = 35
score = 87.6789

# Basic f-string
print(f"My name is {name} and I am {age} years old")

# With expressions
print(f"Next year I'll be {age + 1}")

# With formatting
print(f"My score is {score:.2f}")  # 2 decimal places
print(f"My score is {score:.1%}")  # As percentage

# Alignment and padding
print(f"{'Left':<10}|{'Center':^10}|{'Right':>10}")
```

### Advanced Formatting

```python
# Numbers
number = 1234567
print(f"{number:,}")        # 1,234,567 (comma separator)
print(f"{number:_}")        # 1_234_567 (underscore separator)

# Dates in f-strings
from datetime import datetime
now = datetime.now()
print(f"Today is {now:%Y-%m-%d}")
print(f"Time is {now:%H:%M:%S}")
```

**When to use what:**
- Use f-strings for modern Python (3.6+) - they're fastest and most readable
- Use .format() for Python versions before 3.6
- Avoid % formatting unless maintaining old code

---

## Python Math

Python provides powerful mathematical capabilities both built-in and through the math module.

### Basic Arithmetic

```python
# Basic operations
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")         # Float division
print(f"Floor Division: {a} // {b} = {a // b}") # Integer division
print(f"Modulo: {a} % {b} = {a % b}")           # Remainder
print(f"Exponentiation: {a} ** {b} = {a ** b}") # Power
```

### Built-in Math Functions

```python
# Built-in functions
numbers = [-5, 3.7, -2.1, 8, 0]

print(f"Absolute value of -5: {abs(-5)}")
print(f"Maximum: {max(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Rounded 3.7: {round(3.7)}")
print(f"Rounded 3.7 to 1 decimal: {round(3.7, 1)}")
```

### The Math Module

```python
import math

# Constants
print(f"Pi: {math.pi}")
print(f"E: {math.e}")

# Trigonometry (angles in radians)
angle = math.pi / 4  # 45 degrees
print(f"sin(45°): {math.sin(angle):.4f}")
print(f"cos(45°): {math.cos(angle):.4f}")
print(f"tan(45°): {math.tan(angle):.4f}")

# Convert degrees to radians and vice versa
degrees = 45
radians = math.radians(degrees)
back_to_degrees = math.degrees(radians)
print(f"{degrees}° = {radians:.4f} radians")

# Logarithms
print(f"Natural log of e: {math.log(math.e)}")
print(f"Log base 10 of 100: {math.log10(100)}")
print(f"Log base 2 of 8: {math.log2(8)}")

# Powers and roots
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Cube root of 27: {math.pow(27, 1/3):.1f}")
print(f"2 to the power of 3: {math.pow(2, 3)}")

# Ceiling and floor
print(f"Ceiling of 3.2: {math.ceil(3.2)}")
print(f"Floor of 3.8: {math.floor(3.8)}")

# Factorial
print(f"5! = {math.factorial(5)}")
```

### Practical Examples

```python
import math

# Calculate distance between two points
def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate circle area and circumference
def circle_calculations(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference

# Example usage
point1 = (0, 0)
point2 = (3, 4)
dist = distance(*point1, *point2)
print(f"Distance between {point1} and {point2}: {dist}")

area, circumference = circle_calculations(5)
print(f"Circle with radius 5: Area = {area:.2f}, Circumference = {circumference:.2f}")
```

---

## Python Dates

Working with dates and times is essential for many applications.

### Basic Date and Time

```python
from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Just the date: {now.date()}")
print(f"Just the time: {now.time()}")

# Current date only
today = date.today()
print(f"Today's date: {today}")
```

### Creating Specific Dates

```python
from datetime import datetime, date

# Create specific dates
birthday = date(1990, 5, 15)  # Year, month, day
print(f"Birthday: {birthday}")

# Create specific datetime
meeting = datetime(2024, 12, 25, 14, 30, 0)  # Year, month, day, hour, minute, second
print(f"Meeting: {meeting}")
```

### Formatting Dates

```python
from datetime import datetime

now = datetime.now()

# Common formats
print(f"ISO format: {now.isoformat()}")
print(f"String representation: {str(now)}")

# Custom formatting with strftime
print(f"Readable: {now.strftime('%B %d, %Y')}")           # December 25, 2024
print(f"Short: {now.strftime('%m/%d/%Y')}")                # 12/25/2024
print(f"With time: {now.strftime('%Y-%m-%d %H:%M:%S')}")   # 2024-12-25 14:30:45
print(f"Day of week: {now.strftime('%A')}")                # Monday
print(f"Month name: {now.strftime('%B')}")                 # December

# Common format codes:
# %Y - 4-digit year    %y - 2-digit year
# %m - Month number    %B - Full month name    %b - Short month name
# %d - Day of month    %A - Full day name      %a - Short day name
# %H - Hour (24)       %I - Hour (12)          %p - AM/PM
# %M - Minute          %S - Second
```

### Parsing Dates from Strings

```python
from datetime import datetime

# Parse date from string
date_string = "2024-12-25 14:30:00"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed date: {parsed_date}")

# Different format
date_string2 = "December 25, 2024"
parsed_date2 = datetime.strptime(date_string2, "%B %d, %Y")
print(f"Parsed date 2: {parsed_date2}")
```

### Date Arithmetic

```python
from datetime import datetime, timedelta

now = datetime.now()

# Add/subtract time
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

print(f"Now: {now}")
print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")
print(f"In 2 hours: {in_2_hours}")

# Calculate difference between dates
birthday = datetime(1990, 5, 15)
age = now - birthday
print(f"Age in days: {age.days}")
print(f"Age in years: {age.days // 365}")
```

### Practical Examples

```python
from datetime import datetime, timedelta

# Age calculator
def calculate_age(birth_date):
    today = datetime.now().date()
    age = today - birth_date
    return age.days // 365

# Days until event
def days_until(event_date):
    today = datetime.now().date()
    if event_date > today:
        return (event_date - today).days
    else:
        return 0

# Working days calculator (simple version)
def working_days_between(start_date, end_date):
    current = start_date
    count = 0
    while current <= end_date:
        if current.weekday() < 5:  # Monday = 0, Friday = 4
            count += 1
        current += timedelta(days=1)
    return count

# Example usage
birth_date = date(1990, 5, 15)
age = calculate_age(birth_date)
print(f"Age: {age} years")

event_date = date(2024, 12, 25)
days = days_until(event_date)
print(f"Days until event: {days}")
```

---

## Python Modules

Modules are like toolboxes - they contain functions and variables you can use in your programs.

### What is a Module?

A module is simply a Python file containing code. You can import and use this code in other files.

### Built-in Modules

```python
# Different ways to import
import math
print(math.sqrt(16))

# Import specific functions
from math import sqrt, pi
print(sqrt(16))
print(pi)

# Import with alias
import math as m
print(m.sqrt(16))

# Import all (generally not recommended)
from math import *
print(sqrt(16))  # Can use directly, but can cause name conflicts
```

### Common Built-in Modules

```python
# Random module
import random

print(random.randint(1, 10))      # Random integer between 1 and 10
print(random.random())            # Random float between 0 and 1
print(random.choice(['a', 'b', 'c']))  # Random choice from list

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)           # Shuffle list in place
print(numbers)

# OS module - interact with operating system
import os

print(os.getcwd())                # Current working directory
print(os.listdir('.'))            # List files in current directory

# Platform module - system information
import platform

print(platform.system())          # Operating system
print(platform.python_version())  # Python version
```

### Creating Your Own Module

Create a file called `my_module.py`:

```python
# my_module.py
def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

PI = 3.14159

class Calculator:
    def multiply(self, a, b):
        return a * b
```

Using your module in another file:

```python
# main.py
import my_module

# Use functions from the module
print(my_module.greet("Alice"))
result = my_module.add_numbers(5, 3)
print(f"5 + 3 = {result}")

# Use variables
print(f"PI = {my_module.PI}")

# Use classes
calc = my_module.Calculator()
print(f"4 * 6 = {calc.multiply(4, 6)}")

# Alternative imports
from my_module import greet, add_numbers
print(greet("Bob"))
print(add_numbers(10, 15))
```

### Module Search Path

```python
import sys

# See where Python looks for modules
for path in sys.path:
    print(path)

# Add a custom path
sys.path.append('/path/to/my/modules')
```

### Package Structure

For larger projects, organize modules into packages:

```
my_package/
    __init__.py          # Makes it a package
    module1.py
    module2.py
    sub_package/
        __init__.py
        sub_module.py
```

```python
# Using packages
from my_package import module1
from my_package.sub_package import sub_module
```

### Best Practices

```python
# Good import organization (PEP 8 style)
# 1. Standard library imports
import os
import sys
from datetime import datetime

# 2. Third-party imports
import requests
import pandas as pd

# 3. Local application imports
from my_module import greet
from . import local_module  # Relative import
```

---

## Python JSON

JSON (JavaScript Object Notation) is a lightweight format for storing and exchanging data. It's like a universal language for data.

### What is JSON?

JSON looks similar to Python dictionaries but with some key differences:
- Strings must use double quotes
- No trailing commas
- Only basic data types: string, number, boolean, null, array, object

```json
{
    "name": "John",
    "age": 30,
    "married": true,
    "children": null,
    "hobbies": ["reading", "swimming"]
}
```

### Working with JSON in Python

```python
import json

# Python dictionary
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "hobbies": ["reading", "coding", "hiking"],
    "married": False
}

# Convert Python object to JSON string
json_string = json.dumps(person)
print(f"JSON string: {json_string}")
print(f"Type: {type(json_string)}")

# Convert JSON string back to Python object
parsed_data = json.loads(json_string)
print(f"Parsed data: {parsed_data}")
print(f"Type: {type(parsed_data)}")
```

### Pretty Printing JSON

```python
import json

data = {"name": "Bob", "scores": [85, 90, 88], "active": True}

# Pretty print with indentation
pretty_json = json.dumps(data, indent=4)
print(pretty_json)

# Sort keys alphabetically
sorted_json = json.dumps(data, indent=4, sort_keys=True)
print(sorted_json)
```

### Reading and Writing JSON Files

```python
import json

# Writing to JSON file
data = {
    "students": [
        {"name": "Alice", "grade": 85},
        {"name": "Bob", "grade": 92},
        {"name": "Charlie", "grade": 78}
    ],
    "class": "Python 101"
}

# Write to file
with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

# Read from file
with open("students.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

### Handling JSON Errors

```python
import json

# Invalid JSON will raise an exception
invalid_json = '{"name": "Alice", "age": 25,}'  # Trailing comma

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError as e:
    print(f"JSON Error: {e}")
    print(f"Error at line {e.lineno}, column {e.colno}")
```

### Working with Nested JSON

```python
import json

# Complex nested structure
company_data = {
    "company": "Tech Corp",
    "employees": [
        {
            "name": "Alice",
            "department": "Engineering",
            "skills": ["Python", "JavaScript"],
            "address": {
                "street": "123 Main St",
                "city": "Boston",
                "zip": "02101"
            }
        },
        {
            "name": "Bob",
            "department": "Sales",
            "skills": ["Communication", "CRM"],
            "address": {
                "street": "456 Oak Ave",
                "city": "Boston",
                "zip": "02102"
            }
        }
    ]
}

# Access nested data
print(f"Company: {company_data['company']}")
print(f"First employee: {company_data['employees'][0]['name']}")
print(f"First employee's city: {company_data['employees'][0]['address']['city']}")

# Iterate through employees
for employee in company_data['employees']:
    print(f"{employee['name']} works in {employee['department']}")
    print(f"  Skills: {', '.join(employee['skills'])}")
```

### Custom JSON Encoding/Decoding

```python
import json
from datetime import datetime

# Custom encoder for datetime objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# Using custom encoder
data_with_date = {
    "name": "Alice",
    "timestamp": datetime.now()
}

# This would normally fail
# json.dumps(data_with_date)  # TypeError

# But works with custom encoder
json_with_date = json.dumps(data_with_date, cls=DateTimeEncoder)
print(json_with_date)
```

### Practical Examples

```python
import json
import requests  # For API example (would need to install)

# Configuration file example
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "key": "your-api-key",
        "base_url": "https://api.example.com"
    },
    "debug": True
}

# Save configuration
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)

# Load configuration
def load_config():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Config file not found!")
        return {}
    except json.JSONDecodeError:
        print("Invalid JSON in config file!")
        return {}

# Data processing example
def process_user_data(json_file):
    with open(json_file, "r") as f:
        users = json.load(f)
    
    # Process data
    active_users = [user for user in users if user.get("active", False)]
    average_age = sum(user.get("age", 0) for user in users) / len(users)
    
    return {
        "total_users": len(users),
        "active_users": len(active_users),
        "average_age": round(average_age, 1)
    }
```

---

## Python RegEx

Regular Expressions (RegEx) are powerful tools for pattern matching and text manipulation. Think of them as a search language for text.

### Introduction to RegEx

RegEx uses special characters to define search patterns:
- `.` - Any character except newline
- `*` - Zero or more of the preceding character
- `+` - One or more of the preceding character
- `?` - Zero or one of the preceding character
- `^` - Start of string
- `$` - End of string
- `[]` - Character set
- `()` - Groups
- `|` - OR operator

### Basic Pattern Matching

```python
import re

text = "The quick brown fox jumps over 123 lazy dogs"

# Basic search
pattern = "fox"
match = re.search(pattern, text)
if match:
    print(f"Found '{pattern}' at position {match.start()}-{match.end()}")
    print(f"Matched text: '{match.group()}'")

# Find all matches
pattern = "o"
matches = re.findall(pattern, text)
print(f"Found {len(matches)} occurrences of '{pattern}': {matches}")

# Check if string matches pattern
pattern = "The"
if re.match(pattern, text):
    print(f"Text starts with '{pattern}'")
```

### Character Classes and Quantifiers

```python
import re

# Character classes
text = "Hello World 123! How are you doing today?"

# \d - digits, \w - word characters, \s - whitespace
digits = re.findall(r'\d', text)           # ['1', '2', '3']
digits_plus = re.findall(r'\d+', text)     # ['123']
words = re.findall(r'\w+', text)           # All words
whitespace = re.findall(r'\s+', text)      # All whitespace

print(f"Digits: {digits}")
print(f"Number sequences: {digits_plus}")
print(f"Words: {words}")

# Custom character sets
vowels = re.findall(r'[aeiouAEIOU]', text)
consonants = re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', text)
not_digits = re.findall(r'[^0-9]', text)   # Everything except digits

print(f"Vowels: {vowels}")
print(f"Consonants: {consonants[:10]}...")  # Show first 10
```

### Quantifiers in Detail

```python
import re

text = "aaabbbcccc"

# Different quantifiers
patterns = {
    r'a+': 'One or more a',
    r'a*': 'Zero or more a', 
    r'a?': 'Zero or one a',
    r'a{3}': 'Exactly 3 a',
    r'a{2,4}': '2 to 4 a',
    r'a{3,}': '3 or more a'
}

for pattern, description in patterns.items():
    matches = re.findall(pattern, text)
    print(f"{pattern:8} ({description:15}): {matches}")
```

### Anchors and Boundaries

```python
import re

lines = [
    "start of line",
    "middle start middle", 
    "end line",
    "the word boundary test"
]

for line in lines:
    # ^ - start of string/line
    if re.search(r'^start', line):
        print(f"'{line}' starts with 'start'")
    
    # $ - end of string/line
    if re.search(r'line$', line):
        print(f"'{line}' ends with 'line'")
    
    # \b - word boundary
    if re.search(r'\bword\b', line):
        print(f"'{line}' contains whole word 'word'")
```

### Groups and Capturing

```python
import re

# Email pattern example
email_text = "Contact us at: john.doe@example.com or support@company.org"

# Simple email pattern with groups
email_pattern = r'(\w+\.?\w+)@(\w+\.\w+)'
matches = re.finditer(email_pattern, email_text)

for match in matches:
    print(f"Full email: {match.group(0)}")    # Full match
    print(f"Username: {match.group(1)}")      # First group
    print(f"Domain: {match.group(2)}")        # Second group
    print("---")

# Named groups
phone_pattern = r'(?P<area>\d{3})-(?P<exchange>\d{3})-(?P<number>\d{4})'
phone_text = "Call me at 555-123-4567 or 888-999-0000"

for match in re.finditer(phone_pattern, phone_text):
    print(f"Area code: {match.group('area')}")
    print(f"Exchange: {match.group('exchange')}")
    print(f"Number: {match.group('number')}")
```

### String Substitution

```python
import re

text = "The price is $19.99 and the tax is $2.50"

# Simple substitution
new_text = re.sub(r'\$', 'USD ', text)
print(f"Original: {text}")
print(f"Modified: {new_text}")

# Using groups in substitution
date_text = "Today is 12/25/2024"
# Convert MM/DD/YYYY to DD-MM-YYYY
new_date = re.sub(r'(\d{2})/(\d{2})/(\d{4})', r'\2-\1-\3', date_text)
print(f"Original date: {date_text}")
print(f"New format: {new_date}")

# Using a function for complex substitutions
def celsius_to_fahrenheit(match):
    celsius = float(match.group(1))
    fahrenheit = (celsius * 9/5) + 32
    return f"{fahrenheit:.1f}°F"

temp_text = "It's 25°C today and 30°C tomorrow"
converted = re.sub(r'(\d+)°C', celsius_to_fahrenheit, temp_text)
print(f"Original: {temp_text}")
print(f"Converted: {converted}")
```

### Common RegEx Patterns

```python
import re

# Validation patterns
patterns = {
    'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    'phone': r'^\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})$',
    'url': r'https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:\w.))?)?',
    'ip_address': r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$',
    'credit_card': r'^\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}$'
}

test_data = {
    'email': ['user@example.com', 'invalid.email', 'test@domain.co.uk'],
    'phone': ['(555) 123-4567', '555-123-4567', '5551234567', '123-45-678'],
    'ip_address': ['192.168.1.1', '256.1.1.1', '10.0.0.1']
}

def validate_pattern(pattern_name, test_values):
    print(f"\nValidating {pattern_name}:")
    pattern = patterns[pattern_name]
    
    for value in test_values:
        is_valid = bool(re.match(pattern, value))
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {value:20} - {status}")

# Test patterns
for pattern_name in ['email', 'phone', 'ip_address']:
    if pattern_name in test_data:
        validate_pattern(pattern_name, test_data[pattern_name])
```

### Practical Examples

```python
import re

# Log file parser
def parse_log_line(line):
    # Example log format: "2024-01-15 10:30:45 [INFO] User login successful for user123"
    pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) \[(\w+)\] (.+)'
    match = re.match(pattern, line)
    
    if match:
        return {
            'date': match.group(1),
            'time': match.group(2),
            'level': match.group(3),
            'message': match.group(4)
        }
    return None

# Text cleaner
def clean_text(text):
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove special characters except basic punctuation
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

# Password strength checker
def check_password_strength(password):
    checks = {
        'length': len(password) >= 8,
        'uppercase': bool(re.search(r'[A-Z]', password)),
        'lowercase': bool(re.search(r'[a-z]', password)),
        'digit': bool(re.search(r'\d', password)),
        'special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    }
    
    score = sum(checks.values())
    strength = ['Very Weak', 'Weak', 'Fair', 'Good', 'Strong'][min(score, 4)]
    
    return {
        'strength': strength,
        'score': f"{score}/5",
        'checks': checks
    }

# Example usage
sample_log = "2024-01-15 10:30:45 [INFO] User login successful for user123"
parsed = parse_log_line(sample_log)
print(f"Parsed log: {parsed}")

dirty_text = "  Hello    <b>World</b>!!!   Extra   spaces  "
clean = clean_text(dirty_text)
print(f"Cleaned text: '{clean}'")

password_result = check_password_strength("MyPass123!")
print(f"Password strength: {password_result}")
```

---

## Python PIP

PIP (Pip Installs Packages) is Python's package manager. It's like an app store for Python libraries.

### What is PIP?

PIP comes with Python 3.4+ and allows you to:
- Install packages from the Python Package Index (PyPI)
- Manage package versions
- Uninstall packages
- List installed packages

### Basic PIP Commands

```bash
# Check PIP version
pip --version

# Install a package
pip install requests

# Install specific version
pip install requests==2.28.1

# Install minimum version
pip install requests>=2.25.0

# Install from requirements file
pip install -r requirements.txt

# Upgrade a package
pip install --upgrade requests

# Uninstall a package
pip uninstall requests

# List installed packages
pip list

# Show package information
pip show requests

# Search packages (deprecated in newer versions)
pip search flask
```

### Working with Requirements Files

Create a `requirements.txt` file to manage project dependencies:

```txt
# requirements.txt
requests==2.28.1
pandas>=1.3.0
numpy
flask==2.0.1
matplotlib>=3.5.0
```

```bash
# Install all requirements
pip install -r requirements.txt

# Generate requirements from current environment
pip freeze > requirements.txt
```

### Virtual Environments and PIP

```bash
# Create virtual environment
python -m venv myproject

# Activate virtual environment
# On Windows:
myproject\Scripts\activate
# On macOS/Linux:
source myproject/bin/activate

# Install packages in virtual environment
pip install flask pandas

# Deactivate virtual environment
deactivate
```

### Common Packages to Know

```python
# After installing with: pip install requests
import requests
response = requests.get('https://api.github.com/users/octocat')
print(response.json())

# After installing with: pip install pandas
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print(df)

# After installing with: pip install matplotlib
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
plt.show()
```

### PIP Configuration

```bash
# Upgrade PIP itself
pip install --upgrade pip

# Install from different index
pip install -i https://pypi.org/simple/ requests

# Install with no dependencies
pip install --no-deps package_name

# Install in user directory (no admin rights needed)
pip install --user package_name
```

---

## Python Try...Except

Error handling is crucial for creating robust programs. Try...except blocks help you handle errors gracefully.

### Understanding Exceptions

```python
# This will crash your program
# number = int("not_a_number")  # ValueError

# This handles the error gracefully
try:
    number = int("not_a_number")
    print(f"Number is: {number}")
except ValueError:
    print("That's not a valid number!")
```

### Basic Try...Except Structure

```python
try:
    # Code that might cause an error
    risky_code_here()
except SpecificError:
    # Handle specific error
    handle_error()
except AnotherError:
    # Handle another type of error
    handle_another_error()
else:
    # Runs if no errors occurred
    success_code()
finally:
    # Always runs, regardless of errors
    cleanup_code()
```

### Common Exception Types

```python
# ValueError - wrong value type
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number")

# ZeroDivisionError - division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# FileNotFoundError - file doesn't exist
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")

# KeyError - dictionary key doesn't exist
try:
    person = {"name": "Alice"}
    age = person["age"]
except KeyError:
    print("Key 'age' not found in dictionary")

# IndexError - list index out of range
try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("List index out of range")
```

### Multiple Exception Handling

```python
def safe_divide(a, b):
    try:
        # Convert to numbers
        num_a = float(a)
        num_b = float(b)
        # Perform division
        result = num_a / num_b
        return result
    except ValueError:
        print(f"Cannot convert '{a}' or '{b}' to number")
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

# Test the function
print(safe_divide("10", "2"))      # 5.0
print(safe_divide("10", "0"))      # Division by zero error
print(safe_divide("abc", "2"))     # ValueError
```

### Exception Information

```python
import sys

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"Error details: {sys.exc_info()}")

# Getting more detailed traceback
import traceback

try:
    def problematic_function():
        return 1 / 0
    
    problematic_function()
except Exception as e:
    print("Full traceback:")
    traceback.print_exc()
```

### Else and Finally Clauses

```python
def read_file_safely(filename):
    try:
        file = open(filename, 'r')
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    else:
        # Only runs if no exception occurred
        print(f"Successfully opened '{filename}'")
        content = file.read()
        return content
    finally:
        # Always runs - good for cleanup
        try:
            file.close()
            print("File closed")
        except:
            pass  # File wasn't opened

# Database connection example
def connect_to_database():
    connection = None
    try:
        # Simulate database connection
        connection = create_connection()  # This would be a real function
        # Do database operations
        return query_data(connection)
    except ConnectionError:
        print("Could not connect to database")
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        # Always close connection if it exists
        if connection:
            connection.close()
            print("Database connection closed")
```

### Custom Exceptions

```python
# Create custom exception classes
class InvalidAgeError(Exception):
    """Raised when age is invalid"""
    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class InsufficientFundsError(Exception):
    """Raised when account has insufficient funds"""
    pass

# Using custom exceptions
def validate_age(age):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    print(f"Age {age} is valid")

def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(f"Cannot withdraw ${amount}. Balance: ${balance}")
    return balance - amount

# Test custom exceptions
try:
    validate_age(200)
except InvalidAgeError as e:
    print(f"Age validation error: {e}")

try:
    new_balance = withdraw_money(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```

### Practical Error Handling Patterns

```python
# Retry pattern
import time
import random

def unreliable_function():
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network error")
    return "Success!"

def retry_operation(func, max_retries=3, delay=1):
    for attempt in range(max_retries):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print("Max retries reached")
                raise

# Usage
try:
    result = retry_operation(unreliable_function)
    print(f"Result: {result}")
except Exception:
    print("Operation failed after all retries")

# Input validation pattern
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError("Number must be positive")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}")
            print("Please try again.")

# Graceful degradation pattern
def get_user_data(user_id):
    try:
        # Try to get from database
        return get_from_database(user_id)
    except DatabaseError:
        try:
            # Fall back to cache
            return get_from_cache(user_id)
        except CacheError:
            # Fall back to default
            return {"id": user_id, "name": "Unknown User"}
```

### Logging Errors

```python
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

def divide_with_logging(a, b):
    try:
        result = a / b
        logging.info(f"Successfully divided {a} by {b} = {result}")
        return result
    except ZeroDivisionError:
        logging.error(f"Attempted to divide {a} by zero")
        raise
    except Exception as e:
        logging.exception(f"Unexpected error in division: {e}")
        raise

# Test logging
try:
    divide_with_logging(10, 2)
    divide_with_logging(10, 0)
except Exception:
    pass
```

---

## Python VirtualEnv

Virtual environments are isolated Python environments that allow you to manage dependencies for different projects separately.

### Why Use Virtual Environments?

Imagine you have two projects:
- Project A needs Django 3.2
- Project B needs Django 4.1

Without virtual environments, you can only have one version installed globally. Virtual environments solve this by creating isolated spaces.

### Creating Virtual Environments

```bash
# Method 1: Using venv (built-in, Python 3.3+)
python -m venv myproject_env

# Method 2: Using virtualenv (needs installation)
pip install virtualenv
virtualenv myproject_env

# Method 3: Using conda (if you have Anaconda)
conda create --name myproject_env python=3.9
```

### Activating and Deactivating

```bash
# Activate virtual environment
# On Windows:
myproject_env\Scripts\activate

# On macOS/Linux:
source myproject_env/bin/activate

# Your prompt should change to show (myproject_env)

# Deactivate virtual environment
deactivate
```

### Working with Virtual Environments

```bash
# After activation, install packages
pip install requests pandas flask

# Check what's installed
pip list

# Create requirements file
pip freeze > requirements.txt

# Install from requirements file (in new environment)
pip install -r requirements.txt
```

### Project Structure Example

```
my_project/
├── project_env/          # Virtual environment folder
│   ├── Scripts/         # (Windows) or bin/ (macOS/Linux)
│   ├── Lib/             # Installed packages
│   └── ...
├── src/                 # Your source code
│   ├── main.py
│   └── utils.py
├── requirements.txt     # Dependencies list
├── README.md
└── .gitignore          # Don't commit the env folder!
```

### Managing Multiple Environments

```python
# Create a simple environment manager script
import os
import subprocess
import sys

class EnvironmentManager:
    def __init__(self, base_path="./environments"):
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)
    
    def create_env(self, name, python_version=None):
        env_path = os.path.join(self.base_path, name)
        
        if os.path.exists(env_path):
            print(f"Environment '{name}' already exists")
            return
        
        cmd = [sys.executable, "-m", "venv", env_path]
        if python_version:
            cmd.extend(["--python", python_version])
        
        try:
            subprocess.run(cmd, check=True)
            print(f"Created environment '{name}'")
        except subprocess.CalledProcessError:
            print(f"Failed to create environment '{name}'")
    
    def list_environments(self):
        if not os.path.exists(self.base_path):
            print("No environments found")
            return
        
        envs = [d for d in os.listdir(self.base_path) 
                if os.path.isdir(os.path.join(self.base_path, d))]
        
        if envs:
            print("Available environments:")
            for env in envs:
                print(f"  - {env}")
        else:
            print("No environments found")
    
    def get_activation_command(self, name):
        env_path = os.path.join(self.base_path, name)
        if os.name == 'nt':  # Windows
            return f"{env_path}\\Scripts\\activate"
        else:  # macOS/Linux
            return f"source {env_path}/bin/activate"

# Usage example
manager = EnvironmentManager()
manager.create_env("web_project")
manager.create_env("data_analysis")
manager.list_environments()
```

### Environment Configuration

```python
# config.py - Environment-specific configuration
import os

class Config:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'development')
        self.debug = os.getenv('DEBUG', 'False').lower() == 'true'
        
    def get_database_url(self):
        if self.environment == 'production':
            return os.getenv('PROD_DATABASE_URL')
        elif self.environment == 'testing':
            return os.getenv('TEST_DATABASE_URL')
        else:
            return os.getenv('DEV_DATABASE_URL', 'sqlite:///dev.db')

# .env file example (use python-dotenv package)
"""
ENVIRONMENT=development
DEBUG=True
DEV_DATABASE_URL=sqlite:///development.db
API_KEY=your-dev-api-key
"""

# Loading environment variables
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

config = Config()
print(f"Environment: {config.environment}")
print(f"Debug mode: {config.debug}")
print(f"Database URL: {config.get_database_url()}")
```

### Best Practices

```bash
# 1. Always use requirements.txt
pip freeze > requirements.txt

# 2. Use .gitignore to exclude virtual environment
echo "venv/" >> .gitignore
echo "env/" >> .gitignore
echo "*.env" >> .gitignore

# 3. Pin package versions for production
# requirements.txt
Django==4.1.0
requests==2.28.1
pandas==1.5.0

# 4. Use separate requirements for development
# requirements-dev.txt
pytest==7.1.0
black==22.6.0
flake8==5.0.0

# Install dev requirements
pip install -r requirements-dev.txt
```

### Advanced Virtual Environment Tools

```bash
# pipenv - higher level tool
pip install pipenv

# Create Pipfile and virtual environment
pipenv install requests

# Install dev dependencies
pipenv install pytest --dev

# Activate environment
pipenv shell

# Run commands in environment
pipenv run python script.py

# poetry - modern dependency management
pip install poetry

# Initialize new project
poetry new my-project
cd my-project

# Add dependencies
poetry add requests
poetry add pytest --dev

# Install dependencies
poetry install

# Activate environment
poetry shell
```

---

# File Handling

File handling is essential for reading data, saving results, and persisting information between program runs.

## Python File Handling

### Understanding Files

Files are containers for data stored on your computer. Python can work with:
- Text files (.txt, .csv, .json, .py)
- Binary files (.jpg, .pdf, .exe)
- Structured data files (.xml, .yaml)

### Opening Files

```python
# Basic file opening
file = open("example.txt", "r")  # Open for reading
content = file.read()
file.close()  # Always close files!

# Better approach - using 'with' statement
with open("example.txt", "r") as file:
    content = file.read()
    # File automatically closes when leaving the 'with' block
```

### File Opening Modes

```python
# Different modes for opening files
modes = {
    'r': 'Read only (default)',
    'w': 'Write only (overwrites existing)',
    'a': 'Append only',
    'r+': 'Read and write',
    'w+': 'Read and write (overwrites existing)',
    'a+': 'Read and append',
    'rb': 'Read binary',
    'wb': 'Write binary',
    'ab': 'Append binary'
}

# Examples
with open("data.txt", "r") as file:      # Read text
    content = file.read()

with open("output.txt", "w") as file:    # Write text (overwrites)
    file.write("Hello World")

with open("log.txt", "a") as file:       # Append text
    file.write("New log entry\n")

with open("image.jpg", "rb") as file:    # Read binary
    binary_data = file.read()
```

### File Object Methods

```python
# Different ways to read files
with open("sample.txt", "r") as file:
    # Read entire file
    all_content = file.read()
    
    # Read one line
    file.seek(0)  # Go back to beginning
    first_line = file.readline()
    
    # Read all lines into a list
    file.seek(0)
    all_lines = file.readlines()
    
    # Iterate through lines
    file.seek(0)
    for line in file:
        print(line.strip())  # strip() removes newline characters

print(f"All content: {all_content}")
print(f"First line: {first_line}")
print(f"All lines: {all_lines}")
```

### Error Handling with Files

```python
def safe_read_file(filename):
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except PermissionError:
        print(f"No permission to read '{filename}'")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

# Usage
content = safe_read_file("example.txt")
if content:
    print("File content:", content)
```

---

## Python Read Files

### Reading Text Files

```python
# Read entire file at once
def read_entire_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error: {e}")
        return None

# Read file line by line (memory efficient for large files)
def read_file_lines(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = []
            for line in file:
                lines.append(line.strip())  # Remove newline characters
            return lines
    except Exception as e:
        print(f"Error: {e}")
        return []

# Read specific number of characters
def read_characters(filename, num_chars):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read(num_chars)
    except Exception as e:
        print(f"Error: {e}")
        return None
```

### Reading CSV Files

```python
import csv

# Reading CSV with csv module
def read_csv_file(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            
            # Read header
            header = next(csv_reader)
            print(f"Header: {header}")
            
            # Read data rows
            data = []
            for row in csv_reader:
                data.append(row)
            
            return header, data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return None, []

# Reading CSV as dictionaries
def read_csv_as_dict(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file)
            
            data = []
            for row in csv_reader:
                data.append(dict(row))
            
            return data
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return []

# Example CSV content:
# name,age,city
# Alice,25,New York
# Bob,30,Los Angeles
# Charlie,35,Chicago

# Usage
header, rows = read_csv_file("people.csv")
dict_data = read_csv_as_dict("people.csv")

print("Rows:", rows)
print("Dictionary format:", dict_data)
```

### Reading JSON Files

```python
import json

def read_json_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Invalid JSON format: {e}")
        return None
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return None
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return None

# Example JSON file content:
# {
#     "users": [
#         {"name": "Alice", "age": 25, "email": "alice@email.com"},
#         {"name": "Bob", "age": 30, "email": "bob@email.com"}
#     ],
#     "meta": {"version": "1.0", "created": "2024-01-15"}
# }

data = read_json_file("users.json")
if data:
    print("Users:", data["users"])
    print("Version:", data["meta"]["version"])
```

### Reading Configuration Files

```python
# Reading .ini configuration files
import configparser

def read_config_file(filename):
    config = configparser.ConfigParser()
    try:
        config.read(filename)
        return config
    except Exception as e:
        print(f"Error reading config: {e}")
        return None

# Example config.ini file:
# [database]
# host = localhost
# port = 5432
# name = myapp
# 
# [api]
# key = your-api-key
# url = https://api.example.com

config = read_config_file("config.ini")
if config:
    db_host = config.get("database", "host")
    api_key = config.get("api", "key")
    print(f"Database host: {db_host}")
    print(f"API key: {api_key}")
```

### Reading Large Files Efficiently

```python
# For very large files, read in chunks
def read_large_file_chunks(filename, chunk_size=1024):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk  # Use generator to save memory
    except Exception as e:
        print(f"Error reading file: {e}")

# Process large file without loading everything into memory
def process_large_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            line_count = 0
            word_count = 0
            
            for line in file:  # Reads one line at a time
                line_count += 1
                word_count += len(line.split())
                
                # Process line here
                if line_count % 1000 == 0:  # Progress indicator
                    print(f"Processed {line_count} lines...")
            
            return line_count, word_count
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0

# Usage
lines, words = process_large_file("large_file.txt")
print(f"File has {lines} lines and {words} words")
```

### Reading Binary Files

```python
# Reading binary files (images, executables, etc.)
def read_binary_file(filename):
    try:
        with open(filename, "rb") as file:
            binary_data = file.read()
            return binary_data
    except Exception as e:
        print(f"Error reading binary file: {e}")
        return None

# Reading image file and getting basic info
def analyze_image_file(filename):
    try:
        with open(filename, "rb") as file:
            # Read first few bytes to identify file type
            header = file.read(10)
            
            # Check file signatures
            if header.startswith(b'\xFF\xD8\xFF'):
                file_type = "JPEG"
            elif header.startswith(b'\x89PNG'):
                file_type = "PNG"
            elif header.startswith(b'GIF87a') or header.startswith(b'GIF89a'):
                file_type = "GIF"
            else:
                file_type = "Unknown"
            
            # Get file size
            file.seek(0, 2)  # Go to end of file
            file_size = file.tell()
            
            return {
                "type": file_type,
                "size": file_size,
                "size_mb": round(file_size / 1024 / 1024, 2)
            }
    except Exception as e:
        print(f"Error analyzing image: {e}")
        return None

# Usage
image_info = analyze_image_file("photo.jpg")
if image_info:
    print(f"Image type: {image_info['type']}")
    print(f"Size: {image_info['size_mb']} MB")
```

---

## Python Write/Create Files

### Writing Text Files

```python
# Writing to a file (creates new file or overwrites existing)
def write_text_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except Exception as e:
        print(f"Error writing file: {e}")

# Appending to a file (adds to existing content)
def append_to_file(filename, content):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(content)
        print(f"Successfully appended to {filename}")
    except Exception as e:
        print(f"Error appending to file: {e}")

# Writing multiple lines
def write_lines_to_file(filename, lines):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")
        print(f"Successfully wrote {len(lines)} lines to {filename}")
    except Exception as e:
        print(f"Error writing lines: {e}")

# Usage examples
write_text_file("output.txt", "Hello, World!")
append_to_file("output.txt", "\nThis is a new line.")

lines = ["Line 1", "Line 2", "Line 3"]
write_lines_to_file("multi_line.txt", lines)
```

### Writing CSV Files

```python
import csv

# Writing CSV files
def write_csv_file(filename, data, headers):
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            
            # Write header
            writer.writerow(headers)
            
            # Write data rows
            writer.writerows(data)
        
        print(f"Successfully wrote CSV to {filename}")
    except Exception as e:
        print(f"Error writing CSV: {e}")

# Writing CSV from dictionaries
def write_csv_from_dicts(filename, dict_data):
    if not dict_data:
        return
    
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            fieldnames = dict_data[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(dict_data)
        
        print(f"Successfully wrote dictionary CSV to {filename}")
    except Exception as e:
        print(f"Error writing dictionary CSV: {e}")

# Example data
csv_headers = ["Name", "Age", "City"]
csv_data = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

dict_data = [
    {"name": "Alice", "age": 25, "city": "New York"},
    {"name": "Bob", "age": 30, "city": "Los Angeles"},
    {"name": "Charlie", "age": 35, "city": "Chicago"}
]

# Usage
write_csv_file("people.csv", csv_data, csv_headers)
write_csv_from_dicts("people_dict.csv", dict_data)
```

### Writing JSON Files

```python
import json
from datetime import datetime

# Writing JSON files
def write_json_file(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Successfully wrote JSON to {filename}")
    except Exception as e:
        print(f"Error writing JSON: {e}")

# Writing JSON with custom serialization
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def write_json_with_datetime(filename, data):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, cls=DateTimeEncoder)
        print(f"Successfully wrote JSON with datetime to {filename}")
    except Exception as e:
        print(f"Error writing JSON: {e}")

# Example data
user_data = {
    "users": [
        {"id": 1, "name": "Alice", "email": "alice@email.com", "active": True},
        {"id": 2, "name": "Bob", "email": "bob@email.com", "active": False}
    ],
    "meta": {
        "total_users": 2,
        "created": datetime.now(),
        "version": "1.0"
    }
}

# Usage
write_json_file("users.json", user_data)
write_json_with_datetime("users_with_date.json", user_data)
```

### Creating Directory Structure

```python
import os

# Create directories
def create_directory_structure(base_path, structure):
    """
    Create directory structure from nested dictionary
    structure = {
        'folder1': {
            'subfolder1': {},
            'subfolder2': {
                'subsubfolder': {}
            }
        },
        'folder2': {}
    }
    """
    def create_dirs(current_path, dirs_dict):
        for dir_name, subdirs in dirs_dict.items():
            dir_path = os.path.join(current_path, dir_name)
            os.makedirs(dir_path, exist_ok=True)
            print(f"Created directory: {dir_path}")
            
            if subdirs:  # If there are subdirectories
                create_dirs(dir_path, subdirs)
    
    try:
        os.makedirs(base_path, exist_ok=True)
        create_dirs(base_path, structure)
    except Exception as e:
        print(f"Error creating directory structure: {e}")

# Example usage
project_structure = {
    'src': {
        'models': {},
        'views': {},
        'controllers': {}
    },
    'tests': {},
    'docs': {},
    'data': {
        'raw': {},
        'processed': {}
    }
}

create_directory_structure("my_project", project_structure)
```

### Writing Configuration Files

```python
import configparser

# Writing INI configuration files
def write_config_file(filename, config_data):
    config = configparser.ConfigParser()
    
    for section_name, section_data in config_data.items():
        config[section_name] = section_data
    
    try:
        with open(filename, "w") as file:
            config.write(file)
        print(f"Successfully wrote config to {filename}")
    except Exception as e:
        print(f"Error writing config: {e}")

# Example configuration data
config_data = {
    'database': {
        'host': 'localhost',
        'port': '5432',
        'name': 'myapp',
        'user': 'admin'
    },
    'api': {
        'key': 'your-api-key',
        'url': 'https://api.example.com',
        'timeout': '30'
    },
    'logging': {
        'level': 'INFO',
        'file': 'app.log'
    }
}

write_config_file("config.ini", config_data)
```

### Writing Log Files

```python
import logging
from datetime import datetime

# Simple log writing
def write_log_entry(filename, message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] [{level}] {message}\n"
    
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(log_entry)
    except Exception as e:
        print(f"Error writing to log: {e}")

# Advanced logging setup
def setup_logging(log_file="app.log"):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()  # Also print to console
        ]
    )

# Application logger class
class AppLogger:
    def __init__(self, log_file="app.log"):
        self.log_file = log_file
        setup_logging(log_file)
        self.logger = logging.getLogger(__name__)
    
    def info(self, message):
        self.logger.info(message)
    
    def warning(self, message):
        self.logger.warning(message)
    
    def error(self, message):
        self.logger.error(message)
    
    def debug(self, message):
        self.logger.debug(message)

# Usage examples
write_log_entry("simple.log", "Application started")
write_log_entry("simple.log", "User login failed", "WARNING")

app_logger = AppLogger()
app_logger.info("Application initialized")
app_logger.warning("Low disk space")
app_logger.error("Database connection failed")
```

### Writing Binary Files

```python
# Writing binary data
def write_binary_file(filename, binary_data):
    try:
        with open(filename, "wb") as file:
            file.write(binary_data)
        print(f"Successfully wrote binary data to {filename}")
    except Exception as e:
        print(f"Error writing binary file: {e}")

# Copy binary file (like image, video, etc.)
def copy_binary_file(source, destination):
    try:
        with open(source, "rb") as src_file:
            with open(destination, "wb") as dest_file:
                # Copy in chunks to handle large files
                chunk_size = 1024 * 1024  # 1MB chunks
                while True:
                    chunk = src_file.read(chunk_size)
                    if not chunk:
                        break
                    dest_file.write(chunk)
        print(f"Successfully copied {source} to {destination}")
    except Exception as e:
        print(f"Error copying file: {e}")

# Create a simple binary file with specific pattern
def create_test_binary_file(filename, size_mb=1):
    try:
        with open(filename, "wb") as file:
            # Create a pattern of bytes
            pattern = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09'
            bytes_to_write = size_mb * 1024 * 1024
            
            while bytes_to_write > 0:
                chunk_size = min(len(pattern), bytes_to_write)
                file.write(pattern[:chunk_size])
                bytes_to_write -= chunk_size
        
        print(f"Created {size_mb}MB test file: {filename}")
    except Exception as e:
        print(f"Error creating test file: {e}")

# Usage
create_test_binary_file("test_data.bin", 2)  # Create 2MB test file
copy_binary_file("image.jpg", "backup_image.jpg")
```

---

## Python Delete Files

### Deleting Files

```python
import os

# Delete a single file
def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Successfully deleted {filename}")
        else:
            print(f"File {filename} does not exist")
    except PermissionError:
        print(f"Permission denied: Cannot delete {filename}")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Delete multiple files
def delete_files(file_list):
    deleted_count = 0
    for filename in file_list:
        try:
            if os.path.exists(filename):
                os.remove(filename)
                print(f"Deleted: {filename}")
                deleted_count += 1
            else:
                print(f"File not found: {filename}")
        except Exception as e:
            print(f"Error deleting {filename}: {e}")
    
    print(f"Successfully deleted {deleted_count} out of {len(file_list)} files")

# Usage
delete_file("temp_file.txt")
delete_files(["file1.txt", "file2.txt", "file3.txt"])
```

### Deleting Files with Patterns

```python
import os
import glob

# Delete files matching a pattern
def delete_files_by_pattern(pattern):
    try:
        files_to_delete = glob.glob(pattern)
        if not files_to_delete:
            print(f"No files found matching pattern: {pattern}")
            return
        
        print(f"Found {len(files_to_delete)} files matching pattern: {pattern}")
        for file_path in files_to_delete:
            print(f"  {file_path}")
        
        confirm = input("Delete these files? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            deleted_count = 0
            for file_path in files_to_delete:
                try:
                    os.remove(file_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
            
            print(f"Successfully deleted {deleted_count} files")
        else:
            print("Deletion cancelled")
    except Exception as e:
        print(f"Error finding files: {e}")

# Delete files by extension
def delete_files_by_extension(directory, extension):
    pattern = os.path.join(directory, f"*.{extension}")
    delete_files_by_pattern(pattern)

# Delete old files (older than specified days)
import time

def delete_old_files(directory, days_old=7):
    try:
        current_time = time.time()
        cutoff_time = current_time - (days_old * 24 * 60 * 60)  # Convert days to seconds
        
        deleted_count = 0
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            
            if os.path.isfile(file_path):
                file_modified_time = os.path.getmtime(file_path)
                
                if file_modified_time < cutoff_time:
                    try:
                        os.remove(file_path)
                        print(f"Deleted old file: {filename}")
                        deleted_count += 1
                    except Exception as e:
                        print(f"Error deleting {filename}: {e}")
        
        print(f"Deleted {deleted_count} old files (older than {days_old} days)")
    except Exception as e:
        print(f"Error processing directory: {e}")

# Usage examples
delete_files_by_extension("temp_folder", "tmp")  # Delete all .tmp files
delete_files_by_pattern("logs/*.log")             # Delete all .log files in logs folder
delete_old_files("downloads", 30)                # Delete files older than 30 days
```

### Deleting Directories

```python
import os
import shutil

# Delete empty directory
def delete_empty_directory(directory_path):
    try:
        if os.path.exists(directory_path):
            os.rmdir(directory_path)  # Only works for empty directories
            print(f"Successfully deleted empty directory: {directory_path}")
        else:
            print(f"Directory does not exist: {directory_path}")
    except OSError as e:
        if e.errno == 39:  # Directory not empty
            print(f"Directory not empty: {directory_path}")
        else:
            print(f"Error deleting directory: {e}")

# Delete directory and all its contents
def delete_directory_recursive(directory_path):
    try:
        if os.path.exists(directory_path):
            shutil.rmtree(directory_path)
            print(f"Successfully deleted directory and contents: {directory_path}")
        else:
            print(f"Directory does not exist: {directory_path}")
    except PermissionError:
        print(f"Permission denied: Cannot delete {directory_path}")
    except Exception as e:
        print(f"Error deleting directory: {e}")

# Safe directory deletion with confirmation
def safe_delete_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Directory does not exist: {directory_path}")
        return
    
    # Show directory contents
    try:
        total_size = 0
        file_count = 0
        
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
                file_count += 1
        
        size_mb = total_size / 1024 / 1024
        print(f"Directory: {directory_path}")
        print(f"Contains: {file_count} files ({size_mb:.2f} MB)")
        
        confirm = input("Are you sure you want to delete this directory? (yes/no): ").lower()
        if confirm in ['yes', 'y']:
            shutil.rmtree(directory_path)
            print("Directory deleted successfully")
        else:
            print("Deletion cancelled")
    
    except Exception as e:
        print(f"Error analyzing directory: {e}")

# Usage
delete_empty_directory("empty_folder")
delete_directory_recursive("old_project")
safe_delete_directory("large_folder")
```

### File Cleanup Utilities

```python
import os
import time
from pathlib import Path

class FileCleanup:
    def __init__(self, base_directory="."):
        self.base_directory = Path(base_directory)
    
    def find_duplicate_files(self):
        """Find files with same name in different directories"""
        file_names = {}
        duplicates = {}
        
        for file_path in self.base_directory.rglob("*"):
            if file_path.is_file():
                filename = file_path.name
                if filename in file_names:
                    if filename not in duplicates:
                        duplicates[filename] = [file_names[filename]]
                    duplicates[filename].append(file_path)
                else:
                    file_names[filename] = file_path
        
        return duplicates
    
    def find_large_files(self, min_size_mb=100):
        """Find files larger than specified size"""
        large_files = []
        min_size_bytes = min_size_mb * 1024 * 1024
        
        for file_path in self.base_directory.rglob("*"):
            if file_path.is_file():
                try:
                    if file_path.stat().st_size > min_size_bytes:
                        size_mb = file_path.stat().st_size / 1024 / 1024
                        large_files.append((file_path, size_mb))
                except OSError:
                    continue  # Skip files we can't access
        
        return sorted(large_files, key=lambda x: x[1], reverse=True)
    
    def find_empty_files(self):
        """Find empty files (0 bytes)"""
        empty_files = []
        
        for file_path in self.base_directory.rglob("*"):
            if file_path.is_file():
                try:
                    if file_path.stat().st_size == 0:
                        empty_files.append(file_path)
                except OSError:
                    continue
        
        return empty_files
    
    def cleanup_empty_directories(self):
        """Remove empty directories"""
        removed_dirs = []
        
        # Walk bottom-up to handle nested empty directories
        for dir_path in sorted(self.base_directory.rglob("*"), key=lambda p: len(p.parts), reverse=True):
            if dir_path.is_dir():
                try:
                    dir_path.rmdir()  # Only removes if empty
                    removed_dirs.append(dir_path)
                except OSError:
                    continue  # Directory not empty or permission error
        
        return removed_dirs
    
    def generate_cleanup_report(self):
        """Generate comprehensive cleanup report"""
        report = {
            'duplicates': self.find_duplicate_files(),
            'large_files': self.find_large_files(50),  # Files > 50MB
            'empty_files': self.find_empty_files(),
        }
        
        return report

# Usage example
cleanup = FileCleanup("my_project")

# Generate report
report = cleanup.generate_cleanup_report()

print("=== CLEANUP REPORT ===")
print(f"Duplicate files found: {len(report['duplicates'])}")
for filename, paths in report['duplicates'].items():
    print(f"  {filename}: {len(paths)} copies")

print(f"\nLarge files found: {len(report['large_files'])}")
for file_path, size_mb in report['large_files'][:5]:  # Show top 5
    print(f"  {file_path.name}: {size_mb:.1f} MB")

print(f"\nEmpty files found: {len(report['empty_files'])}")

# Cleanup empty directories
removed = cleanup.cleanup_empty_directories()
print(f"\nRemoved {len(removed)} empty directories")
```

### Safe File Operations

```python
import os
import shutil
from datetime import datetime

class SafeFileOperations:
    def __init__(self, backup_dir="backup"):
        self.backup_dir = backup_dir
        os.makedirs(backup_dir, exist_ok=True)
    
    def safe_delete_with_backup(self, file_path):
        """Delete file but keep a backup copy"""
        if not os.path.exists(file_path):
            print(f"File does not exist: {file_path}")
            return False
        
        try:
            # Create backup filename with timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = os.path.basename(file_path)
            backup_name = f"{filename}.backup.{timestamp}"
            backup_path = os.path.join(self.backup_dir, backup_name)
            
            # Copy to backup location
            shutil.copy2(file_path, backup_path)
            print(f"Created backup: {backup_path}")
            
            # Delete original
            os.remove(file_path)
            print(f"Deleted: {file_path}")
            return True
            
        except Exception as e:
            print(f"Error in safe delete: {e}")
            return False
    
    def restore_from_backup(self, original_path, backup_name=None):
        """Restore file from backup"""
        if backup_name is None:
            # Find most recent backup
            original_filename = os.path.basename(original_path)
            backups = [f for f in os.listdir(self.backup_dir) 
                      if f.startswith(original_filename + ".backup.")]
            
            if not backups:
                print(f"No backups found for {original_filename}")
                return False
            
            backup_name = sorted(backups)[-1]  # Most recent
        
        backup_path = os.path.join(self.backup_dir, backup_name)
        
        try:
            shutil.copy2(backup_path, original_path)
            print(f"Restored {original_path} from {backup_name}")
            return True
        except Exception as e:
            print(f"Error restoring file: {e}")
            return False
    
    def list_backups(self):
        """List all backup files"""
        try:
            backups = os.listdir(self.backup_dir)
            if not backups:
                print("No backup files found")
                return []
            
            print("Available backups:")
            for backup in sorted(backups):
                backup_path = os.path.join(self.backup_dir, backup)
                size = os.path.getsize(backup_path)
                mtime = datetime.fromtimestamp(os.path.getmtime(backup_path))
                print(f"  {backup} ({size} bytes, {mtime})")
            
            return backups
        except Exception as e:
            print(f"Error listing backups: {e}")
            return []

# Usage
safe_ops = SafeFileOperations()

# Safe delete with automatic backup
safe_ops.safe_delete_with_backup("important_file.txt")

# List available backups
safe_ops.list_backups()

# Restore file from backup
safe_ops.restore_from_backup("important_file.txt")
```

---

## Summary and Best Practices

### Key Takeaways

1. **Always use `with` statements** when working with files - they automatically handle closing
2. **Handle exceptions** - file operations can fail for many reasons
3. **Specify encoding** explicitly (usually `utf-8`) for text files
4. **Use appropriate file modes** - don't use write mode if you want to append
5. **Validate input** when getting user input
6. **Use virtual environments** to manage project dependencies
7. **Regular expressions are powerful** but can be complex - test thoroughly
8. **JSON is great for configuration** and data exchange
9. **Always backup important files** before deletion
10. **Consider memory usage** when working with large files

### Final Project Example

Here's a complete example that combines many concepts:

```python
import json
import csv
import os
import re
from datetime import datetime
import logging

class DataProcessor:
    def __init__(self, config_file="config.json"):
        self.setup_logging()
        self.load_config(config_file)
    
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('data_processor.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def load_config(self, config_file):
        try:
            with open(config_file, 'r') as f:
                self.config = json.load(f)
            self.logger.info(f"Loaded configuration from {config_file}")
        except FileNotFoundError:
            self.config = {
                "input_directory": "data/input",
                "output_directory": "data/output",
                "email_pattern": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
            }
            self.save_config(config_file)
            self.logger.info("Created default configuration")
    
    def save_config(self, config_file):
        with open(config_file, 'w') as f:
            json.dump(self.config, f, indent=4)
    
    def process_csv_data(self, input_file):
        try:
            processed_data = []
            
            with open(input_file, 'r', newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                
                for row in reader:
                    # Validate email
                    if 'email' in row:
                        if re.match(self.config['email_pattern'], row['email']):
                            processed_data.append(row)
                        else:
                            self.logger.warning(f"Invalid email: {row.get('email', '')}")
            
            return processed_data
            
        except Exception as e:
            self.logger.error(f"Error processing CSV: {e}")
            return []
    
    def save_results(self, data, output_file):
        try:
            # Create output directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            
            # Save as JSON
            json_file = output_file.replace('.csv', '.json')
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump({
                    'processed_at': datetime.now().isoformat(),
                    'total_records': len(data),
                    'data': data
                }, f, indent=4)
            
            # Save as CSV
            if data:
                with open(output_file, 'w', newline='', encoding='utf-8') as f:
                    writer = csv.DictWriter(f, fieldnames=data[0].keys())
                    writer.writeheader()
                    writer.writerows(data)
            
            self.logger.info(f"Saved {len(data)} records to {output_file}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error saving results: {e}")
            return False
    
    def run(self):
        input_dir = self.config['input_directory']
        output_dir = self.config['output_directory']
        
        if not os.path.exists(input_dir):
            self.logger.error(f"Input directory not found: {input_dir}")
            return
        
        # Process all CSV files in input directory
        for filename in os.listdir(input_dir):
            if filename.endswith('.csv'):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, f"processed_{filename}")
                
                self.logger.info(f"Processing {filename}")
                data = self.process_csv_data(input_path)
                
                if data:
                    self.save_results(data, output_path)
                else:
                    self.logger.warning(f"No valid data found in {filename}")

# Usage
if __name__ == "__main__":
    processor = DataProcessor()
    processor.run()
```

This example demonstrates:
- File handling (reading/writing CSV and JSON)
- Configuration management
- Error handling with try/except
- Logging
- Regular expressions for validation
- Directory operations
- String formatting
- Date/time handling

Congratulations! You now have a comprehensive understanding of Python's file handling capabilities and supporting concepts. Practice these concepts by building your own projects and gradually tackling more complex scenarios.