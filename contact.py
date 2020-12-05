import smtplib, ssl
import getpass
import sys
from argparse import ArgumentParser
#print all, save, add_contact, remove_contact, pull_one_contact, sort_contacts
class ContactBook():
    """ This class creates a contact book, and allows you to manage it
    
    Attributes:
        contacts_file(str): contacts_file(file): the file of contact books (name,number,email,zipcode) all in string format
        contacts(list): all of the contacts, pulled from the file for local changes all in string format
        file(str): the path to the file containing contacts
    """
    
    def __init__(self, filename):
        self.file = filename
        self.contacts = []
        with open(self.file, 'r', encoding='utf-8') as self.contacts_file:
            for line in self.contacts_file.readlines():
                self.contacts.append(line.split(','))
       
        
    def print_all(self):
        """ Prints all of the contacts in a specified path.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Returns:
            Every item in contact book in a dict format 
        """
        with open(self.file, 'r', encoding='utf-8') as self.contacts_file:
            print(self.contacts_file.read())
        
    
    
    def save(self):
        """ This method updates the file with any changes made locally."""
        with open(self.file, 'a', encoding='utf-8') as self.contacts_file:
            for line in self.contacts:
                self.contacts_file.write("\n")
                self.contacts_file.write(str(line))
                  
       
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
        
        new_contact = f"{name}, {number}, {email}, {zipcode}"
        contact_list = [name,number,email,zipcode]
        self.contacts.append(contact_list)
        self.save()
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
        #with open(self.file, 'a', encoding='utf-8') as self.contacts_file:
            #read in file
        for line in self.contacts:
            if line.lower().startswith(name.lower()):
                self.contacts.pop(count)
            else:
                raise ValueError("This contact does not exist. Please try again.")
        self.save()
        print(f"Thank you {name} has been removed from your contact book.")
        

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
        for x in self.contacts:
            if x[0] == name:
                contact_name = x[0]
                number = x[1]
                email = x[2]
                zipcode = x[3]
                contact = [contact_name, number, email, zipcode]
                print(contact)
            #else:
                #raise ValueError("This contact does not exist. Please try again.")
        return contact
        
        
    def update_contact(self):
        """ Updates an existing contact
        
        Args:
            name(str): the name of the contact you want pulled (firstname, lastname)
        """
        """
        #In Progress
        find_contact = pull_one_contact()
        #Find a way to do multiple indices
        update_choice = input("What part of the contact would you like to modify? Enter name, number, email, or zipcode.")
    #for x in find_contact:
            #change x, maybe LC, 
        if update_choice == "name":
            new_name = input("Please enter the updated name.")
            find_contact[0] == new_name
            print(f"Your contact has been updated successfully with the following information: \n Name: {new_name}")
        elif update_choice == "number":
            new_number = input("Please enter the updated number.")
            find_contact[1] == new_number
            print(f"Your contact has been updated successfully with the following information: \n Number:{new_number}")
        elif update_choice == "email":
            new_email = input("Please enter the updated email.")
            find_contact[2] == new_email
            print(f"Your contact has been updated successfully with the following information: \n Email:{new_email}")
        elif update_choice == "zipcode":
            new_zipcode = input("Please enter the updated zipcode.")
            find_contact[3] == new_zipcode
            print(f"Your contact has been updated successfully with the following information: \n Zipcode:{new_zipcode}")
        else:
            sys.exit() 
        """
    
    
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
            for x in name_sort:
                print(x)
        elif method_l == 'name' and order_l == 'desc':
            name_sort = sorted(self.contacts, key=lambda x: x[0], reverse=True)
            for x in name_sort:
                print(x)
        
        elif method_l == 'zipcode' and order_l == 'asc':
            zipcode_sort = sorted(self.contacts, key=lambda y: y[3])
            for x in zipcode_sort:
                print(x)
        elif method_l == 'zipcode' and order_l == 'desc':
            zipcode_sort = sorted(self.contacts, key=lambda y: y[3], reverse=True)
            for x in zipcode_sort:
                print(x)
    
    
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
        if name == "None":
            for x in favorites:
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
    
       
def main(filename):
    functionality = input("""What would you like to do: Enter 1 for printing all of your contacts,
                          Enter 2 for adding a new contact,
                          Enter 3 for removing a contact,
                          Enter 4 to see your past 5 deleted contacts,
                          Enter 5 to see one contact's info,
                          Enter 6 to update a contact,
                          Enter 7 to view your contacts sorted by either Name or Zipcode,
                          Enter 8 to share a contact,
                          Enter 9 to view or add to your favorites \n""")
    ContactBooks = ContactBook(filename)
    if functionality == "1":
        ContactBooks.print_all()
        
    if functionality == "2":
        info = input("Please enter your the contact info in this format: name, number, email, zipcode \n")
        split_info = info.split(",")
        ContactBooks.add_contact(split_info[0], split_info[1], split_info[2], split_info[3])
        
    if functionality == "3":
        remove = input("Please enter the name of the contact you wish to remove \n")
        ContactBooks.remove_contact(remove)
        
    if functionality == "4":
        ContactBooks.deleted_contacts()
        
    if functionality == "5":
        see = input("Please enter the full name of the contact you wish to see \n")
        ContactBooks.pull_one_contact(see)
        
    if functionality == "6":
        update = input("Please enter the name of the contact you wish to update \n")
        #ContactBooks.update_contact(update)
        
    if functionality == "7":
        ContactBooks.sort_contacts()
        
    if functionality == "8":
        info = input("Enter the name of the contact you wish to share, and the email you are sending it to in this format: name,email \n")
        info_split = info.split()
        ContactBooks.share_contact(info_split[0], info_split[1])
        
    if functionality == "9":
        info = input("Enter the name of the contact you want to add to your favorites, if there is none type None \n")
        ContactBooks.favorites(info)
         
    
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

    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)