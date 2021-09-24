import random
import math
#Inputs
lower = int(input("Enter Lower number:- "))
 
upper = int(input("Enter Upper number:- "))
 
x = random.randint(lower, upper)
print("\n\tYou've only ",
       round(math.log(upper - lower + 1, 2)),
      " chances to guess the integer!\n")
 
# Initializing the number of guesses.
count = 2
 
#calculation of minimum number of
while count < math.log(upper - lower + 1, 2):
    count += 1
    guess = int(input("Guess a number:- "))
 
    #Testing condition.
    if x == guess:
        print("Congratulations you did it in ",
              count, " try")
        # Once guessed, loop will break
        break
    elif x > guess:
        print("You guessed too low!")
    elif x < guess:
        print("You Guessed too high!")
 
# output.
if count >= math.log(upper - lower + 1,2):
    print("\nThe number is %d" % x)
    print("\t Good luck next time!")

 












