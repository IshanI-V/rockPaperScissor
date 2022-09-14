import random

# print multi-line instructions
print("The rules of winning this game is simple \n")
print("You have to abide by the rules mentioned below\n" + " Rock vs paper-> paper wins"
      + "Rock vs scissor -> Rock wins" + "scissor vs paper -> paper wins")

chance = True
user_score = 0
comp_score = 0

while chance:
    print("Your score: ", user_score, "Computer score: ", comp_score)
    print("\nDo you want to play ? (y/n): ")
    ans = input().lower()
    if ans == "n":
        chance = False
        print("Thanks for playing")

    elif ans == "y":
        chance = True
        print("Choose for yourself \n 1 for Rock , \n 2 for Scissor, \n 3 for Paper")

        # take input from user
        choice = int(input("Your turn, enter your choice: "))

        while choice > 3 or choice < 1:
            choice = int(input("Enter your choice again , Make sure its either 1, 2, 0r 3 :  "))

        if choice == 1:
            choice_name = "Rock"
        elif choice == 2:
            choice_name = "Paper"
        else:
            choice_name = "Scissor"

        # print user choice
        print("so your choice is: " + choice_name)
        print("now its computer turn ...")

        # computer chooses randomly any number 1, 2, or 3 using randint method of random module
        comp_choice = random.randint(1, 3)
        while comp_choice == choice:
            comp_choice = random.randint(1, 3)

        if comp_choice == 1:
            comp_choice_name = 'Rock'
        elif comp_choice == 2:
            comp_choice_name = 'Paper'
        else:
            comp_choice_name = 'Scissor'

        print("computer chooses " + comp_choice_name.upper())
        print(choice_name + " V/s " + comp_choice_name)

        # now check for Draw
        if choice == comp_choice:
            print("Draw => ", end=" ")
            result = "Draw"
        elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
            print("Paper Wins => ", end="")
            result = "Paper"
        elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
            print("Rock wins => ", end="")
            result = "Rock"
        else:
            print("Scissor wins =>", end="")
            result = "Scissor"

        # printing either user or computer
        if result == "Draw":
            print("\n\n<== IT'S A TIE ==>\n\n")
        elif result == choice_name:
            print("\n\n==> YOU WIN ! ==>\n\n")
            user_score += 1
        else:
            print("\n\n==> COMPUTER WINS! ==>\n\n")
            comp_score += 1
    else:
        print("""It looks like you have entered invalid input
        make sure that your answer is either n for exit or y for continue playing..""")
