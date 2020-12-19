""" Test functions for the contact script """

from contact import ContactBook
import pytest 
from pathlib import Path

def test_pull_one_contact():
    """Tests ContactBook.pull_one_contact method. """
    contact_1 = ContactBook('contacts.txt')
    assert contact_1.pull_one_contact('Kanye West')[0] == ['Kanye West', 
                            ' 657-882-1340', ' kanye4prez@yahoo.com', ' 12345']
    assert contact_1.pull_one_contact('Tony Stark')[0] == ['Tony Stark',
                            ' 212-970-4133', ' tonystark@gmail.com', ' 90265']
    assert contact_1.pull_one_contact('Mike Ike')[0] == ['Mike Ike', 
                            ' 709-704-7126', ' mikeike@mikeike.com', ' 36110']
    assert not contact_1.pull_one_contact('David Dobrik')[0] == ['David Makers',
                            ' 603-520-6789', ' ddobrik83@gmail.com', ' 32452']
    assert not contact_1.pull_one_contact('Kevin Malone')[0] == ['Nicholas Malone', 
                        ' 864-432-4502', ' chilimountain@outlook.com', ' 87425']

def test_add_contact():
    """Tests ContactBook.add_contact method."""
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Lamar Jackson', '410-922-7787', 
                             'thegoat@gmail.com', '21117')
    assert['Lamar Jackson', '410-922-7787', 'thegoat@gmail.com', 
           '21117'] in contact_book.contacts
    
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Brad Pitt', '985-000-2345', 
                             ' bpitt@yahoo.com', '53285')
    assert['Brad Pitt', '985-000-2345', 
           ' bpitt@yahoo.com', '53285'] in contact_book.contacts
    
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Oprah Winfrey', '238-634-9828', 
                             ' oprahw@hotmail.com', '92483')
    assert['Oprah Winfrey', '238-634-9828', 
           ' oprahw@hotmail.com', '92483'] in contact_book.contacts
    
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Walt Disney', '476-184-28593', 
                             'disneywalt@gmail.com', '13948')
    assert['Walt Disney', '476-184-28593', 
           'disneywalt@gmail.com', '13948'] in contact_book.contacts
      
def test_remove_contact():
    """ Testing the remove contact method in contact.py when there is only 
    one contact in the file
    This block of code was modled after test_sports.py
    """
    try:
        contact = """Steve Rogers, 240-606-0590, rogers@shield.com, 22146"""
        filename = "TEMPORARY_TEST_FILE.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(contact)
        cb = ContactBook(filename)
        assert cb.remove_contact("Steve Rogers") == None
    finally:
        try:
            Path(filename).unlink()
        except:
            pass

def test_remove_contact1():
    """Testing remove contact method in contact.py when there are
    multiple contacts in the file
    This block of code was modled after test_sports.py
    """
    try:
        contact1 = """Steve Rog, 240-606-0590, rogers@shield.com, 22146
                   Arya Basir, 240-354-2848, aryabasir2001@hotmail.com, 20866"""
        filename1 = "TEMPORARY_TEST_FILE1.txt"
        with open(filename1, "w+", encoding="utf-8") as f1:
            f1.write(contact1)
            cb1 = ContactBook(filename1)
            cb1.remove_contact("Arya Basir") 
            f2 = f1.read()
        f2 = open(filename1)
        assert "Steve Rog, 240-606-0590, rogers@shield.com, 22146" in f2.read() 
        f2.close()
    finally:
        try:
            Path(filename1).unlink()
        except:
            pass