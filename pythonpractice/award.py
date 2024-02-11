""" store individuals times to complete each
    in variables for the 3 events of a triathlon: swimmiing, cycling and running
    calculate and display the total time taken 
    if the participant has a total time of 100 mins or less they are awarded "Provincial Colours"
    if the participant has a total time of 101-105mins they are awarded "Provinical Half Colours"
    if the particiapant has a time of 106-110 mins they win "Provincial Scroll"
    if the particpant is greater than or equal to 111 mins they win nothing.
"""
# variables created to store the times for each event. 
swim_time = int(50) # example times have been put in to test the statement below
cycle_time = int(50)
run_time = int(6)

total_time = swim_time + cycle_time + run_time # a variable which sums the individual times of each event

print(total_time) # testing to see if the total time variable sums the total time of each part ofthe triathlon

# using an if elif else statement to determine the award the person has. 
if total_time <= 100: # a time of 100 munutes or below 
    print("Well done! Provincial Colours")
elif 101 >= total_time <= 105: #  a time of 101 or above and 105 munutes or below 
    print("well done as well! Provincial Half Colours")
elif 106 >= total_time <= 110: #  a time of 106 or above and 110 munutes or below 
    print("Not bad! Provincial Scroll")
else: 
    print("Sorry better luck next time") # this should catch all other options or anything over 110 minutes 
