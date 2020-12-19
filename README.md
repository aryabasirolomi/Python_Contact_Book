# Python_Contact_Book
UMD INST326 Final Project - Creating a contact book in Python

Our program is a Contact Book that operates using a command line argument that takes a filename. The program is written in 'contact.py'. The sample file used to run the program is named 'contacts.txt' and contains a list of contacts. In order to run the program enter 'python3 contact.py contacts.txt' in the command line if you are using our supplied test file, or make a new text file and enter the path to the file as a string in place of 'contacts.txt'. You will be presented with a list of options in which the contacts can be added, deleted, editied, sorted, etc. Each output of the individual methods is either one contact, a list of contacts sorted or unsorted, or a message containing what was done to the contacts is printed. There is also a file, 'test_contact.py' where multiple tests are written to ensure that 'contact.py, works properly.


References

Aggarwal, Nikhil. “Writing to File in Python.” GeeksforGeeks, 25 Nov. 2019, www.geeksforgeeks.org/writing-to-file-in-python/. 

This website was used when writing the save method and deciding how to open the file. This brief article detailed how to write, read, and append to a file. The reading detailed how write to a file which was needed for the add_contact, remove_contact, and update_contact methods. This helped in deciding how we would edit data in the file and data used to run the program. The description of writing and appending to a file were the main components used when writing the code and in the final method used. The description detailed where the handler starts and the difference and benefits in writing and appending when compared to each other. 


Real Python. “Sending Emails With Python.” Realpython.com, Real Python, 5 Dec. 2018, https://realpython.com/python-send-email/#getting-started.

‌This website was used to help under how Simple Mail Trasnfer Protocol was used. This article described how to import smtplib and ssl, and send an email from python. While reading the artile, This article emphasized that smtplib works in a very structured and unique way, but it nonetheless a powerful tool. This article was used to implement the share_contact method. 


Bills, Aric. "In-class exercise: Sports results". 2020. https://umd.instructure.com/courses/1288445/assignments/5360675

The test file from the sports exercise: "test_sports.py" was used to assist in the development of 'test_contact.py'. The main item used was all of the code associated with the unlink method, as the goal was to create a file to test our script, but we did not want the file to take up unnecessary room.