import smtplib, ssl
import getpass
import sys
from argparse import ArgumentParser

class ContactBook():
    """ This class creates a contact book, and allows you to manage it
    
    Attributes:
        contact_book(list): a list of all of the contacts (name,number,email,zipcode)
    """
    
    def __init__(self, filename):
        with open(filename, 'r', encoding='utf-8') as self.contacts:
            for line in self.contacts:
                self.contacts.split(',')
            
        
    def print_all(self):
        """ Prints all of the contacts in a specified path.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Returns:
            Every item in contact book in a dict format 
        """
        pass
    
    
    def save(self):
        """ This method works with other methods to update the file with the contacts with any changes made"""
        pass
    
       
    def add_contact(self, name, number, email, zipcode):
        """ Creates and adds a contact.
        
        Args:
            name(str): the name of a contact (firstname, lastname)
            number(str): the phone number of a contact (ZZZ-ZZZ-ZZZZ)
            email(str): the email of a contact
            zipcode(int): the zipcode of a contact (ZZZZZ)
            
        Side Effects:
            Updates self.contact_book attribute.
        """
        pass
    
     
    def remove_contact(self, name):
        """ Removes a contact.
        
        Args:
            name(str):  the name of a contact (firstname, lastname)
            
        Side Effects:
            Updates self.contact_book attribute.
            
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
        pass
  
    
    def deleted_contacts(self):
        """ Holds the five most recent deleted contacts, which can be used for
        reference in case of an accidental deletion.
            
        Returns:
            A list of the five most recently deleted contacts.
        """
        pass
    
    
    def pull_one_contact(self, name):
        """ Reads in file and return specific contact
        
        Args: 
            name(str): the name of the contact you want pulled (firstname, lastname)
            
        Returns:
            contact(list): returns a contact with name,
            number, email, and zipcode
             
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
        contact = []
        with open (filename, "r", encoding="utf-8") as f:
            for line in f:
                comma_split = line.strip(),split(",")
                if name == self.name:
                    name = comma_split[0]
                    number = comma_split[1]
                    email = comma_split[2]
                    zipcode = comma_split[3]
                    contact.append(name, number, email, zipcode)
                else:
                    raise ValueError("This contact does not exist")
        return contact 
        
        
    def update_contact(self, name):
        """ Updates a previously existing contact selected in pull_contact function
        
        Args:
            contact(list): the output of the pull_contact method containing the name, number, email, and zipcode to be updated
            
        Side Effects:
            Updates attributes "name", "number", "email," and "zipcode" depending on user input
        """
        update_choice = input("What part of the contact would you like to update? Enter name, number, email, or zipcode")
        if update_choice == name:
            
        elif update_choice == number:
            
        elif update_choice == email:
            
        elif update_choice == zipcode:
            
        else:
            break
        
        
        
        
    
    def sort_contacts(self):
        """ Sorts the contact book by the name or zipcode of the contacts.
            
        Returns:
            A list of sorted contacts.
        """
        pass
        method = input('How would you like to sort the contacts?')
        if method == 'name':
        
        if method == 'zipcode':
    
    
    def share_contact(self, sender_email, name):
        """ Uses simple mail trasnfer protocol(SMTP) to send one contact to another person by email.
        Uses pull one contact method to decide what to send
        
        Args:
            email(str): The email address you are sending the contact to.
            name(str): the name of the contact you want to share.
            
        Raises:
            A ValueError if the senders username or password is incorrect
        """
        your_email = input('What is your email?')
        your_password = getpass.getpass(prompt='What is your password? (case-sensitive')
        contact = pull_one_contact(name)
        email_host = your_email.lower().split('@')
        server_data = {'outlook.com': ['smtp-mail.outlook.com', 587],
                       'gmail.com': ['smtp.gmail.com', 465],
                       'yahoo.com': ['smtp.mail.yahoo.com', 465],
                       'icloud.com': ['imap.mail.me.com', 993],
                       'aol.com': ['smtp.aol.com', 25],
                       'umd.edu': ['smtp.cs.umd.edu', 587],
                       'hotmail.com': ['smtp.live.com', 25]
        }
            
        host, port = [[i[0],i[1] for i in server_data[x]] for x in server_data if x == email_host]

        message =f"""\
            Subject: New shared contact!
            
            {contact}"""
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(host=host, port=port, context=context) as server:
            while True:
                try:
                    server.login(your_email, your_password)
                except ValueError:
                    print('Your email or password is incorrect, please try again')
                    break
            server.sendmail(sender_email, your_email, message)
            server.close()
            

    def favorites(self, name):
        """ Creates a new dict of your 5 favorite contacts. To add a contact after 5, you must
        delete an old contact using remove_contact() first, then adds the contact.
        
        Args:
            name(str): The name of the contact you want to add to your favorites.
            
        Returns:
            A list of 5 contacts that are indicated to be the favorites
        """
        pass
    
       
def main():
    pass
         
    
def parse_args():
        """ Parse command-line arguments. """
