import random

num = random.randint(1, 3)
player_choice = input("Choose Rock, Paper or Scissors\n>>> ").lower()
if player_choice == "rock" or player_choice == "paper" or player_choice == "scissors":
    match num:
        case 1:
            if player_choice == "paper":
                print("Rock vs Paper")
                print("You win!")
            elif player_choice == "rock":
                print("Rock vs Rock")
                print("It's a tie")
            else:
                print("Rock vs Scissors")
                print("You lose :(")
        case 2:
            if player_choice == "scissors":
                print("Paper vs Scissors")
                print("You win!")
            elif player_choice == "paper":
                print("Paper vs Paper")
                print("It's a tie")
            else:
                print("Paper vs Scissors")
                print("You lose :(")
        case 3:
            if player_choice == "rock":
                print("Scissors vs Rock")
                print("You win!")
            elif player_choice == "scissors":
                print("Scissors vs Scissors")
                print("It's a tie")
            else:
                print("Scissors vs Paper")
                print("You lose :(")
else:
    print("Bad decision")

#TODO add more choices not 3 but maybe 4?