import random

# Define the function to play a single round of rock-paper-scissors
def rock_paper_scissors(rock, paper, scissors):
    # Create an array of choices
    choices = [rock, paper, scissors]
    # The computer will randomly choose from the above choices
    computer_choice = random.choice(choices)
    # Prompt the user to input their choice
    user_choice = input("Enter your choice (rock, paper, scissors): ")

    print("Computer chose:", computer_choice)
    print("You chose:", user_choice)
    
    # Check if the user's input is correct
    if user_choice not in choices:
        print("Invalid input")
        return "invalid"
    
    if computer_choice == user_choice:
        print("It's a tie!")
        return "tie"
    elif (
        #this is a set of conditional statements
        (computer_choice == "rock" and user_choice == "paper") or
        (computer_choice == "paper" and user_choice == "scissors") or
        (computer_choice == "scissors" and user_choice == "rock")
    ):
        print("User wins")
        return "user"
    else:
        print("Computer wins")
        return "computer"

# Define the main game function
def play_game(num_rounds):
    user_score = 0
    computer_score = 0

    for _ in range(num_rounds):
        #_ is used when the value that is meant to be iterated is not needed
        result = rock_paper_scissors('rock', 'paper', 'scissors')
        if result == "tie":
            print("It's a tie!")
        elif result == "computer":
            print("Computer wins this round!")
            computer_score += 1
        elif result == "user":
            print("You win this round!")
            user_score += 1
        elif result == "invalid":
            continue

        print("User: ",user_score ,  "Computer: ",computer_score)

        if user_score >= 5 or computer_score >= 5:
            break

    # Determine the overall winner of the game
    if user_score > computer_score:
        print("You win the game!")
    elif computer_score > user_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
    #the above code means that it allows python code to run when the scrips is excecuted directly and not when the script is imported
    num_rounds = int(input("Enter the number of rounds (3 or 5): "))
    if num_rounds not in [3, 5]:
        print("Invalid number of rounds. Please choose 3 or 5.")
    else:
        play_game(num_rounds)
