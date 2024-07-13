# sample of functions 



# Lets create a small function that gets the user input and add it to a number
# we passed to the function 

def add_number(num):
    return int(input()) + num

print(add_number(5))



# Function sum 2 numbers passed to the function 

def add_func(num1, num2):
    return num1 + num2

print(add_func(5,12))


# Function sum 2 numbers passed to the function 


def add_func(num1,num2):
    return num1 + num2

print(add_func(5,num2=2))


# Function receive a list of names and print the tallest person chosen will be the first person's name

def my_function(*friends):
    print('The tallest person is ' + friends[0])

my_function("john","ella","mark")



# Function receive a list and change the third item in the list to 5

nums=[7,4,1,8]
def change_third_item(list):
    list[2] = 5
   # return list

change_third_item(nums)
print(nums)


# Function that receive a number 0 as parameter and add 3 and return result
a=0
def add_three(a):
    return a+3

result=add_three(a)
print(result)



# Function that receives a number 3 as parameter in the variable "a" and sum variable "a" with number 3. At the beginning we need declare a variable a=0.
a=0
def add_three(a):
    return a+3

result=add_three(3)
print(result)


# function that receive a name and a age through the parameters, although the function should have a default value of age=19. The function should pass a name and age=18.
# in this case the default variable/parameter in the function, age=19 is the default value only when there is no parameter passed when calling the function.

def print_name_age(name, age=19):
    print(name,age)

print_name_age("john",18)


# Function that receives a name and concatenate with a surname Mark

def fullname_func(fname):
    print(fname + " Mark")

fullname_func("John")


# Function that receives a name and surname and print

def fullname_func(fname,lname):
    print(fname + " " + lname)

fullname_func("John", "Mark")


# Function receive a number 3 as parameter and return the sum of 5 + the number passed to the function

def my_function(x):
    return 5 + x

print(my_function(3))


# Function square 
#
def square(i):
    j = i * i 
    return j
print(square(3)) 



 
 # Function true or false

def is_true(a): 
  return bool(a) 

result = is_true(6<3) 
print("The result is", result)
