import random

def higherLower(player_name):
    keep_guessing = True
    guesses = 0

    comp_choice = random.randint(1, 100)
    user_choice = int(input("\nSelect a number between 1 - 100: "))

    while keep_guessing:
        guesses += 1
        if user_choice == comp_choice:
            print(f"\nCongratulations {player_name}! You guessed the computers number.")
            print(f"It took you {guesses} guesses.")
            play_again = input("Play again? ").lower()
            if play_again in ["yes", "y"]:
                higherLower()
            elif play_again in ["no", "n", ""]:
                break
        elif user_choice < comp_choice:
            print("Guess higher")
        elif user_choice > comp_choice:
            print("Guess lower")

        user_choice = int(input("Guess again: "))

if __name__ == '__main__':
    higherLower()