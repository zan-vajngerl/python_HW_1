print("Enter a number between 1 and 100 and the program will count to that number. Except for numbers divisible by 3 it will say 'fizz', and for numbers divisible by 5 it will say 'buzz'.")
print("For numbers divisible by both it will say 'Fizzbuzz'")

while True:
    counter = int(input("Enter a number: "))
    if 0 < counter < 100:
        break
    else: print("Please enter a number between 1 and 100")

fizzbuzz_number = 1

for x in range(counter):
    if fizzbuzz_number%15 == 0:
        print("fizzbuzz")
    elif fizzbuzz_number%5 == 0:
        print("buzz")
    elif fizzbuzz_number%3 == 0:
        print("fizz")
    else: print(fizzbuzz_number)

    fizzbuzz_number += 1