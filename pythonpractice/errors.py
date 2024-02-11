# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print("Welcome to the error program") # syntax error, space between the statement and brackets around the statement added. 
print("\n") # syntax error, indent removed, space between the statement and backets added around the statement. 

# Variables declaring the user's age, casting the str to an int, and printing the result.

age_Str = "24" # syntax error, indent removed, variables declared with "=". changed to just 24 so that int works.
age = int(age_Str) # syntax error, indent removed, 
print("I'm" + " " + str(age) + " " + "years old.") 
""" syntax error, indent removed, converted age back to string str. 
    spaces added so it reads nicely. 
"""

# Variables declaring additional years and printing the total years of age.

years_from_now = "3" # syntax error, indent removed. 
total_years = age + int(years_from_now) # syntax error, indent removed and convert years_from_now to a integer int.

print("The total number of years: " + str(total_years)+ ".") 
# syntax error, space between the statement and brackets around the statement added.

""" "answer_years is not defined", replace with str(total_years) and remove "". 
    space added bteween : and " to improve readability and a fullstop at the end. 
"""

# Variable to calculate the total amount of months from the total amount of years and printing the result.

total_months = total_years * 12 + 6 # runtime error, total is not defined, replaced with total_years.
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old.") 
# syntax error, space between the statement and brackets around the statement added.

""" replaced total_months with str(total_months) Logical error, total_months comes out as 324 not 330. Solved by adding 6 to the total. 
    Also added a fullstop at the end for consistencey. 
"""
#HINT, 330 months is the correct answer. 


