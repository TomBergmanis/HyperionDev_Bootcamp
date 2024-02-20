import math # importing the math functions 

# reuploading to include comments as per the feedback from previous submissions
""" the user chooses which calculation via two input statements
    if the user chooses investment ... output what the user has chosen.
    nested within the investment if statement ...
     user inputs their deposited amount, their interest rate, years they want to invest for.
      the user then chooses either simple or compound. if user chooses simple ... run simple calc 
       if the user runs compound run compound calc run.
       output the answer in terminal.
    if the user chooses bond ... 
    nested within the bond if statement...
    run bond inputs then calc then outout answer to terminal. 

    this project runs based on a compliant user i.e. one that enters the right information. 
    this project could deal with a non-compliant user using a try and except statement at each user input stage. 
"""

print("\ninvestment - to calculate the amount of interest you'll earn on your investment\n")
print("bond       - to calculate the amount you'll have to pay on a home loan\n")
# below prompts the user to enter the specific word we could make use of an try except statement to avoid the user entering the wrong information
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")
#trying to think ahead of the user so that the program runs with no errors 
user_choice = user_choice.lower() #convert all answers to lowercase so that the if statement can run.

if user_choice == "investment":

    print("You chose investment.") # the below makes sure we get the right datatype and makes it clear which option the user chose. 
    #below takes the user input information and stores in the variables for later use. 
    deposit = int(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate here: "))
    years = int(input("Enter the number of years you plan to invest: "))
    interest = str(input("Do you want 'simple' or 'compound' interest? ")) # user must specify a string for this to work
    interst = interest.lower() # converts all inputs for interest variable to lower

    # a nested if statement for the user to specify simple or compound interest rates. 
    # if-else statement as there are only two options 
    if interest == "simple":
        print("\nYou chose simple interest\n")
        rate = rate / 100 # taking the user input and dividing by 100 e.g. 8% == 0.08
        total_amount = deposit * (1 + rate * years)
        rounded_number = round(total_amount, 2)
        print("\n£" + str(rounded_number))  
    else:
        print("\nYou chose compound interest\n")
        rate = rate / 100
        total_amount =  deposit * math.pow((1 + rate), years)
        rounded_number = round(total_amount, 2)
        print("\n£" + str(rounded_number)) 

else: 
    print("You chose bond.")
    #prompts the user to enter the require info for the calc to work. 
    house_value = int(input("Enter the value of the house: "))
    interest_rate = float(input("Enter the annual interest rate: "))
    months = int(input("Enter the number of months to take to repay the bond: "))
    interest_rate = (interest_rate / 100) / 12 # getting the monthly interest rate e.g. annual 7% == 0.07 / 12 monthly 

    repayment = (interest_rate * house_value) / (1 - (1 + interest_rate)**(-months))
    rounded_number = round(repayment, 2)
    print("\n£" + str(rounded_number)) 

