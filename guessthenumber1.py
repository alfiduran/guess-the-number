import random #packages/libraries/modules
n = random.randint(1, 99)

guess = int(input("Enter a number from 1 to 99: "))

while (guess != n):
    if(guess > n):
        print("Guessing number is big! ")
        guess=int(input("Enter a smaller Number : "))
        continue
    elif(guess < n):
        print("Guessing number is small !")
        guess=int(input("Enter a higher Number : "))
        continue
if(guess== n):
    print("You guessed the correct the number! Well done!!")
print("Random number is: " )
print(guess)
