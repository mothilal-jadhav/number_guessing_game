# Number Guessing Game

HI i am creating a very easy Number Guessing Game

## Backstory

i am not new to python but i am starting everything from scratch this time, so in this Journey i am starting from building very basic projects that will brush up my python knowledge. 

## Objective

so the objective project is building a game of guessing a number. the user will guess a number and if it is wrong then the output will be based on the difference between the answer and his guessed answer

like if the answer is 23 and the guessed number is 50 then the output will be too high and then the the user will be given a chance again where to guess and this time by his intution if the user guesses say 18 then it says so close to the answer and this iterates till the user guesses the number within the defined no. of chances.

## ALgorithm

The game starts by allowing the user to define a range by entering a lower and upper bound that is from A to B, as this game reminds me of binary search algo. lets say that the allowed chances will be the half of middle number. i.e, middle = (A+B)//2 and allowed = middle//2

1. Accept the Lower and Upper bound number from the user
2. Generate a random number in the selected range
3. Run a loop till allowed no. of chances will be equal to allowed.
        -> if the Guess is too high then print "The Guess is Too High"
        -> if the Guess is high but is close to the number then print "Too close try with a samller number"
        -> same with lower numbers, if the guess is too low then print "the Guess is too low" and if it is closer then print "Very Close. try with some upper number"

4. If the user reaches the allowed limit then print "Better Luck Next Time"

## implementation 

I will be using the **random** module of python

## Problems

If my lower bound is say 40 and upper bound is say 60 then the allowed chances would be 25 , which was not my initial thoght, this gives the player easy chances of winning.

another problem faced is the range from 40 to 60 is only 20 , so i wanted the middle no to be 10 and allowed chances as 5 but the logic went total opposite

## Solution

lets make the allowed chance in a single digit i.e, the allowed cahnce will be the mod by 10 of intial though like this if my allowed chance is 25 then the new_allowed will be 5. this makes the game intersting.

lets take middle as both half of the both numbers difference