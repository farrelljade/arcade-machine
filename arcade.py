from guessnumber import guess_number
from rps import rps

player_name = input("\nWhat is your name: ")

def player_choice():

    while True:
        choice = input("\nWhat do you want to play.\n1 - Rock, Paper, Scissors.\n2 - Guess the number.\n3 - Quit.\n")        
        if choice == "1":
            rps(player_name)
        elif choice == "2":
            guess_number(player_name)
        elif choice == "3":
            print("Thank you for playing at the Arcade! Goodbye 👋")
            break
        else:
            print(f"Sorry {player_name()}, only options 1, 2, or 3 are available right now.")
            return player_choice() 

player_choice()