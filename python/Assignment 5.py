import random
print("welcome to stone,paper,scissor game:")
start =int(input("Enter 1 for play game:"))
def Game_option():
    print("enter 1 for stone:")
    print("enter 2 for paper:")
    print("enter 3 for scissor:")
ch =1
comp =0

Game_option()
ch = int(input())
comp = random.randint(1, 3)


while True:
    choice = int(input("User turn: "))
    while choice > 3 or choice < 1:
        choice = int(input("enter the input: "))
    if choice == 1:
        choice_name = 'stone'
    elif choice == 2:
        choice_name = 'paper'
    else:
        choice_name = 'scissor'

    print("user choice is: " + choice_name)
    print("\nNow its computer turn.......")

    comp_choice = random.randint(1, 3)

    while comp_choice == choice:
        comp_choice = random.randint(1, 3)

    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'

    print("Computer choice is: " + comp_choice_name)

    print(choice_name + " V/s " + comp_choice_name)
    if((ch == 1 and comp == 3) or (ch ==3 and comp ==1)):
        print("yes, i win the round")
        print("----score--")
        print(" c += 1")



    elif ((ch == 3 and comp == 1) or(ch == 1 and comp == 3)):
        print("yes!! i win this round")
        print("---score--")
        print("c += 1")

    else:
        print("uggh!! I lost this round")

    print("you what to play again (Y/N)")
    ans = input()

    if ans == 'n' or ans == 'N':
        break

    print("\nThanks for playing")







