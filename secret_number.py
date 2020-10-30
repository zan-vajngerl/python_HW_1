print("Guess the secret number between 1 and 1000 and the prize is yours! You get 10 tries (Disclaimer: there is no prize)")

import random
SECRET = random.randint(1, 1000)
try_number = 1


for x in range(10):
    guess = int(input(f"Try number {try_number}: "))
    try_number += 1
    if guess == SECRET:
        print (f"Good job!")
        break
    elif guess > SECRET:
        print("Nope! Too high.")
    else:
        print("Nope! Too low")


print(f"The number we were looking for was {SECRET}")