# Python basics - Hello world!


# Function print
print("Hello World !")

print("\n") # this will print a enter character which means a new line
print("Hello world in two lines");\
print("and this is the second line")

# print function with several arguments in one function
print("Hello","World!", "with several arguments", "in one print function")


# Lets use print with argument to replace the enter to empty string
print("Hello!", end="");\
print("Python is great")


# Variables

# Literals

#  
# - Integer 
# - Octal numbers
# - Hexadecimal 
# - Float 
# - Strings
# - Booleans 


# Lets see how to use variables

amount_of_apples = 2
cost_of_apple = 5

print(amount_of_apples * cost_of_apple)

# Lets increase a variable

cost_of_apple = cost_of_apple + 2
print(cost_of_apple)

# Shortcut to increase a variable
cost_of_apple += 2
print(cost_of_apple)

# Lets use input
# when we use input the program stop and prompt something to user enter something in the console
# input function is always a string

feeling = input("How are you feeling today? ")
print("I am feeling " + feeling)

favorite_color = input("What is your favorite color? ")
print("Your favorite color is " + favorite_color)

# the variable age captured on input function is of type string, we need to use print function converting the variable
# age to integer to give us condition to calculate the number.
age = input("How old are you? ") 
print(int(age) - 10)

# another way to store the variable age as integer we can do
# age = int(input("How old are you? "))
# print(age - 10)
