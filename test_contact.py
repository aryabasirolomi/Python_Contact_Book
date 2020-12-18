""" Test functions for the contact script """

from contact import ContactBook
import pytest 
from pathlib import Path

def test_pull_one_contact():
    """Tests ContactBook.pull_one_contact method. """
    contact_1 = ContactBook('contacts.txt')
    assert contact_1.pull_one_contact('Kanye West')[0] == ['Kanye West', ' 657-882-1340', ' kanye4prez@yahoo.com', ' 12345']
    assert contact_1.pull_one_contact('Tony Stark')[0] == ['Tony Stark', ' 212-970-4133', ' tonystark@gmail.com', ' 90265']
    assert contact_1.pull_one_contact('Mike Ike')[0] == ['Mike Ike', ' 709-704-7126', ' mikeike@mikeike.com', ' 36110']
    assert not contact_1.pull_one_contact('David Dobrik')[0] == ['David Makers', ' 603-520-6789', ' ddobrik83@gmail.com', ' 32452']
    assert not contact_1.pull_one_contact('Kevin Malone')[0] == ['Nicholas Malone', ' 864-432-4502', ' chilimountain@outlook.com', ' 87425']

def test_add_contact():
    """Tests ContactBook.add_contact method."""
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Lamar Jackson', '410-922-7787', 'thegoat@gmail.com', '21117')
    assert['Lamar Jackson', '410-922-7787', 'thegoat@gmail.com', '21117'] in contact_book.contacts
    
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Brad Pitt', '985-000-2345', ' bpitt@yahoo.com', '53285')
    assert['Brad Pitt', '985-000-2345', ' bpitt@yahoo.com', '53285'] in contact_book.contacts
    
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Oprah Winfrey', '238-634-9828', ' oprahw@hotmail.com', '92483')
    assert['Oprah Winfrey', '238-634-9828', ' oprahw@hotmail.com', '92483'] in contact_book.contacts
    
    contact_book = ContactBook('contacts.txt')
    contact_book.add_contact('Walt Disney', '476-184-28593', 'disneywalt@gmail.com', '13948')
    assert['Walt Disney', '476-184-28593', 'disneywalt@gmail.com', '13948'] in contact_book.contacts

# def test_save():
    #"""Tests ContactBook.save() method."""
    #contact_book = ContactBook('contacts.txt')
    #contact_book.add_contact('Justin Tucker', '410-922-7788', 'jtkicker@gmail.com', '21244')
    #with open ('contacts.txt', "r", encoding="utf-8") as f:
        #lines = f.readlines()
        #assert ['Justin Tucker, 410-922-7788, jtkicker@gmail.com, 21244'] in lines