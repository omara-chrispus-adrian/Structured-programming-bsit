## Differences between assigning and declaring a variable giving practical examples of each
"Assigning a variable means storing a specific value into a named memory location (the variables) so that it can be used later in the program "

## example
input_score = int(input("Enter your test score"))
score = input_score # reassignment
if score >= 79:
    print("C+")
else:
    print("FAIL")

## Declaring a variable 
"Declaring a variable means introducing it into the program so it can hold values during execution." 

## Example
name = "Adrian" 
print("name")
age = 20 
print("age")