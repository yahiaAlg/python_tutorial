thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
carmodel = thisdict["model"]
print("the car model is", carmodel)
# or using get
print("The car model is %s" % thisdict.get("model"))

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car_properties = car.keys()

print(car_properties)  # before the change

car["color"] = "white"

print(car_properties)  # after the change

car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car_values = car.values()

print(car_values)  # before the change

car["year"] = 2020

print(car_values)  # after the change


car = {"brand": "Ford", "model": "Mustang", "year": 1964}

car_items = car.items()

print(car_items)  # before the change

car["year"] = 2020

print(car_items)  # after the change


# another type of change
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})

# adding items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print(thisdict)

# or by using update
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})

# removing items
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print(thisdict)

# or by del keyword

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict
print(thisdict)  # this will cause an error because "thisdict" no longer exists.

# or by clearing it
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print(thisdict)

# looping through dictionaries
# through keys
for x in thisdict:
    print(x)

for x in thisdict.keys():
  print(x) 

# through values
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
  print(x) 

# both at the same time (items)
for key, value in thisdict.items():
    print(key, value)   

# copying
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = thisdict.copy()
print(mydict)
# or by constructor
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
mydict = dict(thisdict)
print(mydict)


users = [
    ("amin", 22, "admin"),
    ("ahmed", 22, "normal user"),
    ("meriem", 22, "guest"),
    ("nesrine", 22, "normal user"),
    ("yahia", 22, "normal user"),
]
