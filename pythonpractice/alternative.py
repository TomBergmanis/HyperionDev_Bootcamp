"""take a string and make every other character uppercase and the others lowercase """


string = "Hello World"

new_string = ""

for i, char in enumerate(string): # uses enumerate that gets the index and the character associated with the index
    if i % 2 == 0: # if the index is even make the character uppercase
        new_string += char.upper()
    else:
        new_string += char.lower() # all other circumstances make the character lowercase

print("\n" + new_string + "\n") # prints the whole string but with the upper and lower case characters. 

"""take the string and turn every other word to uppercase and the others lowercase"""

string_2 = "I am learing to code"

words = string_2.split() # using split to split up the string into individual words. 

# print(words) # checking the string has been split into words

new_string_2 = " " # empty new string to hold the new changed string

for i, word in enumerate(words): # interate through the words in the words string 
    if i % 2 != 0: # if the word in words is not even print the word as uppercase and also add a space for readability 
        new_string_2 += word.upper() + " "
    else:
        new_string_2 += word.lower() + " " # all other circumstances words lowercase and a space for readability 

print("\n" + new_string_2 + "\n") # print the new string 






    

   
        
        
    
    



