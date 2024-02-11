"""if the user is 40 or over output "You're over the hill"
    if the user is over 100 output "sorry, you're dead" 
    if the user is 65 or older output "Enjoy your retirement!"
    if the user is under 13 output "You qualify for the kiddie discount."
    if the user is 21 output "Congrats on your 21st!"
    if any other gae output "Age is but a number" """

age = int(input("Please enter your age here: "))
 # below is first attempt which causes the if age >= 40 print statement to occur during the age >= 65 statement as well
""" if age >= 40:
    print("You're over the hill.")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
else:
    print("Age is but a number.") """
# reordered to the below, the if, elif, else statement should work as intended 
if age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age > 100:
    print("Sorry, you're dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
else:
    print("Age is but a number.") 
