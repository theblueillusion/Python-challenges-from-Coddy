def display_menu():
    print('Contact Book Menu:')
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. List All Contacts")
    print("6. Exit")

def add_contact(contact_book):
    name = input()
    phone = input()
    email = input()
    address = input()

    if name in contact_book:
        print("Contact already exists!")
    else:
        contact_book[name] = {
            "phone": phone,
            "email": email,
            "address": address
        }
        print("Contact added successfully!")

def view_contact(contact_book):
    name = input()
    if name in contact_book:
        print("Name:", name)
        print("Phone:", contact_book[name]['phone'])
        print("Email:", contact_book[name]['email'])
        print("Address:", contact_book[name]['address'])
    else:
        print("Contact not found!")

def edit_contact(contact_book):
    name = input()
    if name in contact_book:
        new_phone = input()
        new_mail = input()
        new_address = input()
        if new_phone == " ":
            contact_book[name]['phone'] = contact_book[name]['phone']
        else:
            contact_book[name]['phone'] = new_phone
        if new_mail == " ":
            contact_book[name]['email'] = contact_book[name]['email']
        else:
            contact_book[name]['email'] = new_mail
        if new_address == " ":
            contact_book[name]['address'] = contact_book[name]['address']
        else:
            contact_book[name]['address'] = new_address
        print("Contact updated successfully!")
    else:
        print("Contact not found!")
    
def delete_contact(contact_book):
    name = input()
    if name in contact_book:
        deleted_name = contact_book.pop(name)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

def list_all_contacts(contact_book):
    if contact_book == {}:
        print("No contacts available.")
    else:
        for key, value in contact_book.items():
            print(f"Name: {key}")
            print("Phone:", value["phone"])
            print("Email:", value["email"])
            print("Address:", value["address"])
            print("")

contact_book = {}
while True:
    display_menu()
    menu = input()
    if menu == "1":
        add_contact(contact_book)
    elif menu == "2":
        view_contact(contact_book)
    elif menu == "3":
        edit_contact(contact_book)
    elif menu == "4":
        delete_contact(contact_book)
    elif menu == "5":
        list_all_contacts(contact_book)
    elif menu == "6":
        break
    

