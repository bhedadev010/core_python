import random

num=random.randint(1,100)

while True:
    guess=int(input("Guess a number between 1 to 100:"))
    if guess==num:
        print("You guess is correct!!!")
    elif guess>num:
        print("You guessed a greater number")
    elif guess<num:
        print("You guessed a smaller number")