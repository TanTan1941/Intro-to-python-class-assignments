import random  # Import the random module




def userGuess():
    # Function to get the user's choice
    while (True):
        # ask the user for input and simplify it
        strGuess = input("(r)ock, (p)aper, or (s)cissors? ").strip().lower()
        # Check if the input corresponds to "rock"
        if (strGuess == "r" or strGuess == "rock"):
            strReturn = "r"  # Set return value to "rock"
            print("You chose rock.")
            break  # Exit the loop
        # Check if the input corresponds to "paper"
        elif (strGuess == "p" or strGuess == "paper"):
            strReturn = "p"  # Set return value to "paper"
            print("You chose paper.")
            break  # Exit the loop
        # Check if the input corresponds to "scissors"
        elif (strGuess == "s" or strGuess == "scissors"):
            strReturn = "s"  # Set return value to "scissors"
            print("You chose scissors.")
            break  # Exit the loop
        else:
            # If the input is invalid, tell the user to try again
            print("That isn't a valid response. Try again.\n")
    return strReturn  # Return the user's choice

def compGuess():
    # Function to get the computer's choice
    arChoices = ["r", "p", "s"]  # List of possible choices
    strReturn = random.choice(arChoices)  # Randomly select one choice
    # Print the computer's choice
    if (strReturn == "r"):
        print("The computer chose rock.")
    elif (strReturn == "p"):
        print("The computer chose paper.")
    else:
        print("The computer chose scissors.")
    return strReturn  # Return the computer's choice

def whoWon(strU, strC):
    # Function to determine the winner
    if (strC == strU):
        # If both choices are the same, it's a tie
        print("It's a tie.\n")
        return "t"  # Return "t" for tie
    else:
        # Determine the winner based on user and computer choices
        if (strU == "r"):
            if (strC == "p"):
                print("Computer wins!\n")
                return "c"  # Return "c" for computer wins
            else:
                # Computer chose scissors
                print("You won!\n")
                return "u"  # Return "u" for user wins
        elif (strU == "p"):
            if (strC == "r"):
                print("You won!\n")
                return "u"  # Return "u" for user wins
            else:
                # Computer chose scissors
                print("Computer wins!\n")
                return "c"  # Return "c" for computer wins
        else:
            if (strC == "r"):
                print("Computer wins!\n")
                return "c"  # Return "c" for computer wins
            else:
                # Computer chose paper
                print("You won!\n")
                return "u"  # Return "u" for user wins


# Assigning variables for parameters
intCompScore = 0

intUserScore = 0

def game(CompScore, UserScore):
    #defining a function for scoring
    while (CompScore < 3 and UserScore < 3):
        #using a while loop for multiple rounds
        winner = (whoWon(userGuess(), compGuess()))
        # calling the whowon function

        if (winner == "u"):
            #taking results from the strreturn of who won
            UserScore += 1 #appending the score
            print(f"Your Score:{UserScore}, Computer's Score:{CompScore}")# letting the user keep track of the score
            print("congrats! You won!") # informing the user that they won the round
        elif (winner == "c"):
            CompScore += 1 #appending the score
            print(f"Your Score:{UserScore}, Computer's Score:{CompScore}") # letting the user keep track of the score
            print("The computer won!") # informing the user that they lost the round
        elif (winner == "t"):
            print(f"Your Score:{UserScore}, Computer's Score:{CompScore}") #informing the user that the round was a tie

    if (UserScore == 3 or CompScore == 3):
        # using an if statement to say the final scores and return the answer variable in the event the user or computer got a score of 3
        print(f"The final score is User:{UserScore} and Computer:{CompScore} \n")
        answer = input("Would you like to play Rock, Paper, or Scissors?(yes, no) ").lower()
        return answer


again = game(intCompScore, intUserScore)
#assigning the initial call of the game function to a variable
if (again == "yes"):
    #using an if statement to either call the function again or end the progam base on the users input
    print(game(intCompScore, intUserScore))
elif (again == "no"):
    print("Thanks for playing!")