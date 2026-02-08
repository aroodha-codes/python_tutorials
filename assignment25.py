"""Q5 . Create a dictionary where:
Keys = student names
Values = marks (integer)
Write a menu-based program where user presses a key
('A', 'B', C', 'D') depending on the operation they want to perform on the dictionary:
1.A - Add a student
2.B - Update marks
3.C - Search for a student
4.D - Display all students and marks
"""
info = {}
while(True):
    print("Press A to add a student")
    print("Press B to update marks")
    print("Press C to search for a student")
    print("Press D to display all students")
    print("Press E to exit.")
    choice = input("Enter choice:").upper()
    if (choice == "A"):
        print("Enter student details:")
        name = input("Enter name:")
        marks = int(input("Enter marks:"))
        info[name] = marks
        print("Student added")
    elif (choice == "B"):
        name = input("Enter name:")
        if name in info:
            marks = int(input("Enter new marks:"))
            info[name] = marks
            print("Updated")
        else:
            print("Student not found.")
    elif (choice == "C"):
        name = input("Enter name to search:")
        if name in info:
            print("Marks:",info[name])
            print("Student found")
        else:
            print("Student Not found")    
    elif (choice == "D"):
        if not info:
            print(" Students Not found")
        else:
            for name,marks in info.items():
                print(name,marks)
    elif (choice == "E"):
        print("Exiting...")
        break
    else:
        print("Invalid choice!")