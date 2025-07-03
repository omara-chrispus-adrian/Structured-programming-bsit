# Example: System Password Authentication using a while loop

# Set the correct password
correct_password = "secure123"

# Initialize attempt counter
attempts = 0
max_attempts = 3

# Loop for user password authentication
while attempts < max_attempts:
    password = input("Enter system password: ")
    if password == correct_password:
        print("Access granted. Welcome!")
        break
    else:
        attempts += 1
        print(f"Incorrect password. Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("Access denied. Too many incorrect attempts.")