import random

print("Hey Buddy! Ready to Guess a number. Better guess the number within the allowed Chances")

low = int(input("enter the lower bound of the range you want to guess: "))
high = int(input("enter the upper bound of the range you want to guess: "))

middle = (low+high)//2

allowed = middle//2

number = random.randint(low,high)

guess_counter = 0

while guess_counter < allowed:
    guess = int(input("lets take a Guess: "))

    if guess == number:
        print("Hurray! you guessd it right ")
        break

    elif guess > number*2:
        print("Oo! guess is too high, try with a lower number")

    elif guess < number//2:
        print("Oo! guess is too low, try with a higher number")

    elif guess > number and guess<number*2:
        print("Too Close lets try with a lower number")

    elif guess < number and guess >number//2:
        print("Too Close lets try with a higher number")

print("Bad Luck Buddy! Better Luck in the Next Try")
