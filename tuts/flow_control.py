# conditionals
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# compact
if a > b:print("a is greater than b")
a = 2
b = 330
print("A") if a > b else print("B")
# ternary operator
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# using logical operators
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

# Nested
x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")


# loops
# while
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


# with skipping a step

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# with else
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# for loop
# iterating through sequence
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)
# with break and continue

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# looping through a range of values
for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)


# with else

for x in range(6):
    print(x)
else:
    print("Finally finished!")

# nested loops
matrix = [
    [1,3,5],
    [10,-2,6],
    [0,3,12],
    [2,-4,-7],
]

for row in matrix:
    for item in row:
        print(row, item)
