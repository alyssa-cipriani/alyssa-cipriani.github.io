# ----------------------------
# COSC1100- Week 9 Demo 2
# Alyssa Cipriani
# July 11, 2025
# Calculate class Averages 
# ----------------------------

import random

#region DECLARATIONS
students = []
grades = []
MINIMUM_GRADE = 0.00
MAXIMUM_GARDE = 100.00

WELCOME_MESSAGE = '''Welcome to my grade calculator!'''

MAIN_MENU = ''' Main Menu 
-------------------------
1. Enter a Student Grade
2. Find a Student Grade
3. Calculate Stats 
4. Display All Marks
5. Exit'''

#endregion 


#region Functions
def getString(prompt):
    return input(prompt).strip()

def getInt(prompt):
    try:
        return int(input(prompt))
    except ValueError as v:
        return -1
    
def getIntInRange(prompt, minimum, maximum):
    is_valid = False
    while not is_valid:
        try:
            num= int(input(prompt).strip())

            if not minimum <= num <= maximum:
                print("That number was not in the right range")
                raise ValueError
            
            is_valid = True
        except ValueError as v:
            print("Invalid input")

    return num

def getRandomInt(min, max):
    return random.randint(min, max)

def enterGrade():
    students.append(getString("Enter the Student's Name: "))
    grades.append(getFloatInRange("Enter the students grades: ", MINIMUM_GRADE, MAXIMUM_GARDE))

def findGrade():
    # user enters students name
    student_name = getString("Enter the student's name: ")
    # check if the name exits 
    if student_name in students:

    # obtain student's index number
        index = students.index(student_name)
        # obtain and print grade 
        print("%s's garde is %i" % (student_name, grades[index]))
    else: print("That student was not found!")

def getFloatInRange(prompt, minimum, maximum):
    is_valid: False 
    while not is_valid:
        try:
            float = float(input(prompt).strip())

            if not minimum <= float <= maximum:
                print("That number was not in the right range")
                raise ValueError
            
            is_valid = True
        except ValueError as v:
            print("Invalid input")

    return float

def displayAllMarks():
    for i in range(0,len(students)):
        print("%10s - %6.2f" % (students[i], grades[i]))

def calculateGradeTotal():
    sum = 0 
    for g in grades:
        sum += g 
    return sum 

def showStats():
    print("---Class Stats---")
    # how many grades 
    print("Number of stats %i" % len (students))
    try:
        # minimum grade
        print("Minimum Grade: %.2f" % min(grades))
        # maximum grade
        print("Maximum Grade: %.2f" % max(grades))
        # average grade
        print("Average Grade: %.2f" % (calculateGradeTotal()/len(grades)))
    except:
        print("There are no students for the average calculation!")
# get a afloat in a range from the user
# Calculate stats
    # minimum
    # maximum
    # average

# display 


#region Main Program 

# Greet the user
print(WELCOME_MESSAGE)

# set up menu loop
choice = 0
while not choice == 5:
    # show menu
    print(MAIN_MENU)
    # prompt, receive and store user choice 
    choice = getIntInRange("Enter your choice (1-5): ",1,5)
    # conditional structure to process menu choice 
    if choice == 1:       enterGrade()
    elif choice == 2:     findGrade()
    elif choice == 3:     showStats()
    elif choice == 4:     displayAllMarks()

    input("Press -enter- to continue")
    
# exit the program 
print ("Good-bye")
exit()
#endregion