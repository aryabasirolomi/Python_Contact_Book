class ContactBook():
    
    
    def __init__(self, name, number, email, zipcode):
        self.name = name
        self.number = number
        self.number = email
        self.zipcode = zipcode
        
        
    def add_contact(self):
        """Deion
        This method... 
        """
        pass
    
    
    def remove_contact(self):
        """Deion
        """
        pass
    
    def deleted_contacts(self, contact_book):
        """Takes an existing contact list and deletes a specified contact
            from that list. Holds the five most recent deleted contacts.
        
        Args:
            contact_book(list): A list full of contacts.
            
        Returns:
            A list of the five most recently deleted contacts.
        
        """
    
    def pull_contact(self, filenamme):
        """Reads in file and return specific contact to be updated
        Args: 
            filename(str): path to a file containing current contacts
        Returns:
            contact(list): returns contact name with name, number, email, and zipcode to be update
        """
        
        
    def update_contact(self, contact):
        """ Updates a previously existing contact selected in pull_contact function
        Args:
            contact(list): the output of the pull_contact method containing the name, number, email, and zipcode to be updated
        Side Effects:
            Updates attributes "name", "number", and "email" depending on user input
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
    
    
    def sort_by_name(self, contact_book):
        """ Sorts the contact list by the name of the contact.
        
        Args:
            contact_book(list): List that contains all the contacts.
            
        Returns:
            A contact book that is sorted by the name of the contact in alphabetical order.
        """
        pass
    
    
    def sort_by_zipcode(self, contact_book):
        """ Sorts the contact list by the zipcode of each contact.
        
        Args:
            contact_book(list): List that contains all the contacts.
        
        Returns:
            A contact book that is sorted by the contact's zipcode in numerical order.
        
        """
        pass
    
    
    def print_all(self):
        """Arya
        """
        pass
    
    
    def share_contact(self):
        """Arya 
        logging library
        """
        pass

    def favorites(self):
        """Arya
        """
        pass
    
       
def main():
    pass
         
    
def parse_args():
        """ Parse command-line arguments. """
