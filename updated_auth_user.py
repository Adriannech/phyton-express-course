from time import sleep

users = [
    ("admin", "admin"),
    ("turbo_hacker", "hackme"),
    ("qa_tester", "123test"),
    ("a_simple_mortal", "password"),
    ("dog", "bark-bark")
]

auth_retries = 3

print("Description: This program authorize user in system\n")

fields = {
    "id": {
        "default": {
            "value": 1,
            "type": "AUTO_INCREMENT"
        },
        "scan": False
    },
    "username": {
        "converter": str,
        "scan": True
    },
    "password": {
        "converter": str,
        "scan": True
    },
    "first_name": {
        "converter": str,
        "scan": True
    },
    "last_name": {
        "converter": str,
        "scan": True
    },
    "age": {
        "converter": int,
        "scan": True
    },
    "can_be_deleted": {
        "default": True,
        "scan": False
    },
    "role": {
        "default": "USER",
        "scan": False
    }
}

while auth_retries > 0:
    input_username = input("Please enter username: ")
    input_password = input("Please enter password: ")
users = [{
    "id": 1,
    "username": "admin",
    "password": "admin",
    "role": "ADMIN",
    "can_be_deleted": False,
    "age": 24,
    "first_name": "John",
    "last_name": "Doe"
}]

    is_username_valid, is_password_valid = False, False
    for username, password in users:  # unpacking tuple values
        if input_username == username:
            is_username_valid = username == input_username
            is_password_valid = password == input_password
while True:
    auth_retries = 3
    while auth_retries > 0:
        input_username = input("Please enter username: ")
        input_password = input("Please enter password: ")
        is_username_valid, is_password_valid = False, False
        for user in users:  # unpacking tuple values
            if input_username == user["username"]:
                is_username_valid = user["username"] == input_username
                is_password_valid = user["password"] == input_password
                break
        if is_username_valid and is_password_valid:
            break

    if is_username_valid and is_password_valid:
        break
        else:
            auth_retries -= 1
            if not is_username_valid:
                print("Incorrect username")
            if not is_password_valid:
                print("Incorrect password")
    else:
        auth_retries -= 1
        if not is_username_valid:
            print("Incorrect username")
        if not is_password_valid:
            print("Incorrect password")
else:
    print("Auth retries exceeded")
    exit(1)
        print("Auth retries exceeded")
        exit(1)

    print("Welcome " + input_username + ", you are authorized into the system")
    while True:
        print("Please select something: ")
        print("[+] Create new user (1)")
        print("[+] List users (2)")
        print("[+] User details (3)")
        print("[+] Logout (4)")
        print("[+] Exit (5)")

print("Welcome " + input_username + ", you are authorized into the system")
while True:
    print("Please select something: ")
    print("[+] Create new user (1)")
    print("[+] List users (2)")
    print("[+] Hack pentagon (3)")
    print("[+] Exit (4)")

    choice = input(">> ")
    if choice == "1":
        while True:
            input_username = input("Enter new user's username: ")
            input_password = input("Enter new user's password: ")
            user_already_exists = False
            for username, password in users:
                if username == input_username:
                    user_already_exists = True
                    break
            if user_already_exists:
                print(f"Conflict: User with username {input_username} already exist")
                continue
            users.append((input_username, input_password))
            print(f"[+] User {input_username} has been added successfully")
        choice = input(">> ")
        if choice == "1":
            new_user = dict()
            try:
                for field_name, meta in fields.items():
                    should_scan = "scan" in meta and meta["scan"] is True
                    if should_scan:
                        scanned_value = input(f"[-] Please enter value for ({field_name})")
                    elif not should_scan and "default" in meta:
                        if type(meta["default"]) == dict:
                            dm = meta["default"]
                            if "value" in dm and "type" in dm:
                                if dm["type"] == "AUTO_INCREMENT":
                                    dm['value'] += 1
                            scanned_value = dm["value"]
                        else:
                            scanned_value = meta["default"]
                    else:
                        scanned_value = None
                    if "converter" in meta:
                        scanned_value = meta["converter"](scanned_value)  # str(scanned_value)
                    new_user[field_name] = scanned_value
                users.append(new_user)
            except Exception as e:
                print("[-] Failed to add new user")
                print("[-] Error message: " + str(e))
        elif choice == "2":
            for user in users:
                print(f"id {user['id']}) {user['username']} - {'*' * len(user['password'])}")
        elif choice == "3":
            try:
                user_id = int(input("[+] Enter user id: "))
                user = None
                for u in users:
                    if user_id == u["id"]:
                        user = u
                        break
                if user is not None:
                    for field in fields:
                        print(f"{field} - {user[field]}")
                else:
                    print(f"[-] User with id {user_id} does not exist")
            except Exception as e:
                print("[+] Illegal id")
        elif choice == "4":
            print("Logout...")
            break
    elif choice == "2":
        order_number = 1
        for username, password in users:
            print(f"{order_number}) {username} - {'*' * len(password)}")
            order_number += 1
    elif choice == "3":
        print("[+] hacking pentagon...")
        sleep(5)
    elif choice == "4":
        print("Exit program...")
        exit(0)
    else:
        print("No function found!")
        elif choice == "5":
            print("Close application...")
            exit(0)
        else:
            print("No function found!")