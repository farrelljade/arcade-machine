import random
import sys

def guess_number(player, user_wins=0, game_count=0):
    while True:
        user = input(f"\n{player}, guess which number I'm thinking of... 1, 2, or 3?\n")

        if user not in ["1", "2", "3"]:
            print("Not allowed!")
            continue

        computer = random.choice("123")

        if user == computer:
            user_wins += 1
            game_count += 1
            print(f"\n{player} wins! 🎉\nI was thinking of {user}.")
        else:
            game_count += 1
            print(f"\nYou chose {user}\nI was thinking of {computer}")
            print(f"Better luck next time {player} 🥲")

        print(f"\nGame count: {game_count}\nwins: {user_wins}")

        win_percent = user_wins / game_count
        print(f"Your winning percentage is: {win_percent:.2%}")

        play_again = input("\nPlay again? (Y/N) ").lower()
        if play_again != "y":
            print(f"\nThanks for playing, {player}!")
            return

if __name__ == '__main':
    
    #user_name = input("What is your name: ")
    guess_number()
