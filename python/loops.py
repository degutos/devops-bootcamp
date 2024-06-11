# Loops

# Loops - While


secret_number = 3
guess = int(input("Guess a number: "))
while guess != secret_number:
    guess = int(input("Guess a number: "))
else:
    print("Congratulations, you got it!")




# Loops - For


for i in range(5):
   print(i)



for i in range(10):
    if(i == 3):
        break
    print("i is: ", i)
