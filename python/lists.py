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
