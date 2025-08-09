people = []

def create_person():
    print("\nAdd Person")
    pname = input("Name: ")
    pnum = input("Phone Number: ")
    pemail = input("Email: ")
    paddr = input("Address: ")
    people.append({
        "name": pname,
        "phone": pnum,
        "email": pemail,
        "address": paddr
    })
    print("Person added successfully")

def list_people():
    print("\nPeople List")
    if not people:
        print("No entries available")
    else:
        for i, person in enumerate(people, start=1):
            print(f"{i}. {person['name']} - {person['phone']}")

def find_person():
    print("\nSearch Person")
    term = input("Enter name or phone to search: ").lower()
    found = False
    for person in people:
        if term in person['name'].lower() or term in person['phone']:
            print(f"\nName: {person['name']}\nPhone: {person['phone']}\nEmail: {person['email']}\nAddress: {person['address']}")
            found = True
    if not found:
        print("No match found.")

def edit_person():
    print("\nUpdate Person")
    target = input("Enter the name to update: ")
    for person in people:
        if person["name"].lower() == target.lower():
            person["phone"] = input("New Phone Number: ")
            person["email"] = input("New Email: ")
            person["address"] = input("New Address: ")
            print("Person updated successfully")
            return
    print("No match found.")

def remove_person():
    print("\nDelete Person")
    target = input("Enter the name to delete: ")
    for i, person in enumerate(people):
        if person["name"].lower() == target.lower():
            del people[i]
            print("Person deleted successfully")
            return
    print("No match found.")

def menu():
    while True:
        print("\nData Management")
        print("1. Add Person")
        print("2. View All")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")
        option = input("Enter your choice (1-6): ")

        if option == "1":
            create_person()
        elif option == "2":
            list_people()
        elif option == "3":
            find_person()
        elif option == "4":
            edit_person()
        elif option == "5":
            remove_person()
        elif option == "6":
            print("Exiting program")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    menu()
