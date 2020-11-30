class ContactBook():
    
    
    def __init__(self, name, number, email, zipcode):
        self.name = name
        self.number = number
        self.email = email
        self.zipcode = zipcode
        self.contact_book = {}
        
    def print_all(self, filename):
        """ Prints all of the contacts in a specified path.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Returns:
            Every item in contact book in a dict format 
        """
        pass
    
        
    def add_contact(self, filename):
        """ Adds a contact to contact_book.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Side Effects:
            Updates self.contact_book attribute.
        """
        pass
    
    
    def remove_contact(self, filename):
        """ Removes a contact from contact_book.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Side Effects:
            Updates self.contact_book attribute.
            
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
        pass
  
    
    def deleted_contacts(self, contact):
        """ Holds the five most recent deleted contacts, which can be used for
        reference in case of an accidental deletion.

        Args:
            contact(list): A list full of contacts from remove_contact.
            
        Returns:
            A list of the five most recently deleted contacts.
        
        """
    
    
    def pull_one_contact(self, filename, name):
        """ Reads in file and return specific contact
        
        Args: 
            filename(str): path to a file containing current contacts
            name(str): the name of the contact you want pulled
            
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
                if name == self.name]:
                    name = comma_split[0]
                    number = comma_split[1]
                    email = comma_split[2]
                    zipcode = comma_split[3]
                    contact.append(name, number, email, zipcode)
                else:
                    raise ValueError("This contact does not exist")
        return contact 
        
    def update_contact(self, contact):
        """ Updates a previously existing contact selected in pull_contact function
        
        Args:
            contact(dict): the output of the pull_contact method containing the name, number, email, and zipcode to be updated
            
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
        
        
        
        
    
    def sort_by_name(self, contact_book):
        """ Sorts the contact book by the name of the contacts.
        
        Args:
            contact_book(list): List that contains all the contacts.
            
        Returns:
            A dict that is sorted by the name of the contacts in alphabetical order.
        """
        pass
    
    
    def sort_by_zipcode(self, contact_book):
        """ Sorts the contact book by the zipcode of each contact.
        
        Args:
            contact_book(list): List that contains all the contacts.
        
        Returns:
            A dict that is sorted by the contact's zipcode in numerical order.
        
        """
        pass
    
    
    def share_contact(self, email, name):
        """ Uses simple mail trasnfer protocol(SMTP) to send one contact to another person by email.
        Uses pull one contact method to decide what to send
        
        Args:
            email(str): The email address you are sending the contact to.
            name(dict): the Dict that contains the contact you want to send.
            
        Returns:
            A contact that will be emailed to the desired email
        """
        pass


    def favorites(self, name):
        """ Creates a new dict of your 5 favorite contacts. To add a contact after 5, you must
        delete an old contact using remove_contact() first, then adds the contact.
        
        Args:
            name(str): The name of the contact you want to add to your favorites.
            
        Returns:
            A list of dict that contain 5 contacts that are indicated to be the favorites
        """
        pass
    
       
def main():
    pass
         
    
def parse_args():
        """ Parse command-line arguments. """
