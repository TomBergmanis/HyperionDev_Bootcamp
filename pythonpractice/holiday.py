import os 
import sys # importing an exit system 

# A function that allows the user to continue the program by restarting the program. 
def restart_program(): 
    python = sys.executable
    os.execl(python, python, *sys.argv)

city_flight = ''

while city_flight != '4': # while the user choses any option other than 4 the while loop will run
    print("Desinations: \n"
          "1. Paris \n"
          "2. New York \n"
          "3. Tokyo \n"
          "4. Exit \n")
    
    city_flight = input("What city will you be flying to? ").lower()

    # User choices action
    if city_flight == '1' or city_flight == 'paris': # if the user enters one of the options, we break out of the while loop 
        city_flight = "Paris"
        break
    elif city_flight == '2' or city_flight == 'new york':
        city_flight = "New York"
        break
    elif city_flight == '3' or city_flight == 'tokyo':
        city_flight = "Tokyo"
        break
    elif city_flight == '4' or city_flight == "exit":
        break
    else:
        print("\nInvalid option. Please try again!\n") # if the user enters something other than whats on the list the user will be prompted again to input

if city_flight == "4" or city_flight == "exit": # an if else statement to catch the user exiting the menu 
    print("You are exiting the menu") 
    # nested if statement that catches whether the user wants to exit the program and if so completes that request. 
    user_input = input("Are you sure you want to exit? (yes/no): ")

    if user_input.lower() == 'yes':
        print("Exiting the program")
        sys.exit()
    else:
        print("Continuing with the program...\n \nWelcome back!\n") # allows the user to continue if they change their mind by restarting the program by using the modules imported at the top of the program. 
        restart_program()
    
else:
    print(f"You are flying to {city_flight}. Enjoy your trip!") # if the user enters one of the options on the destinations list prints the choice back to the user 


# gets users number of nights they are staying 
# Validates the input for the number of nights
while True:
    try:
        num_nights = int(input("\nHow many nights will you be staying in a hotel? "))
        if num_nights > 0:
            break
        else:
            print("Please enter a valid positive integer for the number of nights.")
    except ValueError:
        print("Please enter a valid integer for the number of nights.")

# gets the users number of days renting a hire car
# Validate input for number of days for car rental
while True:
    try:
        rental_days = int(input("\nHow many days will you be hiring a car for? ")) # casting as an integer to allow for calculations to be performed
        if rental_days > 0:
            break
        else:
            print("Please enter a valid positive integer for the number of days.")
    except ValueError:
        print("Please enter a valid integer for the number of days.")    

# calculates the cost of the hotel. number of nights stayed and the cost of the hotel
def hotel_cost(num_nights):
    hotel_price = 200
    subtotal_1 = hotel_price * num_nights
    return subtotal_1

# function to calculate the cost of the flights depending on the destination chosen
def plane_cost(city_flight):
    if  city_flight == 'Paris': 
        flight_cost = 300.00 # cost to fly to paris
    elif city_flight == 'New York':
        flight_cost = 2500.00 # cost fo fly to new york
    elif city_flight == 'Tokyo':
        flight_cost = 3000.00 # cost to fly to tokyo
    else: 
        print("\nPlease choose a holiday destination.\n") # if the user has not entered the 3 destinations then catch 
    return flight_cost

def car_rental(rental_days):
    hire_car_cost = 30 # cost of hire car per day
    hire_car_total = rental_days * hire_car_cost
    return hire_car_total

def holiday_cost(hotel_cost, plane_cost, car_rental):

    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)  # calling the functions within this function for readability
    return total_cost # using all the functions outputs / returns to calculate the total cost of the holiday

# prints the outputs of all the information entered by the user. 

print(f"The total cost of the holiday, including hotel, flights and car rent, comes to: £ {holiday_cost(hotel_cost, plane_cost, car_rental)}")
print("We hope you enjoy your stay!")
print(f"\n\nHoliday cost breakdown:\n" # prints a breakdown of the costs to simply show the user each items cost.
      "\nHOTEL:\n"
      f"You're hotel will cost £{hotel_cost(num_nights)} for your {num_nights} night stay."
      "\nFLIGHTS:\n"
      f"You're flights to {city_flight} will be: £{plane_cost(city_flight)}."
      "\nCAR RENTAL:\n"
      f"You're car rental cost will be £{car_rental(rental_days)} for {rental_days} days\n"
      f"\nTotal cost of the holiday is: £ {holiday_cost(hotel_cost, plane_cost, car_rental)}\n")
    
