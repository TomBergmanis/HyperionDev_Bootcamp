# this file might need to be opened with the DOB.txt file within its own folder in order for Python to recognise the directory. 

# checks to see what files are in the current working directory and lists them out. 
""" import os

cwd = os.getcwd()
files = os.listdir(cwd)
print("Files in %r: %s" % (cwd, files)) """

contents = "" # empty variabel / empty string 

with open('./DOB.txt', 'r+') as file:
    for line in file:
        contents += line # adds each word in the txt file to contents 
    print(contents) # prints the text file 
    split_contents = contents.split() # splitting the text file into the individual words
    print(split_contents) 

print("\nName\n") # new line added for readability 
for i in range(0, len(split_contents), 5): # iterates through the split_contents list, the range step is 5 as each persons info is 5 items long.
    first_name = split_contents[i]  # gets their first name as its the first index 
    last_name = split_contents[i + 1] # gets their second name as its the second index 
    #print(f"{first_name} {last_name}")   # check if that worked
    name = first_name + " " + last_name # concatanated the two items together so they can be printed together
    print(name)

# this process is repeated for the date of birth section of the task. referencing the indexes needed to extract the data needed for Birthdate 

print("\nBirthdate\n")
for i in range(0, len(split_contents), 5): 
    day = split_contents[i + 2]
    month = split_contents[i + 3]
    year = split_contents[i + 4]
    #print(f"{first_name} {last_name}")   
    date_of_birth = day + " " + month + " " + year
    print(date_of_birth)




  
