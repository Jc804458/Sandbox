SECRET_PASSWORD = 5657

print("Welcome to password checker")

password = input("Enter Password: ")
while password != SECRET_PASSWORD:
    print("Invalid password, try again")
    password = input("Enter Password: ")
else:
    print("You go it")
