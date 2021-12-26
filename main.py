from os import sys
import os

#overwrite function: overwrites an existing file will user input
def Overwrite(userTxt):
    noOfStudents = int(input("Enter the number of Students in your class: "))
    studentsList = []
    try:
        fileCreater = open(userTxt, "w+")
        for x in range(noOfStudents):
            studentName = input("Enter your next student's name: ")
            studentsList.append(studentName)
        for name in studentsList:
            fileCreater.write(name + ",")
            fileCreater.read()
    except:
        print("Sorry, there was an error. Please try again.")


#add function: creates a new text file with the name the user enters and then writes to that file
def add(userText):
    filename = userText + ".txt"
    f = open(filename, "x+")
    Overwrite(filename)
    f.close()


#openfile function: opens a file of the user's choice if that file is available
def Openfile(userTxt):
    f = open(userTxt)
    contents = f.read()
    f.close()
    print(contents)


#delete function: deletes a specified file name
def delete(filename):
    try:
        os.remove(filename)
    except:
        print("Couldn't delete file.")


#startAttendance function: using a specified file program checks which students are absent and present
def startAttendance(filename):
    print(filename)
    try:
        presentStudents = []
        absentStudents = []
        f = open(filename, "r")
        referenceList = list(f.read().split(","))
        # ['tobi', 'visu', 'thiru', 'nihal', ' ']
        referenceList.pop()
        for student in referenceList:
            currentIn = input(f"Is {student} present? [Type yes or no]: ")
            if currentIn.lower() == "yes":
                presentStudents.append(student)
            elif currentIn.lower() == "no":
                absentStudents.append(student)
            else:
                while (currentIn.lower() != "yes"
                       and currentIn.lower() != "no"):
                    currentIn = input(
                        f"Is {student} present? [TYPE IN YES OR NO]: ")
                    if currentIn.lower() == "yes":
                        presentStudents.append(student)
                    elif currentIn.lower() == "no":
                        absentStudents.append(student)
        print(f"\nPresent students: {presentStudents}")
        print(f"Absent Students: {absentStudents}")
    except:
        print(f"Error")


#main function
def uc():
    userChoice = input(
        "Would you like to [overwrite], [add], [display existing], [start attendance]: \n")
    if userChoice == "overwrite":
        print("Let's Start.")
        userTxt = input(
            "Which file do you want to overwrite? Name the file as \nnameoffile.txt: "
        )
        Overwrite(userTxt)
        uc()
    elif userChoice == "add":
        userTxt = input("What is the name of your class:\n ")
        #adds a file with the user input
        add(userTxt)
        uc()
    elif userChoice == "display existing":
        userTxt = input(
            "Which file do you want to see? Name the file as \nnameoffile.txt: "
        )
        print("Here are your students: ")
        #opens the specified file
        Openfile(userTxt)
        uc()
    elif userChoice == "delete":
        userTxt = input("Which file do you want to delete: ")
        delete(userTxt)
        uc()
    elif userChoice == "start attendance":
        filename = input("Which file do you want to use? ")
        startAttendance(filename)
        uc()
    else:
        print(f"Thank you for using (project name) :)")
        sys.exit()


uc()
