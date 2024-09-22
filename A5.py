# start with some $$
from sys import float_repr_style

flSavBal = 500.99
flChkBal = 100.31

# Welcome UI Message
print("#"*80)
print("Welcome to the ATM")
print("#"*80)

# create a loop for the program
while (True):

    #Show the menu options
    print("Choose an option: 1 - Deposit, 2 - With, Check Balance - 3")
    # Ask the user for their choice
    strMenu = input("what do you want to do?")

    if (strMenu == "1"):
        print(f"Current Balance Checking: {flChkBal}, Savings: {flSavBal}".rjust(200))
        # ask for account
        AccDep = input("""which account would you like to deposit to? Pleas say "checking" or "savings" """)
        # turnig input to variables
        DepAmount = input("How much would you like to deposit? ")
        # converting input
        DepAmount = float(DepAmount)
        if (AccDep == "checking"):
            #adding user amount and user balance
            AfterDep = DepAmount + flChkBal
            # appending the balance
            flChkBal = AfterDep
            # printing new balance
            print(f"Your new checking balance is {AfterDep:.2f}")

            #printing account balance on the right of the terminal
            print(f"New Balance Checking: {flChkBal}, Savings: {flSavBal}".rjust(200))

        if (AccDep == "savings"):
            # showing current balance and assigning inputs as variables then adding and appending balance
            print(f"Current Balance Checking: {flChkBal}, Savings: {flSavBal}".rjust(200))
            AfterDep = DepAmount + flSavBal
            flSavBal = AfterDep
            # showing the user the new balance
            print(f"Your new savings balance is {AfterDep:.2f}")



    elif (strMenu == "2"):
        print(f"Current Balance Checking: {flChkBal}, Savings: {flSavBal}".rjust(200))
        # ask for account and assigning inputs as variables
        AccWith = input("""which account would you like to withdraw from? Pleas say "checking" or "savings" """)
        WithAmount = input("How much would you like to withdraw? ")
        # converting the users requested amount to float format
        WithAmount = float(WithAmount)
        # using an if statement for both possible answers
        if (AccWith == "checking"):
            #subracting the inputted amount from the balance
            AfterWith = flChkBal - WithAmount
            # appending the balance
            flChkBal = AfterWith
            # an if statement for if the withdrawal will make the amount less than 0
            if flChkBal < 0:
                #changing the new negative balance back to the previous balance
                AfterWith = flChkBal + WithAmount
                # informing the user of the mistake and showing the current balance
                print("You may not withdraw more that your current balance. \n")
                print(f"Your checking balance is {AfterWith:.2f}")
            # if the amount is not put under zero it will continue without reverting and say the new balance
            elif flChkBal >= 0:
                print(f"Your new checking balance is {AfterWith:.2f}")

        if (AccWith == "savings"):
            # doing the subtracttion and appending the balance
            AfterWith = flSavBal - WithAmount
            flSavBal = AfterWith
            #checking if the balance would be below zero otherwise continuing the change
            if flSavBal < 0:
                AfterWith = flSavBal + WithAmount
                flSavBal = AfterWith
                print("You may not withdraw more that your current balance. \n")
                print(f"Your new Savings balance is {AfterWith:.2f}")
            elif flSavBal >= 0:
                print(f"New Balance Checking: {flChkBal:.2f}, Savings: {flSavBal:.2f}".rjust(200))
                print(f"Your new savings balance is {AfterWith:.2f}")
    # showing the balance
    elif (strMenu == "3"):
            print(f"Your balance in your savings is {flSavBal:.2f}, Your balance in your checking is {flChkBal:.2f}")


    # informing the user of invalid input
    else:
        print ("Sorry - that's not a valid choice \n")
    #asking the user if they would like to continue
    strMore = input("Would you like another transaction?")
    # if the answer is not equal to yes then the while loop will break
    # using string.lower() to prevent common user error
    if (strMore.lower() != "yes"):
        break