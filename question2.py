#Prompts the user to enter a numeric score.

score = int(input("Enter your score: "))

# Determines the grade using the grading scale.
if 80 <= score <= 100:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
elif 0 <= score <= 50:
    grade = "F"
else:
    grade = "Invalid score"

# Prints out the corresponding grade.
print(grade)