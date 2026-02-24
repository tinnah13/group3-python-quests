# ask the user to enter the password, if the password is correct print "Access granted", otherwise print "Access denied"
current_password = "abc123"
user_input = input("Enter the password: ")
if user_input == current_password:
    print("Access granted")
else:
    print("Access denied")