dEmployees = {
    #creating initial list
    "1000": {"Fname": "Tanner", "Lname": "Blattemberg", "Age": "19", "Position": "Tech I", "Salary": "100,000"},

    "1001": {"Fname": "John", "Lname": "doe", "Age": "25", "Position": "Unknown", "Salary": "50,000"}
}

def AddEmp():
    # function do collect dictionary attributes
    EmpID = input("what is their 4 digit employee ID? \n")
    Fname = input("Give the first name \n")
    Lname = input("Give the last name \n")
    Age = input("What is their age \n")
    Position = input("What is their position/role at the company \n")
    Salary = input("What is their yearly salary? \n")
    print("Thank You, appending now!")    
    #appending the dictionary
    dEmployees[EmpID] = {"Fname": Fname, "Lname": Lname, "Age": Age, "Position": Position, "Salary": Salary}
    #showing the result
    print(f"""Here is the updated Employee List
          {dEmployees}""")
    
def ChkEmp():
    #function to check the dictionary
    print("Coming right up! \n")
    print(dEmployees)


def RmEmp():
    #functiom to remove an employee from the dictionary
    EmpID= input("Please give the employee ID of the employee you'd like to remove. \n")
    #using the pop method to remove
    dEmployees.pop(EmpID)
    print(f"""Employee removed, here is your new employee list. #showing updated list
          {dEmployees}""")
    
def Main():
    #main function to call the others
    print("#" * 20, "Welcome to the Employee Management System".center(40), "#" * 20)#welcome screen followed with options
    print("""What would you like to do?
    1. Add an employee
    2. Remove an employee
    3. Check the Employee list \n""")
    #assigning the input to a variable
    Option = input("Please select \n")

    if (Option == "1"): #using an if statement to call a function based on input
        AddEmp()

    elif (Option == "2"):
        RmEmp()
    
    elif (Option == "3"):
        ChkEmp()
    else:
        print("Invalid choice")


while True:
    # while statement to let the user continue calling functions until they say they dont want to anymore.
    Main()

    Again = input("Would you like to do something else?(yes, no) \n".lower)
    if (Again != "yes"):
        print("Thanks for using the tool!")
        break
