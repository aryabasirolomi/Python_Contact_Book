""" Test functions for the contact script """

from contact import ContactBook
import pytest 
import sys
import traceback
def test_pull_one_contact():
    contact_1 = ContactBook('contacts.txt')
    #assert contact_1.pull_one_contact('Kanye West') == ['Kanye West', ' 657-882-1340', ' kanye4prez@yahoo.com', ' 12345']
    #assert contact_1.pull_one_contact('Tony Stark') == ['Tony Stark', ' 212-970-4133', ' tonystark@gmail.com', ' 90265']
    assert contact_1.pull_one_contact('Mike Ike') == '[Mike Ike, 709-704-7126, mikeike@mikeike.com, 36110]'
