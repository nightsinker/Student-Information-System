students=0
dic={}
choice=0
# some assumptions that I hade made is that the score must be an integer between 0 and 100
# the admission number must be a 6 digit number followed by a letter
# the name of each student starts with a capital letter

from Functions import *

if choice==0:
    while True:
        print("\n***** Welcome to SIT Mini Student Information System *****")
        print("Number of student in the system:" + str(len(dic)))
        print("Enter 1 to Add a new student")
        print("Enter 2 to Update an existing student info")
        print("Enter 3 to Remove an existing student info")
        print("Enter 4 to Display all student information in the system")
        print("Enter 5 to Search for student(s)")
        print("Enter -1 to Exit the application")
        choice = input("Enter your choice: ")
        if choice == str(-1):
            break

        elif choice == str(1):
            Addstudent(dic)

        elif choice == str(2):
            updatestudents(dic)

        elif choice == str(3):
            removestudent(dic)

        elif choice == str(4):
            Display(dic)

        elif choice == str(5):
            searchstudent(dic)
        else:
            print("\nInvalid choice\n")
