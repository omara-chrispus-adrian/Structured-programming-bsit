##TODO
'''
With the use of If statements, write a python program that allows an 
istructor to enter a mark strictly between 0 and 100.

On receiving the mark, the program has to assign a grade based on your defined clusters ie 80-90 is A,
91-100 is A+ etc.
'''
print("WELCOME TO MARK DISTRIBUTOR")
mark = int(input("please enter a mark between 0 and 100"))
if mark < 0 or mark > 100:
    print("Invalid, no mark")
elif mark <= 39:
    print("F")
elif mark <= 49:
    print("E")
elif mark <= 59:
    print("D")
elif mark <= 69:
    print("C")
elif mark <= 79:
    print("B")
elif mark <= 89:
    print("A")
elif mark <= 100:
    print("A+")