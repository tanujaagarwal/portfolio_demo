import random
target = random.randint(1,100)
while True:
    userChoice = input("Guess the target or Quit")
    if(userChoice == "Quit"):
        break
    
    userChoice = int(input("Guess the target or Quit(Q):"))
    if (userChoice == target):
        print(" Success : Correct Guess")
        break

    elif (userChoice>target):
        print("your number was too small")
else:
    (userChoice<target)
    print("your number was too large")
    print("--Game Over--")
    