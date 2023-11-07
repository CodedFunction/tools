import sqlite3

conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (
                  id INTEGER PRIMARY KEY,
                  first_name TEXT,
                  last_name TEXT,
                  email TEXT,
                  phone TEXT)''')
conn.commit()


def add_contact(first_name, last_name, email, phone):
    cursor.execute("INSERT INFO contacts (first_name, last_name, email, phone) VALUES (?, ?, ?, ?)",
                   (first_name, last_name, email, phone))
    
    conn.commit()
    print("Contact added successfully.")


def list_contacts():
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(f"{contact[0]}: {contact[1]} {contact[2]} ({contact[3]} {contact[4]})")
    else:
        print("No contacts found.")


def search_contact(keyword):
    cursor.execute("SELECT * FROM contacts WHERE first_name LIKE ? OR last_name LIKE ?",
                   ('%' + keyword + '%', '%' + keyword + '%'))
    contacts = cursor.fetchall()
    if contacts:
        for contact in contacts:
            print(f"{contact[0]}: {contact[1]} {contact[2]} ({contact[3]}, {contact[4]})")
    else:
        print("No matching contacts found.")


def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    cursor.commit()
    print("Contact deleted successfully.")

while True:
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Search Contacts")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        phone = input("Phone: ")
        add_contact(first_name, last_name, email, phone)
    elif choice == '2':
        list_contacts()
    elif choice == '3':
        keyword = input("Enter a keyword: ")
        search_contact(keyword)
    elif choice == '4':
        contact_id = input("Enter the ID of the contact to delete: ")
        delete_contact(contact_id)
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")