###Python dictionary
"""
represented with {}

functions on a concept of key and value
"""

credentials = {
    'username': "B96227@students.ucu.ac.ug",
    'password': "12345"
}
print(credentials["username"])
print("Log in system")
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == credentials["username"] and password == credentials["password"]:
    print("Invalid credential, please try again!")

if username == credentials["username"]:
    if password == credentials["password"]:
        print("Logged in successfully!")
    else:
        print("invalid password")
else:
    print("Invalid username")


##extract data from a dict
#credentials["username"] ##username is the key


##changing a value in the dictionary
credentials = {
    'username': "B96227@students.ucu.ac.ug",
    'password': "12345"
}
print(f"Initial dictionary: {credentials}")
credentials["password"] = "charles21234"  ## updating a field
#adding another item to the dictionary
credentials["personal_email"] = "mugangacharles5@gmail.com" ## creating 
print(f"Updated dictionary: {credentials}")


## lists and dicts