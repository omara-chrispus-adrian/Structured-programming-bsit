attempts = 0
while attempts < 3:
    secret_number = int(input("enter the secret number:"))
    if secret_number == 7:
        print("You got it right!")
        break
    else:
        print("wrong number! Try again.")
    attempts += 1
else:
    print("Too many tries. locked out.")