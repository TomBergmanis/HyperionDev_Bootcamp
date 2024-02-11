# Register students for an exam venue

# using a while loop over a try except statement to make sure the user enters a number, this will repeat until the user enters a number
while True: 
    try:
        num_students = int(input("How many students are registering? "))
        break # once a number is inputted break out of the statement 
    except:
        print("Please enter the NUMBER of students registering!")

with open('reg_form.txt', 'w') as f:
    f.write("<=======Student Register=======>\n\n")
    for num in range(1, num_students + 1): # iterates through the loop as many times as the user specifies (number of students registered)
        student_id = input("Enter the next students ID number: ")
        f.writelines(f"Student ID - {student_id}: " + "..." * 10 + "\n\n") # writes the information to the text file and repeats as many times the user has specified
# using a f string for readability 
# the above create and writes to a new .txt file called 'reg_form.txt' creating a register of the student ID's and a space for them to add their signature. 


