## lists and dicts
students = [
    {'username': "B96227@students.ucu.ac.ug",'password': "123456"},
    {'username': "B96228@students.ucu.ac.ug",'password': "147751"},
    {'username': "B96229@students.ucu.ac.ug",'password': "123685"}
    ]

student = {
    'username': "B96230@students.ucu.ac.ug",
    'password': "12345"
}
students.append(student)
students.insert(1,student)

print(students)