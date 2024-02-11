sum = 0 # storing the total of the numbers entered. starting at 0. 
 
count = 0 # storing the count variable at 0. this stores the total amount of times the user enters a number

while True: # effectively cerates an infinate loop which we need to break out of in order to stop. 
    user_input = int(input("Enter a number here (-1 to finish): ")) # while the user enters a number repeat the input function.

    if user_input == -1: # tells the while loop that if the user enters -1 break out of the while loop 
        break
    sum += user_input # whilst in the while loop add the number the user enters to the sum variable until we break out the while loop
    count += 1 # this adds 1 to the count so we know what to divide the sum by to get the average. 

if count > 0: # if the user has entered at least 1 number carry out the calc below
    average = sum / count # calculates the average of all the numbers entered by the user excluding -1
    print(average)
