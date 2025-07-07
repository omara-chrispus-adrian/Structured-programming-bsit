# LOOPS AND SUMMATION.

# 1. Prompts the user to enter a positive number n.
n = int(input("Enter a positive number: "))

# 2. Uses a loop (while) to calculate and display the sum of all even numbers from 1 to n.
sum_even = 0
i = 2
while i <= n:
    sum_even += i
    i += 2
print(f"Sum of even numbers: {sum_even}")

