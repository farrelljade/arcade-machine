import random
import sys
from enum import Enum

def rps(player=None):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins, python_wins

        class RPS(Enum):
            Rock = 1
            Paper = 2
            Scissors = 3

        user_choice = input("\nEnter...\n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

        if user_choice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            return play_rps()

        computer_choice = random.choice("123")
        computer = int(computer_choice)
        user_choice = int(user_choice)

        print(f"You chose {RPS(user_choice).name}.")  # the number chosen will also print the name in the enum class
        print(f"Python chose {RPS(computer).name}.")  # the number chosen will also print the name in the enum class

        def decide_winner(user, comp):
            nonlocal player_wins, python_wins

            if user == 1 and comp == 3:
                player_wins += 1
                return "🎉 You win!"
            elif user == 2 and comp == 1:
                player_wins += 1
                return "🎉 You win!"
            elif user == 3 and comp == 2:
                player_wins += 1
                return "🎉 You win!"
            elif user == comp:
                return "😲 That's a draw!"
            else:
                python_wins += 1
                return "🥲 You lose!"

        game_result = decide_winner(user_choice, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"Game Count: {game_count}")
        print(f"\nThe scores are:\n{player}: {player_wins} Python: {python_wins}.")

        while True:
            play_again = input("Play again? (Y)(N)\n").lower()
            if play_again not in ["y", "n"]:
                continue
            else:
                break

        if play_again == "y" or play_again == "yes":
            return play_rps()
        else:
            print("\nThanks for playing!")
            return
            #sys.exit("Bye!")

    play_rps()  # Call the play_rps function directly

if __name__ == '__main__':
    rps()  # Call the rps function when the script is run
