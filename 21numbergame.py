def nearestMultiple(num):
    if num >= 4:
        near = num + (4 - (num % 4))
    else:
        near = 4
    return near

def lose1():
    print("\n\nYOU LOSE !")
    print("Better luck next time !")
    exit(0)

def check(xyz):
    for i in range(1, len(xyz)):
        if (xyz[i] - xyz[i - 1]) != 1:
            return False
    return True

def start1():
    xyz = []
    last = 0
    while True:
        print("Enter 'F' to take the first chance.")
        print("Enter 'S' to take the second chance.")
        chance = input('> ')

        if chance == "F":
            while True:
                if last == 20:
                    lose1()
                else:
                    print("\nYour Turn.")
                    print("\nHow many numbers do you wish to enter?")
                    try:
                        inp = int(input('> '))
                    except ValueError:
                        print("Invalid input. You are disqualified from the game.")
                        lose1()

                    if inp > 0 and inp <= 3:
                        comp = 4 - inp
                    else:
                        print("Wrong input. You are disqualified from the game.")
                        lose1()

                    print("Now enter the values")
                    for _ in range(inp):
                        try:
                            a = int(input('> '))
                        except ValueError:
                            print("Invalid input. You are disqualified from the game.")
                            lose1()
                        xyz.append(a)

                    last = xyz[-1]

                    if check(xyz):
                        if last == 21:
                            lose1()
                        else:
                            for j in range(1, comp + 1):
                                xyz.append(last + j)
                            print("Order of inputs after computer's turn is: ")
                            print(xyz)
                            last = xyz[-1]
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()

        elif chance == "S":
            comp = 1
            last = 0
            while last < 20:
                for j in range(1, comp + 1):
                    xyz.append(last + j)
                print("Order of inputs after computer's turn is:")
                print(xyz)
                last = xyz[-1]
                if last == 20:
                    lose1()
                else:
                    print("\nYour turn.")
                    print("\nHow many numbers do you wish to enter?")
                    try:
                        inp = int(input('> '))
                    except ValueError:
                        print("Invalid input. You are disqualified from the game.")
                        lose1()

                    print("Enter your values")
                    for _ in range(inp):
                        try:
                            num = int(input('> '))
                        except ValueError:
                            print("Invalid input. You are disqualified from the game.")
                            lose1()
                        xyz.append(num)

                    last = xyz[-1]
                    if check(xyz):
                        near = nearestMultiple(last)
                        comp = near - last
                        if comp == 4:
                            comp = 3
                    else:
                        print("\nYou did not input consecutive integers.")
                        lose1()
            print("\n\nCONGRATULATIONS !!!")
            print("YOU WON !")
            exit(0)

        else:
            print("Wrong choice")

game = True
while game:
    print("Player 2 is Computer.")
    print("Do you want to play the 21 number game? (Yes / No)")
    ans = input('> ')
    if ans.lower() == 'yes':
        start1()
    else:
        print("Do you want quit the game?(yes / no)")
        nex = input('> ')
        if nex.lower() == "yes":
            print("You are quitting the game...")
            exit(0)
        elif nex.lower() == "no":
            print("Continuing...")
        else:
            print("Wrong choice")
