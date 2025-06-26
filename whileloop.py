user_db ={
    "charles@gmail.com":"password" ,
    "admin@gmail.com":"password@123"

}

email = input("enter an email")
password = input("enter the password")

if email in user_db and user_db[email] == password:
    print("login Successful!")
    print(f"Welcome, {email}")
else:
    print("Invalid Credentials")