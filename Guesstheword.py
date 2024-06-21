import random 
#library that we use in order to choose on random words from a list of words 
name = input("What is your name?")

#Here the user is asked to enter the name first.
print("Good Luck!" , name)
words = ['Reliance', 'Wipro', 'HDFC', 'TCS', 'Capgemini', 'ICICI', 'Accenture', 'Cognizant', 'Infosys']
 
#Function will choose one random word from the list 
word = random.choice(words)
print("Guess the characters")
guesses= ' '

# any number of turns can be used here
turns = 10
while turns > 0: 
    
    # all characters from the input word taking one at a time.
    for char in word:
        
            #comparing that character with the character in guesses
            if char in guesses:
                print(char, end="")
            else:
                print("_", end="")
                
               # Check if all characters guessed
    if all(char in guesses for char in word):
        print("\nYou win!")
        print("The word is:", word)
        break

    # Get user guess and update turns
    guess = input("\nGuess a character:")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", turns, 'more guesses')

if turns == 0:
    print("You lose!")
                    
                 
                        