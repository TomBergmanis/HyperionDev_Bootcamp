sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print("The string without any manipulation: ") # printing the string as is. 
print(sentence)
print("\nThe string with ! removed and replaced with a space: ")
sentence = sentence.replace("!", " ") # using the replace method to identify the ! and replace with a space
print(sentence)

print("\nthe new sentence with the ! removed etc. converted to uppercase: ")
print(sentence.upper()) # converts the newly manipulated string (with ! removed) to uppercase

print("\nThe string in reverse using the slice method: ")

# getting the length of the string to start the slice index
b =  slice(len(sentence), 0, -1) # reverses the string by slicing it from index -1 
print("\n" + sentence[b]) # this does not give the desired output as its missing the last character

# An alternative to this is to use the below
c = sentence[slice(None, None, -1)] # "none" would provde a default "start" and "end" point with -1 as the step. "none" would enable to include all the elements of the variable. 
print("\n" + c) # prints the correct version on a new line

# an alternative to the above
print("\n" + sentence[::-1]) # uses sting slicing instead of the slice method to achieve the same result


