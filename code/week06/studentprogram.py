# Student Management Program
# Author: Brendan Heeney

# Write a function that prints out a menu of commands we can perform, ie add, 
# view and quit. The function should return what the user chose.
# Test the function. We don’t need to worry about error handling yet


from secrets import choice


def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()
    return choice

    # To Test the Function
    # choice = displayMenu()
    # print("you chose {}".format(choice))

def doAdd():
    # fill in later
    print("in adding")
def doView():
    # fill in later
    print("in viewing")

# Main Program

choice = displayMenu()
while(choice!= 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nplease select either a,v or q")
    choice = displayMenu()