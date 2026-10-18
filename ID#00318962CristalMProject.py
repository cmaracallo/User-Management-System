##Cristal Maracallo 
##Project: User Management 
## The program lets users create accounts, log in, and change their passwords.
##it saves usernames and passwords on an encrypted file, and keeps records of
##Everything users log in to another file.

import random

def load_user_data():
    user_dict = {}
    file_1 = open("user_data.txt", "r")
    for line in file_1:
        line = line.strip()
        print(line)
        if line:
            username, password = line.split(':')
            user_dict[username] = password
    file_1.close()
    return user_dict

def save_user_data(user_dict):
    file_1 = open("user_data.txt", "w")
    for username, password in user_dict.items():
        file_1.write(f"{username}:{password}\n")
    file_1.close()

def test_valid_password(password):
    min_length = 7
    forbidden_characters = ' !@$:? '
    if len(password) >= min_length:
        for char in forbidden_characters:
            if char in password:
                return True
    else:
        return False

def encrypt_password(password):
    first = password[0]
    last = password[-1]
    password = last + password[1:-1] + first

    password = password.replace('i', '!')
    password = password.replace('a', '@')
    password = password.replace('S', '$')
    password = password.replace('J', '?')

    return password

def create_username():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    username = first_name[0].lower() + last_name.lower() + str(random.randint(1000,9999))
    return username

def get_password():
    attempts = 0
    while attempts < 5:
        type_pass = input("Enter a password: ")
        type_pass_again = input("Enter password again: ")
        if type_pass == type_pass_again:
            if test_valid_password(type_pass) == True:
                return type_pass
            else:
                print("Password invalid. Needs to be 7 characters long and needs to have forbidden characters")
        else:
            print("Password does not match. Try again, please")
            attempts = attempts + 1
            return None

def add_user(username, password, user_dict):
    encrypted = encrypt_password(password)
    user_dict[username] = encrypted

def check_user(username, password, user_dict):
    encrypted = encrypt_password(password)
    if username in user_dict:
        if user_dict[username] == encrypted:
            return True
        else:
            return False

def write_to_log(username, status):
    file_1 = open("log.txt", "a")
    file_1.write(username + ":" + status + "\n")
    file_1.close()

def print_log():
    file_1 = open("log.txt", "r")
    for line in file_1:
        print(line.strip())
    file_1.close()

def update_password(username, user_dict):
    new_password = get_password()
    if new_password:
        encrypted = encrypt_password(new_password)
        user_dict[username] = encrypted
        save_user_data(user_dict)
        write_to_log(username, "UPDATE")
        print("Password has been succesfully updated")
    else:
        print("Password failed")

def display_main_menu():
    print("1. Login")
    print("2. Create account")
    print("3. Quit")
    user_choice = input("Enter your choice: ")
    return user_choice

def display_user_menu():
    print("1. Print Log")
    print("2. Update password")
    print("3. Log out")
    user_choice = input("Enter your choice: ")
    return user_choice

def update_password(username, user_dict):
    new_password = get_password()
    if new_password:
        encrypted = encrypt_password(new_password)
        user_dict[username] = encrypted
        save_user_data(user_dict)
        write_to_log(username, "UPDATE")
        print("Password has been succesfully updated")
    else:
        print("Password failed")

if __name__ == "__main__":
    user_dict = load_user_data()
    logged_in = False
    current_user = " "
    running = True

    while running:
        if logged_in == False:
            user_choice = display_main_menu()
            if user_choice == "1":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if check_user(username, password, user_dict) == True:
                    logged_in = True
                    current_user = username
                    write_to_log(username, "OK")
                    print("Login")
                else:
                    write_to_log(username, "BAD PASS")
                    print("Invalid username or password.")
            if user_choice == "2":
                username = create_username()
                password = get_password()
                if password:
                    add_user(username, password, user_dict)
                    save_user_data(user_dict)
                    write_to_log(username, "New User")
                    print("Account has been created succesful.")
                else:
                    print("Missing requirements for password.")
            if user_choice == "3":
                save_user_data(user_dict)
                print("Quit")
                running = False
        else:
            user_choice = display_user_menu()
            if user_choice == "1":
                print_log()
                print("Print Log")
            if user_choice == "2":
                update_password(current_user, user_dict)
                print("Password has been updated.")
            if user_choice == "3":
                logged_in = False
                current_user = " "
                print("Log out succesfuly.")
