#Welcome to the Contact Management System project! In this project, you will apply your Python 
# programming skills to create a functional command-line-based application that simplifies the 
# management of your contacts. You will be able to add, edit, delete, and search for contacts, 
# all while reinforcing your understanding of Python dictionaries, file handling, user interaction, 
# and error handling.

#Project Requirements
#Your task is to develop a Contact Management System with the following features:

#User Interface (UI):
#Create a user-friendly command-line interface (CLI) for the Contact Management System.
#Display a welcoming message and provide a menu with the following options:

import re
import os

def validate_phone_number(phone_number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(pattern, phone_number)

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

def read_contacts(filename):
    try:
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                contact, phone_number, email = line.strip().split(',')
                contacts[contact] = phone_number, email
            return contacts
    except FileNotFoundError:
        return {}

def add_new_contact(contacts):
    contact = input("Enter first and last name: ")
    if contact in contacts:
        print("Contact already exists. ")
        return 
    phone_number = input("Enter phone number: ")
    while not validate_phone_number(phone_number):
        print("Invalid phone number. Use (xxx-xxx-xxxx)")
        phone_number = input("Enter phone number: ")

    email = input("Enter email: ")
    while not validate_email(email):
        print("Invalid email.")
        email = input("Enter email: ")
    #print(f"{contact}, {phone_number}, {email}")
    contacts[contact] = (f"{phone_number}, {email} ")
    print("Contact added successfully.")

def edit_contact(contacts):
    contact = input("Enter first and last name: ")
    if contact not in contacts:
        print("Contact name not found")
    else:
        phone_number = input("Enter contact's phone number: ")
        if phone_number and not validate_phone_number(phone_number):
            print("Invalid format. Use (xxx-xxx-xxxx)")
            return
        email = input("Enter email: ")
        if email and not validate_email(email):
            print("Invalid email.")
            return
        contacts[contact] = (f"{phone_number}, {email}")
        print(f"Contact successfully updated.\nContact: {contact}\nPhone number: {phone_number}\nEmail: {email}")

def delete_contact(contacts):
    contact = input("Enter first and last name: ")
    if contact not in contacts:
        print("Contact not found!")
    del contacts[contact]
    print("Contact has been deleted.")

def search_contact(contacts):
    contact = input("Enter first and last name that you want to search: ")
    if contact in contacts:
        print(f"Contact '{contact}' found - Phone number: {contacts[contact]}")
    else:
        print("Contact not found!")

def display_contact(contacts):
    if not contacts:
        print("No contacts to display.")
        return
    for contact, info in contacts.items():
        print(f"Contact name: {contact}\n Phone number: {info}\n Email: {info}")

def export_contact(contacts):
    filename = input("Enter file name to export files: ")
    with open(filename, 'w') as file:
        for contact, info in contacts.items():
            print(info)
            file.write(f"{contact}, {info}\n")
    print(f"Contacts exported to {filename}.")

def write_contacts(filename, contacts):
    with open(filename, 'w') as file:
        for contact, info in contacts.items():
            file.write(f"{contact}, {info}\n")

def main():
    contacts = read_contacts('contacts.txt')
    while True:
        print("Welcome to the Contact Management System!")
        print('''
Menu:
1. Add a new contact
2. Edit an existing contact
3. Delete a contact
4. Search for a contact
5. Display all contacts
6. Export contacts to a text file
7. Quit
      ''')
        choice = input("Enter a directory 1-7: ")
        if choice == '1':
            add_new_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_contact(contacts)
        elif choice == '6':
            export_contact(contacts)
        elif choice == '7':
            print("Exiting...\nGoodbye!")
            break
        else:
            print("Invalid input. Try again.")
        
        write_contacts('contacts.txt', contacts)


if __name__ == "__main__":
    main()