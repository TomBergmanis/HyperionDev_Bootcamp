# write a program that displays a logical error 

sum = 0

while True: # creating an infinite loop 

    user_input = int(input("Enter a number (-1 to get the total): "))

    sum += user_input

    if user_input == -1: # breaks out the while loop if the user enters -1 
        print("The total of all the numbers you entered (excluding -1) is: ") 
        # We would expect the total to ignore th e-1 input from the user. 
        print(sum) # prints the total to be the total - 1 when i was expecting to get the total without the total - 1
        break
    
 
""" # ========== fixed version ==============

user_input1 = int(input("Please enter a number (-1 to exit): "))

sum = 0

while user_input1 != -1:

    sum += user_input1 # it is important that this statement comes before the user input so it stores the latest input before the user enters -1
    
    user_input1 = int(input("Please enter another number (-1 to exit): "))
    
    if user_input1 == -1:
        print(sum) # the output should ignore the -1 
        break
 """
