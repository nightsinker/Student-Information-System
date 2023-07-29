import re
import string

def Addstudent(dic):
    print("==Add a new student==")
    # I did this to prevent errors for the admission number for Validation.
    while True:
        admission = input("\nPlease enter the admission number: ")
        while admission in dic:
            admission = input("Please enter a new admission number or enter 0 to return to main menu: ")
            if admission == '0':
                return dic
            else:
                continue

        long = len(admission)
        if long == 7:
            for i in range(0, 6):
                check = admission[i]
                if int(check) < 10:
                    continue
                else:
                    print("\n Invalid admission number")
            x = re.search("[A-Za-z]$", admission) #used regex matches   for validation  purposes
            if x:
                break
            else:
                print("\nInvalid admission number")
        else:
            print("\nInvalid admission number.")

    studentname = input("Please enter the student name: ")
    studentname = string.capwords(studentname) #I imported strings here because it will capitalize the student name first letter.
    modulename = input("Please enter the module name: ")
    modulename= string.capwords(modulename) #I imported strings here because it will capitalize the first letter of the module name.
    # Im making an assumption that all the scores is between 0 and 100
    while True:
        score = int(input("Please enter the score: "))
        if score <= 100 and score >= 0:
            break
        else:
            print("\nInvalid Score")

    dic[admission] = {studentname, modulename, score}
    dic.update({admission: [admission, studentname, modulename, score]})  #I updated the dictionary here
    print("Student added!")
    return dic

#Users can update the Name of the student and the Module name and the Score of the student.
def updatestudents(dic):
    if len(dic) == 0:
        print("\nThere is no student information currently in the system")
    else:
        print("== Update student==")
        admission = input("Please enter the admission number of the student you would like to update: ")
        if admission in dic:
            print("\nAdmission Number: " + admission)
            print("Student Name: ", dic[admission][0])
            print("Module Name: ", dic[admission][1])
            print("Score: ", dic[admission][2])
            print("Student Exist!")
            print("Enter 1 to Update Name")
            print("Enter 2 to Update Module Name")
            print("Enter 3 to Update Score")
            print("Enter 0 to return to Main Menu")
            updatechoice = int(input("What would you like to update? "))
            if updatechoice == 1:
                newname = input("Enter the new student name: ")
                dic[admission][1] = newname
                print("Student Name Updated!")
            elif updatechoice == 2:
                newmod = input("Enter the new module name: ")
                dic[admission][2] = newmod
                print("Module Name Updated!")
            elif updatechoice == 3:
                newscore = input("Enter the new score: ")
                dic[admission][3] = newscore
                print("Score  Updated!")
            elif updatechoice == 0:
                choice = 0
        else:
            print("No such student found.")
    return dic


def removestudent(dic):
    if len(dic) == 0:
        print("\nThere is no student currently in the system")
    else:
        print("==Remove Student==")
        admission = input("Please enter the admission number you want to remove: ")
        if admission in dic:
            print("\nAdmission Number: " + dic[admission][0])
            print("Student Name: ", dic[admission][1])
            print("Module Name: ", dic[admission][2])
            print("Score: ", dic[admission][3])
            remove = input("Is this the student you want to remove? (Yes/No) ")
            if remove == "No" or remove == "no":
                print("Student info was not removed!")
            elif remove == "Yes" or remove == "yes":
                print("Student info removed!")
                del dic[admission]
        else:
            print("No such student found.")
        return dic

def Display(dic):
    if len(dic) == 0:
        print("\nThere is no student currently in the system")
    else:
        print("==Display all students==")
        for key in dic:
            print("\nAdmission Number: ", dic[key][0])
            print("Student Name: ", dic[key][1])
            print("Module Name: ", dic[key][2])
            print("score: ", dic[key][3])
    return dic

def searchstudent(dic):
    if len(dic) == 0:
        print("\nThere is no student currently in the system")
    else:
        while True:
            print("\n== Search Student ==")
            print("Search By:")
            print("Enter 1 to search by Admission Number")
            print("Enter 2 to search by Module Name")
            print("Enter 3 to search by Score Range")
            print("Enter 0 to return to Main Menu")
            choice5 = input("Your choice: ")
            if choice5 == '1':
                admission = input("Please enter the admission number you wish to search by: ")
                if admission in dic:
                    print("\nAdmission Number: " + admission)
                    print("Student Name: ", dic[admission][1])
                    print("Module Name: ", dic[admission][2])
                    print("Score: ", dic[admission][3])
                else:
                    print("No student with this admission number found!")

            elif choice5 == '2':
                modulename = input("Please enter the module name you wish to search by: ")
                for admission in dic:
                    if modulename in dic[admission]:
                        print("\nAdmission Number: " + admission)
                        print("Student Name: ", dic[admission][1])
                        print("Module Name: ", dic[admission][2])
                        print("Score: ", dic[admission][3])
                    else:
                        print("\nNo student with this module name found!")

            elif choice5 == '3':
                print("Please enter the range of score you wish to search by:")
                minscore = int(input("Minimum score: "))
                if minscore >= 0 and minscore <= 100:
                    maxscore = int(input("Maximum score: "))
                    if maxscore >= 0 and maxscore <= 100:
                        for admission in dic:
                            if maxscore >= dic[admission][3] >= minscore:
                                print("\nAdmission Number: " + admission)
                                print("Student Name: ", dic[admission][1])
                                print("Module Name: ", dic[admission][2])
                                print("Score: ", dic[admission][3])
                            else:
                                print("\nNo student meets the above criteria")
                    else:
                        print("\nInvalid Maximum score")
                else:
                    print("\nInvalid Minimum score")
            elif choice5 == '0':
                break
            else:
                print("\nInvalid Choice\nPlease Re-enter your choice")

                return dic