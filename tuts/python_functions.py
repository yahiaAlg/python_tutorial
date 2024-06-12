# In Python a function is defined using the def keyword:
# Example


def my_function():
    print("Hello from a function")


my_function()


# Functions can take arguments, which  are passed when calling the function. These arguments act as placeholders for actual values that will be
# Functions can take parameters, which are values that get passed into the function when it's called.
# These parameter values act as placeholders for the actual data you want to pass in.  You can think of them like variable names
# These parameter values act as placeholders for the actual data you want to use in your function.  You can assign these placeholder names function_name(param1,param2,....)
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Number of Arguments


# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emil", "Refsnes")


# Arbitrary Arguments, *args

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:


# If the number of arguments is unknown, add a * before the parameter name:
def my_function(
    *kids,
):  # Arbitrary Arguments are often shortened to *args in Python documentations.
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# Keyword Arguments

# You can also send arguments with the key = value syntax.


# This way the order of the arguments does not matter.
# Example
def my_function(
    child3, child2, child1
):  # The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")

# Arbitrary Keyword Arguments, **kwargs

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:
# Example


# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(
    **kid,
):  # Arbitrary Kword Arguments are often shortened to **kwargs in Python documentations.
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")

# Passing a List as an Argument

# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.


# E.g. if you send a List as an argument, it will still be a List when it reaches the function:
# Example
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Return Values


# To let a function return a value, use the return statement:
# Example
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))

# The pass Statement


# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
# Example
def myfunction():
    pass


# Positional-Only Arguments

# You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.


# To specify that a function can have only positional arguments, add , / after the arguments:
# Example
def my_function(x, /):
    print(x)


my_function(3)


# Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:
# Example
def my_function(x):
    print(x)


my_function(x=3)

try:

    def my_function(x, /):
        print(x)

    my_function(x=3)
except TypeError as e:
    print(e)

# Keyword-Only Arguments


# To specify that a function can have only keyword arguments, add *, before the arguments:
# Example
def my_function(*, x):
    print(x)


my_function(x=3)


# Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:
# Example
def my_function(x):
    print(x)


my_function(3)

# But when adding the *, / you will get an error if you try to send a positional argument:
# Example
try:

    def my_function(*, x):
        print(x)

    my_function(3)
except TypeError as e:
    print(e)


# Combine Positional-Only and Keyword-Only

# You can combine the two argument types in the same function.


# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
# Example
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)


my_function(5, 6, c=7, d=8)

# Recursion

# Python also accepts function recursion, which means a defined function can call itself.

# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.


# Example
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.
# Syntax:
# lambda arguments: expression

# Example
# Get your own Python Server

# Add 10 to argument a, and return the result:
x = lambda a: a + 10
print(x(5))

# lambda functions can take any number of arguments:
# Example

# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b
print(x(5, 6))

# Example

# Summarize argument a, b, and c and return the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))

# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.


# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myfunc(n):
    return lambda a: a * n


# Use that function definition to make a function that always doubles the number you send in:
# Example
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))


# Or, use the same function definition to make a function that always triples the number you send in:
# Example
def myfunc(n):
    return lambda a: a * n


mytripler = myfunc(3)

print(mytripler(11))


# Or, use the same function definition to make both functions, in the same program:
# Example
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
