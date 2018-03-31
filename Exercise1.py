## My Schedule
## A program that stores information about class schedules in a dictionary
##
## Reuben Mees
## March 31, 2018

# define the main function
def main():
    # define the schedule dictionary
    schedule={"CS101":[3004, "Haynes", "8:00 a.m."],
              "CS102":[4501, "Alvarado", "9:00 a.m."],
              "CS103":[6755, "Rich", "10:00 a.m."],
              "NT110":[1244, "Burke", "11:00 a.m."],
              "CM241":[1411, "Lee", "1:00 p.m."]}

    # set a variable to allow multiple attempts
    cont="y"
    while cont[0].lower()=="y": # check only first character for lowercase
        # get the input and convert to all caps
        course=input("Which course are you looking for? ")
        course=course.upper()
        # test if the input is in the schedule and print the message
        if course in schedule:
            print(course, "meets in room", schedule[course][0],
                  "with instructor", schedule[course][1],
                  "at", schedule[course][2])
        # print a message if not in the schedule 
        else:
            print(course, "is not on the schedule.")

        # ask if the user wants to try another course
        cont=input("Would you like to try another course number? (y to continue) ")
        # test against a null input to avoid IndexError in the test
        if cont=="":
            cont="n"

    # print an exit message
    print("Goodbye.")

# call the main function
main()
    
