import random


random.randint(1, 10)
random_num = 5
while True:
    guess = int(input("number:"))

    if guess > random_num:
        print("Too high Try again")
    elif guess < random_num:
        print("Too low, Try Again")

    else:
        print("Congratulations! You've guessed the number.")5








