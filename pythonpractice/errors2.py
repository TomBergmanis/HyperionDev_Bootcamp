# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # syntax error, to assign a string to a variable "" is needed. 
animal_type = "cub" 
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth." # Syntax error, the implementation of an f string is needed.
# additional logical error made above, the sentence printed to the terminal is incorrect. swapped the number_of_teeth and animal_type to make sense. 

print(full_spec) # syntax error, print statements should have opening and closing brackets. 

# Thank you for the feedback and apologies for not completing the submission fully first time round. Not sure what happened there... 