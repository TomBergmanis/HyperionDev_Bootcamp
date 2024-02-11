for i in range(1, 6): # using two for loops to create a triangle
    print(i * "* ")
for i in range(4, 0, -1):
    print(i * "* ")

print("\nOnly using one loop and if else statement: \n")
# using one for loop and an if else statement to create the triangle in the doc 

num_stars = 10 # sets the size of the triangle 

for i in range(1, num_stars + 1): # range starting at 1 and going up to the specified number + 1. As range does not count the last number 
    # Sloping up
    if i <= num_stars // 2 + 1: # determines if i is less than or equal to half of the size of the triangle + 1 
        stars = 1 * i - 1 # number of stars to print i.e. counting up
        # once i is greater than half of the specified triangle size the else part of the statement starts. 
    # Sloping down
    else:
        stars = 1 * (num_stars - i) + 1 # number of stars to print i.e. counting down

    # Print stars
    print("*" * stars + "\n")  # prints the stars and adds the correct spacing 
