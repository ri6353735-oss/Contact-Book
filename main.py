
contact = {}

while True :
    print("\n====Contact Book====")

    print("1. Add Contact")
    print("2. view Contact")
    print("3. Search Contact")
    print("4. Delect Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name:")
        phone = input("Enter your phone number")

        contact[name] = phone

        print("contact added!")

    elif choice == "2":
        if contact:
            for name,phone in contact.items():
                print("name:",name)
                print("phone:",phone)

        else:
            print("No contact found")

    elif choice == "3":
        name = input("Enter name to search")
        if name in contact:
            print("phone",contact[name])

        else:
            print("Contact Not found")


    elif choice == "4":
        name = input("Enter Name to Delete:")
        if name in contact:
            del contact[name]
            print("Contact Deleted!")

        else:
            print("Contact Not Found!")

    elif choice == "5":
        print("progarm bondo hoccha")
        break
    else:
        print("Invalid Choice!")
