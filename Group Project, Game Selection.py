#Game Selection by Diego, Marco, Julio
#Importing random
import random

#       Guess the Number Function
def game_one():
#         Function Variables    
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)  

    total_guesses = 0
    guess1 = 0
    guess2 = 0
#                   Guess the Number Prompt
    print("Welcome to Guess the Number! Your challenge is to guess correctly 2 random numbers.",
            "\nThese numbers range between (1 - 100) And your total amount of guesses will be shown!")

    while guess1 != num1:
        guess1 = int(input("\nGuess the first number!: "))

        if guess1 == num1:
            print("You got the first number!")
            total_guesses += 1
            break
        elif guess1 > num1:
            print("Incorrect, it's lower.")
            total_guesses += 1
        else:
            print("Incorrect, it's higher.")
            total_guesses += 1

    while guess2 != num2:
        guess2 = int(input("\nGuess the second number!: "))

        if guess2 == num2:
            print("You got the second number!")
            total_guesses += 1
            break
        elif guess2 > num2:
            print("Incorrect, it's lower.")
            total_guesses += 1
        else:
            print("Incorrect, it's higher.")
            total_guesses += 1
#                                              Function End
    print(f"\nCongrats at guessing the 2 numbers! \nHere's how many guesses you had: {total_guesses}")

#       Rock Paper Scissors Function
def game_two():
#       Function Variables    
    game_actions = ["rock", "paper", "scissors"]
    player_wins = 0
    computer_wins = 0
#       Rock Paper Scissors Prompt    
    print("Welcome to Rock Paper Scissors! You'll be challenging the computer in the",
            "game of Rock Paper Scissors. Whoever reaches 3 wins first wins the whole game!")

#       While Loop, counts wins
    while player_wins != 3 and computer_wins != 3:
        player_action = input("\nMake your choice! (rock, paper, scissors): ").lower()

        computer_action = random.choice(game_actions)

        if player_action == computer_action:
            print(f"You and the computer have selected {player_action}. It's a tie...")
        
        elif player_action == "rock":
            if computer_action == "scissors":
                print(f"You chose {player_action} while the computer chose {computer_action}.",
                "\nRock smashes scissors, you win!")
                player_wins += 1
            else:
                print(f"You chose {player_action} while the computer chose {computer_action}.",
                "\nPaper covers rock, you lose!")
                computer_wins += 1
        
        elif player_action == "paper":
            if computer_action == "rock":
                print(f"You chose {player_action} while the computer chose {computer_action}.",
                "\nPaper covers rock, you win!")
                player_wins += 1
            else:
                print(f"You chose {player_action} while the computer chose {computer_action}.",
                "\nScissors cuts paper, you lose!")
                computer_wins += 1
        
        elif player_action == "scissors":
            if computer_action == "paper":
                print(f"You chose {player_action} while the computer chose {computer_action}.",
                "\nScissors cuts paper, you win!")
                player_wins += 1
            else:
                print(f"You chose {player_action} while the computer chose {computer_action}.",
                "\nRock smashes scissors, you lose!")
                computer_wins += 1

        print(f"\nScore so far:",
            f"\nPlayer: {player_wins}",
            f"\nComputer: {computer_wins}")
#                                   Function End, Winner or Loser
    if player_wins == 3:
        print("\nCongratulations for winning 3 rounds against the mighty computer!")
    else:
        print("\nYou gave it a good try, but better luck next time.")



#       Main
print("Hello Player! Welcome to the arcade where we \nhave 2 fun filled games for you to enjoy infinitely!")

while True:
    print("\nYour two options for games are",
        "\n1. Guess the Number",
        "\n2. Rock Paper Scissors")
#   Asking User for Game choise
    while True:
        game_choice = input("Which game would you like to play?(1/2): ")
            
        if game_choice == "1":
            print("You've chosen Guess the Number!")
            break
        elif game_choice == "2":
            print("You've chosen Rock Paper Scissors!")
            break
        else:
            print("You've made an error, please choose one of the options given.")
            print()
            continue

#   Calls Functions based on User Choise
    if game_choice == "1":
        game_one()
    else:
        game_two()
#   Asks User if they want to play again
    play_again = input("\n Would you like to play again in one of these games?(y/n): ").lower()
    if play_again == "y":
        continue
    else:
        break
#   Exit
input("\n\nPress the enter key to exit.")
