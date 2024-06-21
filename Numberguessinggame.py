import random
import math
#Taking inputs
lower = int(input("Enter Lower bound:"))

#Taking inputs
upper = int(input("Enter upper bound:"))

#generatting random number between the lower and the upper
x = random.randint(lower,upper)
print("\n\tYou've only", round(math.log(upper-lower +1, 2)), "chances to guess the integer!\n")

#Initialising the number of guesses.
count = 0

#for calculation of minimum number guesses depends upon the range
while count < math.log(upper-lower+1,2):
    count+=1
    
    #Taking guessing number as input
    guess = int(input("Guess a number:"))
    
    #Condition testing
    if x == guess:
        print ("Congratulations you guessed it in" , count, "try")
        
        #Once guessed, loop will break 
        break
    elif x > guess:
        print("You guessed too small")
    elif x < guess:
        print ("You guessed too high!")
        
        #If guessing is more than required guesses, shows this output.
        if count >= math.log(upper-lower+1,2):
            print ("\The number is %d" % x)
            print("\tBetter luck next time!")
            