# Tuples and Dictionaries
# 
# Tuples

# Tuples is similar to list but represented by () instead of []
# Tuples different from list tuples are immutable, which means you can not change or add or delete a value in the tuple.
# You can not append, you can not del, you can not change a value
# Tuples are ordered, unchangeable, and allow duplicated values


# First sample of Tuples - It can be used within () or not
tuple1 = (1,2,3,4,5)
tuple1 = 1,2,3,4,5



# Slicing a tuple 
tuple1=(0,1,2,3,4,5)
print(tuple1[0:4]) # this will print from index 0 to 3 which means 0,1,2,3


# Tuple can not be append - this snippet will error AttributeError
tuple1=(1,2,3,4,5)
print(tuple1.append(6))


# Empty tuple
x=()

# Tuple with different data type
x = ("john",True,2.2,2)


# Printing in opposite way
a=(10,20,30,40,50)
a=a[::-1]
print(a)


# Slicing a tuple
a=(10,20,30,40,50)
print(a[2])

# Another example slicing with tuples and list inside.
a=(10,[20,30],40,50)
print(a[1][1])




##### Dictionary
# Dictionary is a object to store data values in key-value
# Dictionary is a collection that is ordered, changeable and does not allow duplicates


usernames = {
    "lydia":"lydiahalllie",
    "sarah":"sarah123",
    "max":"max_",
    "joe":"joejoe",
}


print(usernames)

print(usernames.keys())
print(usernames.values())

for key in usernames.keys():
    print(key + " - " + usernames[key])



# Let change a value
usernames["max"] = "max123"
print(usernames["max"])
print(usernames)


# Lets add a new item in the dictionary
usernames.update({"chloe":"chloe123"})
print(usernames)


# Lets delete a item in the dictionary
del usernames["max"]
print(usernames)


# Lets remove or delete the last item in the dictionary
usernames.popitem()
print(usernames)


# Lets copy a entire dictionary to a new dictionary variable
usernames_copy = usernames.copy()
print(usernames_copy)

# Lets remove or delete all items in the dictionary
usernames.clear()
print(usernames)



# Lets understand how dictionaries can not be duplicated
testdict = {
  "brand": "apple",
  "ram": "3",
  "year": 2020,
  "year": 2021
}

print(testdict) # this will print out {'brand': 'apple', 'ram': '3', 'year': 2021} as we see year was replaced



# Lets see some examples of dictionary methods 
# dictionary.values()
# dictionary.keys()
# dictionary.items()
# dictionary.update()
# dictionary.popitem()
# dictionary.copy()
# dictionary.clear()


# Lets print the keys
testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

print(testdict.keys())



# Lets use the method dictionary.items() - here it turn the dictionary in tuples
testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

print(testdict.items())





# Lets add a item in the dictionary and this item already exists
testdict = {
  "brand": "Samsung",
  "ram": "3",
  "Os": "Android",
  "year": 2020
}

testdict.update({'brand':'oppo' })
print(testdict)


# Lets delete a item and value in a dictionary
testdict = {'brand': 'oppo', 'ram': '3', 'Os': 'Android', 'year': 2020}
del testdict['brand']
print(testdict)




