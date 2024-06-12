# Python Classes/Objects

# Python is an object oriented programming language.

# Almost everything in Python is an object, with its properties and methods.

# A Class is like an object constructor, or a "blueprint" for creating objects.
# Create a Class

# To create a class, use the keyword class:
# Example
# Get your own Python Server


# Create a class named MyClass, with a property named x:
class MyClass:
    x = 5


# Create Object

# Now we can use the class named MyClass to create objects:
# Example

# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)


# The __init__() Function

# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
# Example


# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:

    def __init__(
        self, name, age
    ):  # Note: The __init__() function is called automatically every time the class is being used to create a new object.
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# The __str__() Function

# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:
# Example


# The string representation of an object WITHOUT the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1)

# Example


# The string representation of an object WITH the __str__() function:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"


p1 = Person("John", 36)

print(p1)

# Object Methods

# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:
# Example


# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print(
            "Hello my name is " + self.name
        )  # Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


p1 = Person("John", 36)
p1.myfunc()

# The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
# Example


# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()

# Modify Object Properties

# You can modify properties on objects like this:
# Example

# Set the age of p1 to 40:
p1.age = 40

# Delete Object Properties

# You can delete properties on objects by using the del keyword:
# Example

# Delete the age property from the p1 object:
del p1.age

# Delete Objects

# You can delete objects by using the del keyword:
# Example

# Delete the p1 object:
del p1

# The pass Statement


# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
# Example
class Person:
    pass


# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class

# Any class can be a parent class, so the syntax is the same as creating any other class:
# Example


# Create a class named Person, with firstname and lastname properties, and a printname method:
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


# Create a Child Class

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:
# Example


# Create a class named Student, which will inherit the properties and methods from the Person class:
class Student(Person):
    pass  # Note: Use the pass keyword when you do not want to add any other properties or methods to the class.


# Now the Student class has the same properties and methods as the Person class.
# Example

# Use the Student class to create an object, and then execute the printname method:
x = Student("Mike", "Olsen")
x.printname()

# Add the __init__() Function

# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# Example


# Add the __init__() function to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        # add properties etc.
        pass


# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.


# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
# Example
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)


# Use the super() Function


# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
# Example
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(
            fname, lname
        )  # By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.


# Add Properties
# Example


# Add a property called graduationyear to the Student class:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2019


x = Student("Mike", "Olsen", 2019)


# Add Methods
# Example


# Add a method called welcome to the Student class:
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(
            "Welcome",
            self.firstname,
            self.lastname,
            "to the class of",
            self.graduationyear,
        )


# Class Polymorphism

# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move():
# Example


# Different classes with the same method:
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car class
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat class
plane1 = Plane("Boeing", "747")  # Create a Plane class

for x in (car1, boat1, plane1):
    x.move()
# Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.


# Inheritance Class Polymorphism

# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, but can override them:
# Example


# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

# Because of polymorphism we can execute the same method for all classes.
