# Student Result Management System

## 1. Project Overview

The Student Result Management System is a Python-based command-line application
designed to manage student information, subject marks, and academic results.
The system allows users to add, view, search, update, and delete student records. It also
provides features for entering marks, calculating total marks and percentage, assigning
grades, checking pass/fail status, generating student rankings, calculating class statistics, and
performing subject-wise analysis.
Student records are stored in a CSV file so that the data can be saved and accessed when the
program is run again.

## 2. Problem Statement

The Student Result Management System is developed to provide a computerized solution for
managing student information and academic results. The system allows users to store student
details, enter marks, calculate results automatically, search and modify records, and analyze
overall class performance.

## 3. Features

1.Add student records
2.View all students
3.Search student by roll number or name
4.Update student details
5.Delete student records
6.Enter and update subject marks
7.Calculate total marks
8.Calculate percentage
9.Calculate grade
10.Check pass/fail status
11.Generate student marksheet
12.Calculate class statistics
13.Generate student ranking
14.Perform subject-wise analysis
15.Store records using CSV file handling
16.Validate marks between 0 and 100
17.Handle invalid user input

## 4. Technologies Used

-Python 3
-Python Classes and Objects
-Functions
-Lists
-Loops
-Conditional Statements
-Input Validation
-Python `unittest`
-Command-line interface (CLI)
No external Python libraries are required.

## 5. Project Structure

student-result-management-system/
├── main.py
├── statement.md
├── README.md
├── students.csv

The program automatically creates:
students.csv
When student data is saved.

## 6. Requirements

Python 3 must be installed on the computer.

Check the installed Python version:
python3 --version

For Windows, you can also use:
python –version

## 7. Installation and Setup

1.Clone the Repository

https://github.com/shrayashisingh05/student-result-management-system.git

2.Open the Project Folder
cd student-result-management-system

3.Run the Program
On macOS/Linux:
python3 main.py
On Windows:
python main.py
No external packages need to be installed.

## 8.Main Menu

# When the program starts, the following menu is displayed:

# STUDENT RESULT MANAGEMENT SYSTEM

1.Add Student
2.View All Students
3.Search Student
4.Update Student
5.Delete Student
6.Enter / Update Marks
7.View Student Result
8.Class Statistics
9.Student Ranking
10.Subject Analysis
11.Exit

Enter your choice:

## 9.Complete Usage Workflow

Step 1 – Add Student

Select option 1 and enter:
• Roll number
• Student name
• Course
The new student is added to the system.

Step 2 – Enter Marks

Select option 6, enter the student's roll number, and provide marks for all five subjects.
Marks must be between 0 and 100.

Step 3 – View Student Result

Select option 7 and enter the student's roll number.
The system displays:
• Student details
• Subject marks
• Total marks
• Percentage
• Grade
• Pass/fail status

Step 4 – Search Student

Select option 3 to search using a student's roll number or name.

Step 5 – View Class Statistics

Select option 8 to display:
• Number of students
• Class average
• Highest percentage
• Lowest percentage
• Number of passed students
• Number of failed students

Step 6 – View Student Ranking

Select option 9 to display students ranked according to their percentage.

Step 7 – Subject Analysis

Select option 10 to view the average, highest, and lowest marks for each subject.

Step 8 – Update or Delete Records

Use option 4 to update student details and option 5 to delete a student record.

Step 9 – Exit

Select option 11 to close the application.

## 10.Sample Result

========================================
MARKSHEET
========================================
Name : Rahul Sharma
Roll Number: 101
Course : CSE

---

Mathematics : 85
Physics : 78
Python : 92
English : 81
EVS : 88

---

Total : 424.00/500
Percentage : 84.80%
Grade : A
Status : PASS

## 11.Data Storage

Student records are stored in:
students.csv

The CSV file is automatically created when student information is saved.

It contains fields such as:
• Roll no
• name
• course
• Mathematics
• Physics
• Python
• English
• EVS

## 12.Error Handling

The system handles:
• Invalid menu choices
• Duplicate roll numbers
• Student not found
• Invalid marks
• Marks below 0
• Marks above 100
• Non-numeric marks
• Empty or invalid searches

Appropriate messages are displayed to the user when an invalid input is entered.

## 13.Future Imporvements

Possible future improvements include:

• Admin and student login
• Database integration
• Graphical user interface
• PDF marksheet generation
• Multiple semesters
• Attendance management
• Excel export
• Password protection
• Graphical performance charts
• Detailed academic reports

## 14.Conclusion

The Student Result Management System provides a simple way to manage student academic records through a command-line interface.

The project demonstrates important Python concepts including functions, loops, conditional statements, lists, dictionaries, CSV file handling, input validation, and exception handling.

The system reduces manual result calculations and provides useful features for managing and analyzing student academic performance.
