### --- OOP Email Simulator --- ###

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

    # Declare the class variable, with default value, for emails. 
 
    # Initialise the instance variables for emails.

    # Create the method to change 'has_been_read' emails from False to True.

class Email():
    # Class variable created 
    has_been_read = False # Defaults to not read.

    # Constructor function.
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
    
    # Method to mark an email as read.
    def mark_as_read(self):
       if self.has_been_read:
           return f"{self.email_address} - {self.subject_line} - has been read"
       else:
           return f"{self.email_address} - {self.subject_line} - unread"
    

# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #
# Build out the required functions for your program.

def populate_inbox(inbox, email_address, subject_line, email_content):
    new_email = Email(email_address, subject_line, email_content)
    # adds the new email info to the inbox list
    inbox.append(new_email) 

    
# Create 3 sample emails and add it to the Inbox list. 

def list_emails(inbox): # def list_emails(inbox, show_unread=False) 
    # Loops through the emails in the inbox printing the subject line with a corresponding number. 
    # If the email has been read then it wont show when the user selects option 2 in the menu. 
    # However, the task specificaion has asked not to use a function to complete this feature. 
    for i, email in enumerate(inbox, 1):  # Added (inbox, 1) to start it at 1 instead of 0. 
      # if not email.has_been_read or show_unread:
           unread_emails = f"-------------------------------------------"
           unread_emails += f"\n \t{i} \t{email.subject_line}\n"
           unread_emails += f"-------------------------------------------"
           print(unread_emails)

    
# Create a function which prints the email’s subject_line, along with a corresponding number.

def read_email(inbox, list_emails, user_selection):
    list_emails(inbox) # Display the list of emails with numbers. 

    if 1 <= user_selection <= len(inbox):
            selected_email = inbox[user_selection -1]
            selected_email.has_been_read = True

            email_details = f"\n Subject: {selected_email.subject_line}\n"
            email_details += f"From: {selected_email.email_address}\n"
            email_details += f"Content: {selected_email.email_content}\n"
            # Once the user has selected the specific email to view it will mark it as read. 
            email_details += f"Status: {selected_email.mark_as_read()}"
            print(email_details)
        
    elif user_selection != -1:
            print("\nInvalid selection. Please try again.")
            

            
# Create a function which displays a selected email. 
# Once displayed, call the class method to set its 'has_been_read' variable to True.

# --- Email Program --- #

# # Call the function to populate the Inbox for further use in your program.
# Example emails - Creating 3 Email objects. 
populate_inbox(inbox, "johnsmith@gmail.com", "This is your first email!", "Nothing much just a welcome message")
populate_inbox(inbox, "tom.bergmanis@gmail.com", "Second example email", "using personal email to see if this works")
populate_inbox(inbox, "georgiaecope@gmail.com", "Third example email", "yep another email")

# # Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:\n
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # add logic here to read an email
        print("\n\tInbox: ")
        list_emails(inbox)  # list_emails(inbox, show_unread=True)
    
        user_selection = int(input("Select an email to read (-1 to exit): "))

        read_email(inbox, list_emails, user_selection)
        
    elif user_choice == 2:
        print("View unread emails: \n")
        # add logic here to view unread emails
        # Achieved by using a function: list_emails(inbox)
        # Without a function 
        for i, email in enumerate(inbox, 1):
            if not email.has_been_read:
                unread_emails = f"-------------------------------------------"
                unread_emails += f"\n \t{i} \t{email.subject_line}\n"
                unread_emails += f"-------------------------------------------"
                print(unread_emails)

    elif user_choice == 3:
        # add logic here to quit appplication
        print("Exiting application...")
        break
    else:
        print("Oops - incorrect input.")

