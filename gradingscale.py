print("WELCOME TO MARK DISTRIBUTOR")
mark = int(input("please enter a mark between 0 and 100"))
if mark < 0 or mark > 100:
    print("Invalid, no mark")
elif mark <= 39:
    print("F9")
elif mark <= 49:
    print("C6")
elif mark <= 59:
    print("C5")
elif mark <= 69:
    print("C4")
elif mark <= 79:
    print("C3")
elif mark <= 89:
    print("D2")
elif mark <= 100:
    print("D1")