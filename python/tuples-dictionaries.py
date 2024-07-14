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
