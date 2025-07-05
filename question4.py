# Define a function called is_prime(n)
def is_prime(n):
    """Checks if n is a prime number. Returns True if prime, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+ 1):
        if n % i == 0:
            return False
        return True
    
# Asks the user for a number, call the function and display a message saying whether the number is prime.
num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")