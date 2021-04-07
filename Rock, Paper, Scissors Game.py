# This program allows the computer to play rock paper scissors with the user

# Imports the random module
import random


# Defines the main function
def main():
    # Defines the rps function
    def rps():
        # This line uses gets a random number between 1 and 3 and sets that number equal to choice
        choice = random.randint(1, 3)
        # If the number that is chosen is 1, that means the computer's choice is Rock
        if choice == 1:
            choice = "Rock"
        # If the number that is chosen is 2, that means the computer's choice is Paper
        elif choice == 2:
            choice = "Paper"
        # If the number that is chosen is 3, that means the computer's choice is Scissors
        elif choice == 3:
            choice = "Scissors"
        # This returns whatever the computer choice is to the rps function
        return choice

    # This defines the ask_user function
    def ask_user():
        # This line lets the user enter either Rock, Paper, or Scissors
        user = input("What would you like to throw?(Rock, Paper, or Scissors : ")
        # This returns the contents of the user variable to the ask_user function
        return user

    # Sets the computer_choice variable to 0 for the while loop
    computer_choice = 0
    # Sets the user_choice variable to 0 for the while loop
    user_choice = 0
    # Sets the go variable to Y for the while loop
    go = "Y"

    # Calls the while loop saying that as long as either the computer_choice variable and the user_choice variable are
    # equal or the go variable equals y the loop will run
    while computer_choice == user_choice or go == "Y":

        # Gets the computer choice of either Rock, Paper, or Scissors and assigns it to the computer_choice variable
        computer_choice = rps()
        # Gets the users choice of either Rock, Paper, or Scissors and assigns it to the user_choice variable
        user_choice = ask_user()

        # Prints the computers choice
        print("The Computer choices", computer_choice)

        # Sets the possibilities and prints the outcomes
        if computer_choice == "Rock" and user_choice == "Paper":
            print("Congratulations, You beat the computer")
        elif computer_choice == "Rock" and user_choice == "Scissors":
            print("You lost, Sorry try again though")
        elif computer_choice == "Paper" and user_choice == "Scissors":
            print("Congratulations, You beat the computer")
        elif computer_choice == "Paper" and user_choice == "Rock":
            print("You lost, Sorry try again though")
        elif computer_choice == "Scissors" and user_choice == "Rock":
            print("Congratulations, You beat the computer")
        elif computer_choice == "Scissors" and user_choice == "Paper":
            print("You lost, Sorry try again though")
        else:
            print("You and the computer tied! Throw again")
        # Ask the user if he or she would like to continue.
        go = input("Would you like to to go again (Y or N): ")
    print("Thanks for playing")


main()
