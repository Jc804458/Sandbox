SECRET_PASSWORD = "Akachukwu"


def main():

    print_welcome_message()
    getting_password()
    print_asterisks()


def print_asterisks():
    print("**")


def getting_password():
    password = input("Enter Password: ")
    while password != SECRET_PASSWORD:
        print("Invalid password, try again")
        password = input("Enter Password: ")


def print_welcome_message():
    print("Welcome to password checker")


main()
