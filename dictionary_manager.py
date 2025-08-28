print("Welcome Dictionary Manager")
print()

my_dict = {
    "user1": {
        "name": "Elvin",
        "age": 23,
        "city": "Warsaw"
    },
    "user2": {
        "name": "Aylin",
        "age": 25,
        "city": "Baku"
    },
    "user3": {
        "name": "Kamran",
        "age": 30,
        "city": "Berlin"
    },
    "user4": {
        "name": "Nigar",
        "age": 28,
        "city": "Vienna"
    },
    "user5": {
        "name": "Farid",
        "age": 22,
        "city": "Prague"
    }
}

try:
    while True:
        print("1 – Display the dictionary")
        print("2 – Search for a value")
        print("3 – Replace a value by key")
        print("4 – Display a value by key")
        print("5 – Delete a value by key")
        print("quit – Exit the program")

        user_choose = input("Please choose one of the options: ")

        if user_choose == "1":
            print("Current dictionary:")
            for user, data in my_dict.items():
                print(f"{user}: {data}")

        elif user_choose == "2":
            search_value = input("Enter a value to search: ")
            found = False
            for user, user_data in my_dict.items():
                if search_value in map(str, user_data.values()):
                    print(f"Value found in {user}: {user_data}")
                    found = True
            if not found:
                print("Value not found.")

        elif user_choose == "3":
            key_1 = input("Enter user key (e.g. user1): ")
            field = input("Which field to replace? (name / age / city): ")
            new_value = input("Enter new value: ")
            if key_1 in my_dict and field in my_dict[key_1]:
                my_dict[key_1][field] = new_value
                print("Value updated.")
            else:
                print("Invalid user or field.")

        elif user_choose == "4":
            key_2 = input("Enter a user key to display: ")
            if key_2 in my_dict:
                print(f"{key_2}: {my_dict[key_2]}")
            else:
                print("User not found.")

        elif user_choose == "5":
            key_3 = input("Enter a user key to delete: ")
            if key_3 in my_dict:
                del my_dict[key_3]
                print("User deleted.")
            else:
                print("User not found.")

        elif user_choose.lower() == "quit":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please choose between 1–5 or 'quit'.")

except ValueError:
    print("Invalid input.")
except KeyError:
    print("User or field not found.")
