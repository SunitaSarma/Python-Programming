# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:47:38 2024

@author: sarma
"""
contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print("Contact added successfully.")

def view_contacts():
    if contacts:
        print("Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts found.")

def search_contact(name):
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        number = input("Enter contact number: ")
        add_contact(name, number)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        delete_contact(name)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please choose again.")
