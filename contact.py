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
        """Deion is in this method
        This method... 
        """
        pass
    
    
    def remove_contact(self, filename):
        """Deion
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
    
    
    def pull_one_contact(self, filenamme, name):
        """ Reads in file and return specific contact
        
        Args: 
            filename(str): path to a file containing current contacts
            name(str): the name of the contact you want pulled
            
        Returns:
            contact(dict): returns a contact with name as the key and
            number, email, and zipcode as the value
        """
        
        
    def update_contact(self, contact):
        """ Updates a previously existing contact selected in pull_contact function
        
        Args:
            contact(dict): the output of the pull_contact method containing the name, number, email, and zipcode to be updated
            
        Side Effects:
            Updates attributes "name", "number", and "email" depending on user input
            
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
    
    
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
