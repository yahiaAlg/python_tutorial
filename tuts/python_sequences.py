# Lists are Ordered Changeable Allow Duplicates type of sequence
list_example = ["apple", "banana", "cherry", "cherry"]
print(list_example) 
# Tuples are Ordered Not Changeable Allow Duplicates type of sequence
tuple_example = ("apple", "banana", "cherry", "cherry") 
print(tuple_example)
# sets are not Ordered Changeable doesn't Allow Duplicates type of sequence
set_example = {"apple", "banana", "cherry", "cherry"} 
print(set_example)

# accessing a list or a tuple using index
try:
    print("Accessing the list example by index : ", list_example[0])
except IndexError as e:
    print("An error occurred: ", str(e))

try:
    print("\nAccessing the tuple example by index : ", tuple_example[1])
except IndexError as e:
    print("An error occurred: ", str(e))

# checking if an item exists in a List or a tuple
print("banana" in list_example)
print("kiwi" not in tuple_example)
# checking if an item is present in a set
fruit_present = "cherry" in set_example
print(fruit_present)

# adding elements to lists and tuples
list_example.append("grape")
print("Adding element to the list example: ", list_example)

# tuples cannot be modified once created, so we can't add anything to it
# but we can convert it into a list first then modify it
tuple_as_list = list(tuple_example)
tuple_as_list.append("orange")
print("Modifying the tuple converted to a list: ", tuple_as_list)

# converting back to a tuple before assigning it back to the variable
tuple_example = tuple(tuple_as_list)
print("Converting back the list to a tuple: ", tuple_example)


# sorting lists
some_list = [8,9,2,6,3,54,-10]
print("The empty list was: ", some_list)
some_list.sort() #sorts the list in ascending order
print("After sorting the empty list: ", some_list)

# reversing lists
coffee_shops = ["Starbucks","Peet's Coffee","Dunkin Donuts"]
print("Original coffee shops list: ", coffee_shops)
coffee_shops.reverse()
print("List after reversal: ", coffee_shops)

# checking if an item is in a list with the "in" keyword
tea = "green tea"
print("\nChecking for the existence of '{}' in the list using 'in': ".format(tea))
drinks = ["tea", "coffee", "juice", "water"]
if tea in drinks:
    print("Yes, {} is in the list!".format(tea))
else:
    print("No, {} is not in the list.".format(tea))
# List operations
# appending
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# inserting
fruit_basket = ["kiwi", "orange", "banana"]
fruit_basket.insert(1,"grapefruit")
print(fruit_basket)

# popping (removing and returning last element)
last_item = fruit_basket.pop()
print("Last item removed from fruit basket: ", last_item)
print("Fruit basket now: ", fruit_basket)

# removing specific items with remove() method
try:
    fruit_basket.remove("kiwi")  # this should work because "kiwi" exists in the list
    print("Kiwi has been removed.")
except ValueError as e:
    print("Value Error: ",e)

# replacing
fruit_basket[-1] = "mango"
print("Replacement test - Fruit Basket", fruit_basket)

# removing items from lists
del list_example[2]  # deletes the third element (index starts at 0)
print("Removing an item from the list example: ", list_example)

# popping an item from the end of the list
last_item = list_example.pop()  # defaults to removing the last item
# if you want to remove something else, use pop(index) instead
print("Popping the last item from the list example: ", last_item)
print("After popping, the list looks like this now: ", list_example)

# joining
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# or by element
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# or by extending it
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Sets operations
# addition by element
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# by a whole sequence
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# removing an element   ##Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# if it doesn't exist , use discard(), which won't raise an error.
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# to remove everything  in a set use clear
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# or the del keyword
thisset = {"apple", "banana", "cherry"}

del thisset

try:
    print(thisset)
except NameError:
    print("the set is not found")

# sets operations
# union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# multiple union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# intersection
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# difference

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# Symmetric Differences
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
