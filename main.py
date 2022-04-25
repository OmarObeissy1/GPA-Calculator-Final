"""
This program will help students be successful through:
Time management tools
GPA calculator.
"""
__author__ = "Omar Obeissy"


# Final Integration Project

print("Hi Professor Osheroff and fellow COP1500 students!", end='')
# Use the end function to have the next print statement come on the same line
# as the previous print statement.
print(" My integration project is an academic tracker and success program!")
print("Project due date:" + "3", "25", "2022", sep="/")
# Use the sep command to change the comma from a space to a backslash.
print("Don't forget: " + "Hard work is key! " * 5)
# Here I used + to concatenate two strings and * to repeat the string
# "Hard work is key! " five times.
# The following part will output the total
# study hours per week for each student.
print("The GPA calculator is meant for a range of 1 to 5 classes!")


def gpa_calc():
    """
    This function will be a GPA calculator by asking users for input regarding
    previous gpa, credit hours, and projected grades for this semester
    """
    validation = True
    while validation:
        try:
            num_classes = int(
                input("How many classes are you in this semester? "))
            if num_classes <= 0 or num_classes > 5:
                print("Please enter a valid whole number between 1 and 5!")
            else:
                validation = False
        except ValueError:
            print("Please enter an integer.")
    validation = True
    while validation:
        try:
            cred_hours = int(input(
                "How many credit hours are you enrolled in this semester? ", ))
            if cred_hours <= 0 or cred_hours > 21:
                print("Please enter a valid whole number between 1 and 21!")
            else:
                validation = False
        except ValueError:
            print("Please enter an integer.")
    study_hours = cred_hours * (2 ** 2)
    # The multiplication operator (*) is used to multiply two numbers.
    # The exponential operator (**) takes the first number and
    # raises it to the power of the second number.
    print(
        "You should spend the following amount of hours outside of class"
        "working on schoolwork each week:", study_hours)

    # The following part will calculate a students total GPA based on
    # projected grades for the current semester.
    validation = True
    while validation:
        try:
            prev_gpa = float(
                input("Enter your current GPA coming into this semester: ", ))
            if prev_gpa <= 0 or prev_gpa > 4:
                print("Please enter a valid positive number!")
            else:
                validation = False
        except ValueError:
            print("Please enter a positive number.")

    validation = True
    while validation:
        try:
            prev_ch = int(
                input(
                    "Enter your total credit hours completed coming into this "
                    "semester: ", ))
            if prev_ch <= 0 or prev_ch > 120:
                print("Please enter a valid whole number between 1 and 120!")
            else:
                validation = False
        except ValueError:
            print("Please enter an integer.")

    print(
        "For the following inputs please enter your grade as a capital letter "
        "by itself. Do not put a + or -.")

    counter = 1
    grade1 = 0
    grade2 = 0
    grade3 = 0
    grade4 = 0
    grade5 = 0
    good_input = False
    # Boolean operator not actually sets good_input to False

    # For loop for calculating GPA this semester
    for x in range(num_classes):
        grade = input("Enter your projected grade for a class: ", )
        if grade in ('A', 'B', 'C', 'D', 'F'):
            if grade == 'A':
                grade = 4.0
            elif grade == 'B':
                grade = 3.0
            elif grade == 'C':
                grade = 2.0
            elif grade == 'D':
                grade = 1.0
            elif grade == 'F':
                grade = 0
        else:
            while good_input is False:
                # != means not equal to
                # this while loop makes users put in valid input
                print("Invalid input. Please enter a capital letter grade.")
                grade = input("Enter your projected grade for a class: ", )
                if grade in ('A', 'B', 'C', 'D', 'F'):
                    if grade == 'A':
                        grade = 4.0
                    elif grade == 'B':
                        grade = 3.0
                    elif grade == 'C':
                        grade = 2.0
                    elif grade == 'D':
                        grade = 1.0
                    elif grade == 'F':
                        grade = 0
                    good_input = True

        if counter == 1 and grade1 == 0:
            grade1 = grade
        # Grade 1 will only save the value of grade if counter=1 and grade1=0
        # This is only on loop 1
        elif counter == 2 or grade2 == 0:
            grade2 = grade
        # Grade 2 will save the value of grade the first time through the loop
        # Since grade=0. But it will resave the second time through the
        # loop since counter = 2. This will leave us with the correct
        # value for grade2.
        elif counter == 3:
            grade3 = grade
        elif counter == 4:
            grade4 = grade
        elif counter == 5:
            grade5 = grade
        counter += 1
    # Shortcut operator +=1 saves counter as (counter = counter+1)

    # GPA Calculator
    # The addition operator (+) is used to add to numeric values.
    # The division operator (/) is used to divide two values.

    gpa_this_semester = (
            grade1 + grade2 + grade3 + grade4 + grade5) / num_classes
    print("Your projected GPA this semester is: ", round(gpa_this_semester, 2))

    # A conservative gpa can be obtained using
    # the floor division operator (//).
    # It will round down to the nearest integer.

    floor_gpa_this_smtr = (
            grade1 + grade2 + grade3 + grade4 + grade5) // num_classes
    print("A conservative projected GPA for this semester is: ",
          floor_gpa_this_smtr)

    # Projected GPA Calculator
    pct_cred_hours_this_semester = cred_hours / (cred_hours + prev_ch)
    pct_cred_hours_prev_semesters = prev_ch / (cred_hours + prev_ch)
    projected_gpa = (gpa_this_semester * pct_cred_hours_this_semester) + \
                    (prev_gpa * pct_cred_hours_prev_semesters)
    print("Your projected total GPA after this semester is: ",
          round(projected_gpa, 2))


# The following function will display the modulus operator.
def mod(num1, num2):
    """This function is a modulus calculator"""
    modulo = (num1 % num2)
    return modulo


def modulus():
    """
    This function asks users for valid input and uses the mod function to
    output a value
    """
    good_input = False
    while good_input is False:
        try:
            user_input1 = int(input("Enter an integer larger than 1: "))
            if user_input1 > 1:
                good_input = True
        except ValueError:
            print("Please enter a whole number larger than 1.")
    good_input = False
    while good_input is False:
        try:
            user_input2 = int(input("Enter a larger number: "))
            if user_input2 > user_input1:
                good_input = True
        except ValueError:
            print("Please enter an integer greater than the first one.")

    my_modulus = mod(user_input2, user_input1)
    print(user_input2, "modulus", user_input1, "=", my_modulus)


def main():
    """
    This will call the gpa_calc() function and modulus() function to run them
    """
    gpa_calc()
    modulus()


if __name__ == "__main__":
    main()
