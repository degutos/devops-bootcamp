# Lists

# normal list
list1 = [1, 2, 3, 4, 5]
print(list1[4])

# Changing a value in the list
numbers = [1, 2, 3, 4, 5]
numbers[4] = 6
print(numbers[4])

list1 = [1, 2, 3, 4, 5]
list1[0] = 10
print(list1)




# Showing Reverse List
list1=[2,5,3,1]
print(list1[::-1])


# Print first and item [3] in the list
list1 = [10, 11, 12, 13, 14]
print(list1[::3])



# Lists - Methods


countries = ["USA","Canada","India"]
countries.append("Spain")
countries.insert(2,"Italy")
print(countries)


# swapping values in the list - logical way

temp = countries[0]
countries[0] = countries[1]
countries[1] = temp
print(countries)


# swapping values back in the list - easy way
countries[0], countries[1] = countries[1], countries[0]
print(countries)



# Sort
countries.sort()
print(countries)

# Reverse
countries.reverse()
print(countries)


# Another sort examples:
ages = [56, 72, 24, 46]
ages.sort()
print(ages)

num = [4, 4, 3, 1]
num.sort()
print(num)


# Another example of append
list1 = [10, 20, 30, 40, 50]
list1.append(60)
print(list1)

# function max and min
list1=["Go","Java","C","Python"]
print(max(list1))

list1=["Go","Java","C","Rust"]
print(min(list1))

# Another example of Insert method, this will print:  UK 8 India Canada
list1=['UK','India','Canada']

list1.insert(1,8)

print(list1)


# how to remove one item of the list
list1 = [4, 4, 3, 1]
list1.pop(2)
print(list1)



# using len function 
list1=['h', 'e', 'l', 'l', 'o']
print(len(list1))



# How to find an average of a list of numbers

ages = [56, 72, 24, 46]
total = 0
for age in ages:
    total += age
average = total / len(ages)
print(average)


# How to sum a list
sum = 0
values = [2,9,1,7]
for number in values:
    sum += number
print(sum)

# Another way of sum
sum = 0
values = [2,9,1,7]
for number in values:
    sum = sum + number
print(sum)


# using continue to skip your looping run and go back to beginning of your loop for
for letter in 'KodeKloud':
    if letter == 'e':
        continue
    print('Letter : ' + letter)



# For within another For - printing 16 * asterisk 
for x in [0, 1, 1, 3]:
    for y in [0, 2, 1, 2]:
            print('*')


# Using enumerate function this will print position of the list and values  
list1 = [1, 2, 3, 4]
for i, j in enumerate(list1):
     print(i, j)

# Another example of enumerate and index
list1 = [1, 2, 3, 4]
for index, j in enumerate(list1):
     print(index, j)


# print all elements in the list from beginning to the end
list1 = [10, 11, 12, 13, 14]
print(list1[::1])

# print from element 1 (second in the list) to the end - B C D E
letters = ["A", "B", "C", "D", "E"]
print(letters[1:])

# print a list in opposite way
list1=[4,0,7,1]
print(list1[::-1])


# List of list - this example it will print 4 5 6 7
list1 = [[1,2,3,2,5],[4,5,6,7],[8,9,10]]
for i in list1:
      if len(i)==4:
        print(i)

# Append a number 15 at the end of a list - [10, 11, 12, 13, 14, 15]
list1 = [10, 11, 12, 13, 14]
list1.append(15)
print(list1)

# Printing a number in the position 0 within a list
list1 = [10, 11, 12, 13, 14]
print(list1[0])




# Slicing a list
letters = ["A","B","C","D","E"]
firstTwo = letters[0:2]
print(firstTwo)
# this will print A and B

print(letters[1:]) # this will print B,C,D,E

print(letters[:3]) # this will print A B C

print(letters[1:-1]) # this will print B C D

print(letters[1::]) # this will print B C D E

print(letters[:]) # this will print entire list

del letters[1:3] # this will delete list position number 1 and 2 which means delete B and C

print(letters)

del letters[:] # this will delete the entire list / array

print(letters)



# List can have different elements
list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[2:4]) # this will print "python 11 55 cat"

list1 = [1, 66, "python", [11, 55, "cat"], [ ], 2.22, True]
print(list1[0:4]) # this will print [1, 66, "python", [11, 55, "cat"]]

my_list = [0, 1, 2, 3, 4]
print(my_list[::-1]) # this will print entire list in opposite way

my_list = [0, 1, 2, 3, 4]
my_list.append("python")
print(my_list[2:]) # this will print [2, 3, 4, python]

my_list = [0, 1, 2, 3, 4]
print(my_list[-1]) # this will print 4

my_list = [0, 1, 2, 3, 4]
my_list.append("python")
b = my_list[1:]
print(b) # this will print [1, 2, 3, 4, python]

my_list = [0, 1, 2, 3, 4]
print(my_list[::3]) # this will print 0 and 3



