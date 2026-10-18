# User-Management-System

A Python program that manages users and logins from the command line. It lets a person create an account, log in, change their password, and see a log of activity. 

## What it does
- Main menu: Log in, create an account, or quit.
- Create an account: Asks for a first name and last name, then makes a username from the first letter of the first name, the last name, and a random 4-digit number.
- Password rules: At least 7 characters, and these characters are not allowed: !, @, $, :, and ?. The password is typed twice to confirm it, with up to 5 tries.
- Login: Checks the username and password and says if the login worked.
- User menu: Print the log, update your password, log out.
- Log file: Saves each event with the username and a status: OK, BAD PASS, NEW USER, or UPDATE.

## How to run 
1. Install Python.
2. Download the Python file from this repository.
3. In the same folder, create an empty text file named 'user_data.txt'. The program needs it to start.
4. Open Terminal in that folder and run: 'python user_management.py'
5. Choose "Create account" first, then log in with the username the program gives you.

## What I learned 
- How functions work and how to organize code
- To test my code every time before I run it

## Skills shown 
- Writing and organizing functions
- Using dictionaries to store users
- Reading from and writing to files
- Checking user input with loops and conditions

## What I Learned 
- How functions work and how to organize code so each part has a clear job
- To test my code every time before I run it

## What I would improve 
- Hide the password while it is typed.
- Ask for the old password before it can be changed.
- Limit failed logins 
