import random

num=random.randint(1,20)

while True:
    guess=int(input("Guess a number between 1 and 20 :"))
    if guess==num:
        print("You have guessed the  correct number!!!")
    elif guess>=num+1 or guess>=num+2 or guess>=num+3:
        print("You are close!!!")
    elif guess >= num - 1 or guess >= num - 2 or guess >= num - 3:
        print("You are close!!!")
    elif guess>num:
        print("You have guessed a higher number")
    elif guess<num:
        print("You have guessed a smaller number")
