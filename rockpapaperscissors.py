import random

# Define the function to play a single round of rock-paper-scissors
def rock_paper_scissors(rock,paper,scissors):
    #create an array of choices
    choices=[rock,paper,scissors]
    #the computer will randomly choose from the above choices
    computer_choice=random.choice(choices)
    #prompt the user to imput thier choice
    user_choices=input("Enter your choice(rock, paper,scissors): ")

    print("Computer chose: ",computer_choice)
    print("You chose:",user_choices)
#check if the users input is correct
    if user_choices not in choices:
            #not in is used to check if an element is not in the list
            print("invalid input")
    else:
            print("correct input")
    if computer_choice==user_choices:
            print("tie")
    elif(
            (computer_choice=="rock" and user_choices=="paper") or
            (computer_choice=="paper" and user_choices=="scissors") or
            (computer_choice=="scissors"and user_choices=="rock")
        
        ):
            print("user wins")
    else:
        print("computer wins")
#defin the main game function
def play_game(num_rounds):
    user_score = 0
    computer_score = 0
    #the _ is used when the value is not neeeded to iterate over
    
    
#determine the overall winner of the game
    if user_score > computer_score:
        print("You win the game!")
    elif computer_score > user_score:
        print("Computer wins the game!")
    else:
        print("It's a tie game!")

if __name__ == "__main__":
        num_rounds = int(input("Enter the number of rounds (3 or 5): "))
        if num_rounds not in [3, 5]:
            print("Invalid number of rounds. Please choose 3 or 5.")
        else:
            play_game(num_rounds)


