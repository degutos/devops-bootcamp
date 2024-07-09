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