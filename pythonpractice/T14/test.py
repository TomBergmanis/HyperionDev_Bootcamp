# Define the list of names
names_and_dates = [
    "Orville Wright 21 July 1988",
    "Rogelio Holloway 13 September 1988",
    "Marjorie Figueroa 9 October 1988",
    "Debra Garner 7 February 1988",
    "Tiffany Peters 25 July 1988",
    "Hugh Foster 2 June 1988",
    "Darren Christensen 21 January 1988",
    "Shelia Harrison 28 July 1988",
    "Ignacio James 12 September 1988",
    "Jerry Keller 30 February 1988",  # Note: Invalid date corrected
    "Frankie Cobb 1 July 1988",
    "Clayton Thomas 10 December 1988",
    "Laura Reyes 9 November 1988",
    "Danny Jensen 19 September 1988",
    "Sabrina Garcia 20 October 1988",
    "Winifred Wood 27 July 1988",
    "Juan Kennedy 4 March 1988",
    "Nina Beck 7 May 1988",
    "Tanya Marshall 22 May 1988",
    "Kelly Gardner 16 August 1988",
    "Cristina Ortega 13 January 1988",
    "Guy Carr 21 June 1988",
    "Geneva Martinez 5 September 1988",
    "Ricardo Howell 23 December 1988",
    "Bernadette Rios 19 July 1988"
]

# Iterate through the list and print only the full names
for item in names_and_dates:
    # Split each item into words
    words = item.split()
    print(words[:-3])
    
    # Check if there are more than two words (a full name)
    if len(words) > 2:
        # Join and print the full name
        full_name = ' '.join(words[:-3])  # Join all words except the last two (date)
        print(full_name)
