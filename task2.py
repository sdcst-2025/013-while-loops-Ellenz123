#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""
username=""
password=""
while username != "admin":
    username=input("Enter the username:")
    password=input("Enter the password:")
    if username!= "admin" or password!="12345":
        print("Access denied")
print("Access granted")