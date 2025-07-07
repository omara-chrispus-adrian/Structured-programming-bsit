# 1. Allows the user to enter 5 numbers, storing them in a list.

numbers= []
print("Enter 5 numbers:")
for i in range(5):
    number = int(input())
    numbers.append(number)

# 2a. Displays the list of numbers.
print(f"numbers: {numbers}")

# 2b. Displays the maximum, mininmum, and average.
maximum = max(numbers)
minimum = min(numbers)
average = sum(numbers) / len(numbers)

print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
print(f"Average: {average}")

# 2c. Displays the list in sorted order
sorted_numbers = sorted(numbers)
print(f"Sorted: {sorted_numbers}")