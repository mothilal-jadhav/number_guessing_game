import random

print("Hey Buddy! Ready to Guess a number. Better guess the number within the allowed Chances")

low = int(input("enter the lower bound of the range you want to guess: "))
high = int(input("enter the upper bound of the range you want to guess: "))

middle = (high - low)//2

allowed = middle//2

new_allowed = allowed%10

number = random.randint(low,high)

guess_counter = 0

while guess_counter < new_allowed:
    guess_counter += 1
    print(f"you only have {new_allowed} chances be aware")
    guess = int(input("lets take a Guess: "))

    if guess == number:
        print("Hurray! you guessd it right ")
        break

    elif guess > number:
        print("Oo! guess is little bit high , try with a lower number")

    elif guess < number:
        print("Oo! guess is little bit low, try with a higher number")

if guess_counter == new_allowed:
    print(f"Bad Luck Buddy! Better Luck in the Next Try. The correct number is {number}")
