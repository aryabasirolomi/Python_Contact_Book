import smtplib, ssl
import getpass
import sys
from argparse import ArgumentParser

class ContactBook():
    """ This class creates a contact book, and allows you to manage it
    
    Attributes:
        contacts_file(file): the file of contact books (name,number,email,zipcode)
        contacts(list): all of the contacts, pulled from the file for local changes
    """
    
    def __init__(self, filename):
        with open(filename, 'r+', encoding='utf-8') as self.contacts_file:
            for line in self.contacts_file:
                self.contacts = line.split(',')
            
        
    def print_all(self):
        """ Prints all of the contacts in a specified path.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Returns:
            Every item in contact book in a dict format 
        """
        print(self.contacts_file.read())
    
    
    def save(self):
        """ This method updates the file with any changes made locally."""
        self.contacts_file = self.contacts
                  
       
    def add_contact(self, name, number, email, zipcode):
        """ Creates and adds a contact.
        
        Args:
            name(str): the name of a contact (firstname, lastname)
            number(str): the phone number of a contact (ZZZ-ZZZ-ZZZZ)
            email(str): the email of a contact
            zipcode(int): the zipcode of a contact (ZZZZZ)
            
        Side Effects:
            Updates self.contact.
            
        """

        new_contact = input("Input your contact? Enter name,number,email,zipcode (in this format)")
        self.contacts_file.write(new_contact)
        print(f"Thank you {new_contact} has been added to your contact book.")
         
         
    def remove_contact(self, name):
        """ Removes a contact.
        
        Args:
            name(str):  the name of a contact (firstname, lastname)
            
        Side Effects:
            Updates self.contact
            
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
        delete_name = input("Enter 'name' to delete this contact.")
        if name in self.contacts:
            contact.append(name, number, email, zipcode)
        else:
            raise ValueError("This contact does not exist. Please try again.")
        print(f"Thank you {delete_name} has been removed from your contact book.")
  
    
    def deleted_contacts(self):
        """ Holds the five most recent deleted contacts, which can be used for
        reference in case of an accidental deletion.
            
        Returns:
            A list of the five most recently deleted contacts.
        """
        pass
    
    
    def pull_one_contact(self, name):
        """ Takes full name as input and returns the one contact
        
        Args: 
            name(str): the name of the contact you want pulled (firstname, lastname)
            
        Returns:
            contact(list): returns a contact with name,
            number, email, and zipcode
             
        Raises:
            ValueError: ValueError raises if contact does not exist
        """
        contact = []
        if name in self.contacts:
            name = [0]
            number = [1]
            email = [2]
            zipcode = [3]
            contact.append(name, number, email, zipcode)
        else:
            raise ValueError("This contact does not exist. Please try again.")
        return contact
        
        
    def update_contact(self):
        """ Updates an existing contact
        
        Args:
            name(str): the name of the contact you want pulled (firstname, lastname)
        """
        #In Progress
        find_contact = pull_one_contact[0]
        update_choice = input("What part of the contact would you like to modify? Enter name, number, email, or zipcode.")
        
        if update_choice == "name":
            new_name = input("Please enter the updated name.")
            contact[0] = "name"
        elif update_choice == "number":
            new_number = input("Please enter the updated number.")
            contact[1]
        elif update_choice == "email":
            new_email = input("Please enter the updated email.")
        elif update_choice == "zipcode":
            new_zipcode = input("Please enter the updated zipcode.")
        else:
            sys.exit()      
    
    def sort_contacts(self):
        """ Sorts the contact book by the name or zipcode of the contacts
            and displays the contact book in ascending or descending order.
            
        Returns:
            A list of sorted contacts.
        """
        method = input("Enter 'name' to sort by name or 'zipcode' to sort by zipcode: ")
        method_l = method.lower()
        order = input("Type 'asc' to display in ascending order or 'desc' to display in descending order: ")
        order_l = order.lower()
        
        if method_l == 'name' and order_l == 'asc':
            name_sort = sorted(self.contacts, key=lambda x: x[0])
            return name_sort
        elif method_l == 'name' and order_l == 'desc':
            name_sort = sorted(self.contacts, key=lambda x: x[0], reverse=True)
            return name_sort
        
        elif method_l == 'zipcode' and order_l == 'asc':
            zipcode_sort = sorted(self.contacts, key=lambda y: y[3])
            return zipcode_sort
        elif method_l == 'zipcode' and order_l == 'desc':
            zipcode_sort = sorted(self.contacts, key=lambda y: y[3], reverse=True)
            return zipcode_sort
    
    
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
        contact = self.pull_one_contact(name)
        email_host = your_email.lower().split('@')
        server_data =  [
                       ('outlook.com', 'smtp-mail.outlook.com', 587),
                       ('gmail.com', 'smtp.gmail.com', 465),
                       ('yahoo.com', 'smtp.mail.yahoo.com', 465),
                       ('icloud.com', 'imap.mail.me.com', 993),
                       ('aol.com', 'smtp.aol.com', 25),
                       ('umd.edu', 'smtp.cs.umd.edu', 587),
                       ('hotmail.com', 'smtp.live.com', 25)
                       ]
       
        host_list = [str(x[1]) for x in server_data if x[0] == email_host[1]]
        port_list = [int(x[2]) for x in server_data if x[0] == email_host[1]]
        host = host_list[0]
        port = port_list[0]

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
        """ Creates a new list of your 5 favorite contacts. To add a contact after 5, you must
        delete an old contact using remove_contact() first, then adds the contact.
        
        Args:
            name(str): The name of the contact you want to add to your favorites.
            
        Returns:
            A list of 5 contacts that are indicated to be the favorites
        """
        favorites = []
        if name == None:
            print(favorites)
        if len(favorites) <= 5:
            favorites.append(self.pull_one_contact(name))
        if len(favorites) >= 5:
            answer = input("You can only have a maximum of 5 favorites. If you would like to remove a contact, enter: yes")
            if answer == "yes":
                print(favorites)
                remove = input("Please enter the name of the contact you would like to remove")
                for x in favorites:
                    for y in x:
                        if y == remove:
                            favorites.pop(remove)
    
       
def main(filename, print_all, add_contact, remove_contact, deleted_contacts, pull_one_contact, update_contact, sort_contacts, share_contact, favorites):
    ContactBooks = ContactBook(filename)
    if print_all != False:
        ContactBooks.print_all()
    if add_contact != False:
        ContactBooks.add_contact(add_contact)
    if remove_contact != False:
        ContactBooks.remove_contact(remove_contact)
    if deleted_contacts != False:
        ContactBooks.deleted_contacts()
    if pull_one_contact != False:
        ContactBooks.pull_one_contact(pull_one_contact)
    if update_contact != False:
        ContactBooks.update_contact(update_contact)
    if sort_contacts != False:
        ContactBooks.sort_contacts()
    if share_contact != False:
        ContactBooks.share_contact(share_contact)
    if favorites != False:
        ContactBooks.favorites(favorites)
         
    
def parse_args(arglist):
    """ Parse command-line arguments. 
        Args:
            arglist (list of str): list of command-line arguments.
        Returns:
            namespace: the parsed arguments (see argparse documentation for
            more information)
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help = "The path to a file containing contacts")
    parser.add_argument("-p", "--print_all", default = False,
                        help = "Enter anything if you would like to see all of your contacts")
    parser.add_argument("-a", "--add_contact", default = False,
                        help = "Enter the contact info you would like to add in this format (name, number, email, zipcode")
    parser.add_argument("-r", "--remove_contact", default = False,
                        help = "Enter the name of the contact you would like to remove")
    parser.add_argument("-d", "--deleted_contacts", default = False,
                        help = "Enter anything if you would like to see your recently deleted contacts")
    parser.add_argument("-o", "--pull_one_contact", default = False,
                        help = "Enter the name of the contact you wish to see")
    parser.add_argument("-u", "--update_contact", default = False,
                        help = "Enter the name of the contact you would like to update")
    parser.add_argument("-s", "--sort_contacts", default = False,
                        help = "Enter anything to see a sorted version of your contacts")
    parser.add_argument("-h", "--share_contact", default = False,
                        help = "Enter the sender email and name of the contact you want to share")
    parser.add_argument("-f", "--favorites", default = False,
                        help = "Enter the name of the contact you want to add to your favorites, or enter None to view them")
    
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.print_all, args.add_contact, args.remove_contact,
         args.deleted_contacts, args.pull_one_contact, args.update_contact, 
         args.sort_contacts, args.share_contact, args.favorites)