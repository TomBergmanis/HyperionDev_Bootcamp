""" ask the user to input their name, age house number and street name 
store the user's inputs in separate variables 
print the user's input in a single strig (concateration)
"""

user_name = input("Please enter your full name here: ")
user_age = input("Enter your age here: ")
user_house_number = input("Enter your house number: ")
user_street_name = input("Enter your street name: ")

# Using an f string
print(f"This is ${user_name}. He is ${user_age} years old and lives at number ${user_house_number} on ${user_street_name}.")
# Using .format 
print("This is {}. He is {} years old and lives at house number {} on {}".format(user_name, user_age, user_house_number, user_street_name))
