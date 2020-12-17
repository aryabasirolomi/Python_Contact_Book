""" Test functions for the contact script """

from contact import ContactBook
import pytest 

def test_pull_one_contact():
    contact_1 = ContactBook('contacts.txt')
    assert contact_1.pull_one_contact('Kanye West') == (['Kanye West', ' 657-882-1340', ' kanye4prez@yahoo.com', ' 12345'],9)
    assert contact_1.pull_one_contact('Tony Stark') == (['Tony Stark', ' 212-970-4133', ' tonystark@gmail.com', ' 90265'],9)
    assert contact_1.pull_one_contact('Mike Ike') == (['Mike Ike', ' 709-704-7126', ' mikeike@mikeike.com', ' 36110'],9)
    assert not contact_1.pull_one_contact('David Dobrik') == (['David Makers', ' 603-520-6789', ' ddobrik83@gmail.com', ' 32452'],9)
    assert not contact_1.pull_one_contact('Kevin Malone') == (['Nicholas Malone', ' 864-432-4502', ' chilimountain@outlook.com', ' 87425'],9)