username = "programmer1"
password = "hackme"
auth_retries = 3

print("Description: This program authorize user in system\n")

while auth_retries > 0:

    input_username = input("Please enter username:")
    input_password = input("Please enter password:")

    is_username_valid = username == input_username
    is_password_valid = password == input_password

    if  is_username_valid and is_password_valid:
        break
    else :
        auth_retries -= 1
if not(is_username_valid and is_password_valid):
    if not is_username_valid:
        print("Invalid username")
    if not is_password_valid:
        print("Invalid password")

else :         



print("Welcome " + input_username + ", you are authorized into the system")
shut_down = input("Do you want to shut down your computer? yes/no:")
if shut_down == "yes":
    print("Shutting down your computer...")
elif shut_down == "no":
    become_admin = input("Do you want to become admin? yes/no:")
    if become_admin == "yes":
        print("Congrats! You are admin")
else:
    print("Have a nice day!")











