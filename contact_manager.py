import json

# File to store contact data
CONTACTS_FILE = "contacts.json"

# Function to load contacts from file
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Function to save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Function to display all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    if name in contacts:
        print("Contact already exists. Use the edit option to modify it.")
    else:
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added successfully.")

# Function to edit an existing contact
def edit_contact(contacts):
    name = input("Enter the name of the contact to edit: ").strip()
    if name in contacts:
        print(f"Current Info - Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
        phone = input("Enter new phone number (leave blank to keep current): ").strip()
        email = input("Enter new email address (leave blank to keep current): ").strip()

        if phone:
            contacts[name]["phone"] = phone
        if email:
            contacts[name]["email"] = email
        
        print(f"Contact {name} updated successfully.")
    else:
        print("Contact not found!")

# Function to delete a contact
def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print("Contact not found!")

# Main menu function
def main():
    contacts = load_contacts()

    while True:
        print("\nContact Management System")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
            save_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
            save_contacts(contacts)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
