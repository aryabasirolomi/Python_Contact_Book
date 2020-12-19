import smtplib, ssl
import sys
from argparse import ArgumentParser

class ContactBook():
    """ This class creates a contact book, and allows you to manage it
    
    Attributes:
        contacts_file(str): contacts_file(file): the file of contact books 
        (name,number,email,zipcode) all in string format
        contacts(list): all of the contacts, pulled from the file for local 
        changes all in string format
        file(str): the path to the file containing contacts
    """
    
    def __init__(self, filename):
        self.file = filename
        self.contacts = []
        self.contacts_file = open(self.file, 'r', encoding='utf-8') 
        for line in self.contacts_file.readlines():
            self.contacts.append(line.strip("\n").split(','))
       
        
    def print_all(self):
        """ Prints all of the contacts in a specified path.
        
        Args:
            filename(str): path to a file containing current contacts
            
        Side Effects:
            Prints all contents in the contacts file
        """
        with open(self.file, 'r', encoding='utf-8') as self.contacts_file:
            for i in self.contacts_file.readlines():
                print(i)
    
    
    def save(self):
        """ This method updates the file with any changes made locally.
        
        Side Effect:
            Updates self.contacts_file
        """
        with open(self.file, 'w', encoding='utf-8') as self.contacts_file:
            self.contacts_file.seek(0)
            for line in self.contacts:
                self.contacts_file.write(",".join(line))
                self.contacts_file.write("\n")
            self.contacts_file.truncate()
        self.contacts_file.close()
       
    def add_contact(self, name, number, email, zipcode):
        """ Creates and adds a contact.
        
        Args:
            name(str): the name of a contact (firstname, lastname)
            number(str): the phone number of a contact (ZZZ-ZZZ-ZZZZ)
            email(str): the email of a contact
            zipcode(int): the zipcode of a contact (ZZZZZ)
            
        Side Effects:
            Updates self.contact
            Prints a message containing the new contact information that was
            added to the contact book
            
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
            Prints a message containing the name of the contact that was removed 
            from the file
        """
        
        for line in self.contacts:
            match = line[0]
            if match == name:
                res = self.contacts.index(line)
                self.contacts.pop(res)
                self.save()
                print(f"Thank you! '{name}' has been removed from your contact"
                        +" book.")
        
    
    
    def pull_one_contact(self, name):
        """ Takes full name as input and returns the one contact
        
        Args: 
            name(str): the name of the contact you want pulled
            (firstname, lastname)
            
        Side Effects:
            Prints a contact with name, number, email, and zipcode
        
        Returns:
            tuple: returns a tuple containing the contact as a list 
                    and the indexed position of the contact.


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
                return contact, self.contacts.index(x)
        
        
    def update_contact(self,name):
        """ Updates an existing contact
        
        Args:
            name(str): the name of the contact you want to update 
            (firstname lastname)
            
        Side Effects:
            Prints a message containing the updated information
        """
        update_choice = input("What part of the contact would you like to"+
                            " modify? Enter name, number, email, or zipcode. ")
        find_contact = self.pull_one_contact(name)[1]
        
        if update_choice == "name":
            new_name = input("Please enter the updated name as"+ 
                " firstname lastname: ")
            self.contacts[find_contact][0] = new_name
            print(f"Your contact has been updated successfully with the"+ 
                f" following information: \n Name: {new_name}")
    
        elif update_choice == "number":
            new_number = input("Please enter the updated number: ")
            self.contacts[find_contact][1] = new_number
            print(f"Your contact has been updated successfully with the"+ 
                f" following information: \n Number: {new_number}")
    
        elif update_choice == "email":
            new_email = input("Please enter the updated email: ")  
            self.contacts[find_contact][2] = new_email
            print(f"Your contact has been updated successfully with the"+ 
                f" following information: \n Email: {new_email}")
    
        elif update_choice == "zipcode":
            new_zipcode = input("Please enter the updated zipcode: ")
            self.contacts[find_contact][3] = new_zipcode
            print(f"Your contact has been updated successfully with the"+ 
                f" following information: \n Zipcode: {new_zipcode}")
    
        else:
            sys.exit() 
        self.save()

    
    def sort_contacts(self, method, order):
        """ Sorts the contact book by the name or zipcode of the contacts
            and displays the contact book in ascending or descending order
            
        Args:
            method(str): Dictates what aspect the list will be sorted by.
            order(str): Dictates the order the list will be displayed in.
            
        Side Effects:
            Prints a list of sorted contacts.
        
        Returns:
            A list of sorted contacts.
        """
        
        method_l = method.lower()
        order_l = order.lower()
        
        if method_l == 'name' and order_l == 'asc':
            name_sort = sorted(self.contacts, key=lambda x: x[0])
            for x in name_sort:
                print(x)
            return name_sort
        elif method_l == 'name' and order_l == 'desc':
            name_sort = sorted(self.contacts, key=lambda x: x[0], reverse=True)
            for x in name_sort:
                print(x)
            return name_sort  
        
        elif method_l == 'zipcode' and order_l == 'asc':
            zip_sort = sorted(self.contacts, key=lambda y: y[3])
            for x in zip_sort:
                print(x)
            return zip_sort
        elif method_l == 'zipcode' and order_l == 'desc':
            zip_sort = sorted(self.contacts, key=lambda y: y[3],reverse=True)
            for x in zip_sort:
                print(x)
            return zip_sort
    
    def share_contact(self, name, sender_email):
        """ Uses simple mail trasnfer protocol(SMTP) to send one contact to 
        another person by email, using the pull one contact method.
        
        Args:
            name(str): the name of the contact you want to share.
            sender_email(str): The email address you are sending the contact to.
        
        Side Effects:
            prints to the console the contact that is being shared, and a 
            message once sharing is complete.
            
        """
        contact = self.pull_one_contact(name)[0]
            
        from_email = "share.contact326@gmail.com"
        from_password = "INST326Final" 
        the_name = contact[0]
        number = contact[1]
        email = contact[2]
        zipcode = contact[3]
        
        message = f"""Subject:New shared contact! \n
        Name: {the_name},\n 
        Number: {number},\n
        Email: {email},\n
        Zip Code: {zipcode} 
        """ 
            
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_email, from_password)
            server.sendmail(from_email, sender_email, message)
            print(f"""The contact for {name} has been sent to {sender_email}.\n
                  They may have to check their junk folder.""")
               
       
def main(filename):
    functionality = input("""What would you like to do: 
                        Enter 1 for printing all of your contacts,
                        Enter 2 for adding a new contact,
                        Enter 3 for removing a contact,
                        Enter 4 to see one contact's info,
                        Enter 5 to update a contact,
                        Enter 6 to view your contacts sorted by Name or Zipcode,
                        Enter 7 to share a contact \n""")
    ContactBooks = ContactBook(filename)
    if functionality == "1":
        ContactBooks.print_all()
        
    if functionality == "2":
        info = input("Enter your the contact info in this format: name,"+
                     " number, email, zipcode \n")
        split_info = info.split(",")
        ContactBooks.add_contact(split_info[0], split_info[1], split_info[2], 
                                 split_info[3])
        
    if functionality == "3":
        remove = input("Enter the name of the contact you wish to remove: ")
        ContactBooks.remove_contact(remove)
        
    if functionality == "4":
        see = input("Enter the full name of the contact you wish to see: ")
        ContactBooks.pull_one_contact(see)
        
    if functionality == "5":
        update = input("Enter the name of the contact you wish to update: ")
        ContactBooks.update_contact(update)
        
    if functionality == "6":
        method = input("Enter 'name' to sort by name or 'zipcode' to"+ 
                " sort by zipcode: ")
        order = input("Type 'asc' to display in ascending order or 'desc' to"+ 
                " display in descending order: ")
        ContactBooks.sort_contacts(method,order)
        
    if functionality == "7":
        info = input("""Enter the name of the contact you wish to share, and 
        the email you are sending it to in this format: firstname lastname,
        email \n""")
        info_split = info.split(",")
        ContactBooks.share_contact(str(info_split[0]), str(info_split[1]))

         
    
def parse_args(arglist):
    """ Parse command-line arguments. 
        Args:
            arglist (list of str): list of command-line arguments
            
        Returns:
            namespace: the parsed arguments (see argparse documentation for
            more information)
    """
    parser = ArgumentParser()
    parser.add_argument("filename", help = """The path to a file containing 
                        contacts""")

    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename)