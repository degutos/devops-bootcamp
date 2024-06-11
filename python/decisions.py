# Making Decisions

# Comparison operators

# ==    !=      >       >=      <       <=


# Lets use operator == Equal

print(2 == 2)

print(2 == 4)

print("Hello!" == "Hello!")

print(4 == (2 * 2))


# Lets use operator != Not Equal

print(2 != 2)

print(2 != 4)

print("Hello!" != "Hello!")

print(4 != (2 * 2))



# Lets use operator > grater than

print(4 > 2)

print(2 > 4)

print(2 > 2)


cost_of_apple = 2
cost_of_banana = 3

print(cost_of_apple > cost_of_banana)


# IF statement

age = int(input("How old are you? "))

if age >= 18:
    print("You are an adult! ")


if age >= 18:
    if age == 18:
        print("You are exactly 18 years old! ")
    else:
        print("You are older than 18 years old")




age1 = 24
age2 = 16

if(age1 >= 18 and age2 >= 18):
    print("You are both adults")
elif(age1 >= 18 or age2 >=18):
    print("One of you is adult")
else:
    print("You are both children")




