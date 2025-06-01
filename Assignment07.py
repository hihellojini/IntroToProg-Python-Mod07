# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   JDuldulao, 05/30/2025, Created Script
# ------------------------------------------------------------------------------------------ #
import json

# Data Constants Definition
MENU: str = """
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
"""
FILE_NAME: str = "Enrollments.json"

# Data Variables Definition
menu_choice: str = ""  # Hold the choice made by the user
students: list = []  # a table of student data

# Processing
# Start of class FileProcessor
# ------------------------------------------------------------------------------------------ #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created class
    """
    @staticmethod
    def read_data_from_file(file_name: str, student_data: list):
        """
        This function reads data from a json file and loads it into a list of dictionary
        rows then returns the list filled with student data.

        ChangeLog: (Who, When, What)
            JDuldulao, 05/30/2025, Created function

        :param file_name: string data with name of file to read from
        :param student_data: list of dictionaries with student data

        :return: list
        """
        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")

            list_of_dictionary_data = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            # TODO replace this line of code to convert dictionary data to Student data
            for student in list_of_dictionary_data:  # Convert the list of dictionary rows into Student objects
                student_objects: Student = Student(student_first_name=student["FirstName"],
                                                  student_last_name= student["LastName"],
                                                  course_name=student["CourseName"])
                student_data.append(student_objects)
            file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and not file.closed:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created function

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file = None

        try:
            # TODO Add code to convert Student objects into dictionaries
            list_of_dictionary_data: list = []

            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.student_first_name, "LastName": student.student_last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file)
            file.close()

            IO.output_student_courses(student_data)

        except TypeError as e:
            IO.output_error_messages("Please make sure that the data is a valid JSON format!\n", e)
        except Exception as e:
            IO.output_error_messages("\nThere was a non-specific error!\n", e)
        finally:
            if file is not None and not file.closed:
                file.close()
# ------------------------------------------------------------------------------------------ #
# End of class FileProcessor

# Presentation
# Start of class IO
# ------------------------------------------------------------------------------------------ #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created Class
        JDuldulao, 05/30/2025, Added menu output and input functions
        JDuldulao, 05/30/2025, Added a function to display the data
        JDuldulao, 05/30/2025, Added a function to display custom error messages
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """
        This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """
        This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created function


        :return: None
        """
        print(menu)

    @staticmethod
    def input_menu_choice():
        """
        This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            print() # Adding extra space to make it look nicer
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This function displays the student's name and course separated by comma. Each
        entry is separated by a new line.

        ChangeLog: (Who, When, What)
        JDuldulao, 05/24/2025, Created function

        :return: None
        """
        print("The following students are currently enrolled")
        print("-" * 50)
        for student in student_data:
            message = " {},{},{}."
            print(message.format(student.student_first_name, student.student_last_name,
                student.course_name))
        print("-"*50)

    @staticmethod
    def input_student_data(student_data: list):
        """
        This function gets to User first name, last name, and course name.
        This function will produce an error if user enter a number.

        :param student_data: list of dictionary rows to be filled with input data
        :return: list

         ChangeLog: (Who, When, What)
            JDuldulao, 5/30/2025, Created Function
        """
        try:
            student = Student()
            student.student_first_name = input("Enter the student's first name: ")
            student.student_last_name = input("Enter the student's last name: ")
            student.course_name = input("Enter the student's course name: ")
            student_data.append(student)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data
# ------------------------------------------------------------------------------------------ #
# End of class IO

# TODO Create a Person Class
# Start of class Person
# ------------------------------------------------------------------------------------------ #
class Person:
    """
    A class representing person data.

    Properties:
        student_first_name (str): The student's first name.
        student_last_name (str): The student's last name.

    ChangeLog:
        JDuldulao, 05/30/2025, Created the class.
    """

    # TODO Add student_first_name and student_last_name properties to the constructor
    def __init__(self, student_first_name: str = "", student_last_name: str = ""):
        self.__student_first_name = student_first_name
        self.__student_last_name = student_last_name

    # TODO Create a getter and setter for the student_first_name property
    @property  # (Use this decorator for the getter or accessor)
    def student_first_name(self):
        return self.__student_first_name.title() # formatting code

    @student_first_name.setter
    def student_first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__student_first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # TODO Create a getter and setter for the student_last_name property
    @property
    def student_last_name(self):
        return self.__student_last_name.title()  # formatting code

    @student_last_name.setter
    def student_last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__student_last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data
    def __str__(self):
        return f"{self.student_first_name},{self.student_last_name}"
# ------------------------------------------------------------------------------------------ #
# End of class Person

# TODO Create a Student class the inherits from the Person class
# Start of class Student
# ------------------------------------------------------------------------------------------ #
class Student(Person):
    """
    A class representing student data.

    Properties:
        student_first_name (str): The student's first name.
        student_last_name (str): The student's last name.
        course_name (str): The student's course name.

    ChangeLog: (Who, When, What)
        JDuldulao, 05/30/2025, Created Class
    """

    # TODO call to the Person constructor and pass it the student_first_name and student_last_name data
    def __init__(self, student_first_name: str = "", student_last_name: str = "", course_name: str = ""):
        super().__init__(student_first_name=student_first_name, student_last_name=student_last_name)

        # TODO add a assignment to the course_name property using the course_name parameter
        self.__course_name = course_name

    # TODO add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.title()

    # TODO add the setter for course_name2
    @course_name.setter
    def course_name(self, value: str):
        self.__course_name = value

    # TODO Override the __str__() method to return the Student data
    def __str__(self):
        return f"{self.student_first_name},{self.student_last_name},{self.course_name}"
# ------------------------------------------------------------------------------------------ #
# End of class Student

# Beginning of the main body of this script
# ------------------------------------------------------------------------------------------ #
# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)

# Present and Process the data
while True:  # Repeat the follow tasks

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_courses(student_data=students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the while loop

print("Program Ended")
