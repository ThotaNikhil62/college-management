Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class College:
...     collegename = "Indian Express College"
...     branch = "A23,BBSR,India"
... 
...     # Create student profile
...     def _init_(self, studentname, rollno, course):
...         self.studentname = studentname
...         self.rollno = rollno
...         self.course = course
...         self.grades = {}  # Dictionary to store grades for each course
...         print(f'Hello {self.studentname}! Your profile is created successfully.')
... 
...     # Enroll in new course
...     def enroll_course(self, course_name):
...         if course_name not in self.grades:
...             self.grades[course_name] = None  # Grade is set to None initially
...             print(f'{self.studentname} enrolled in {course_name} successfully.')
...         else:
...             print(f'Already enrolled in {course_name}.')
... 
...     # Add or update grade for a course
...     def add_grade(self, course_name, grade):
...         if course_name in self.grades:
...             self.grades[course_name] = grade
...             print(f'Grade for {course_name} updated to {grade}.')
...         else:
...             print(f'You are not enrolled in {course_name}.')
... 
...     # View grades
...     def view_grades(self):
...         if not self.grades:
...             print('No courses enrolled yet.')
...         else:
...             print(f'Grades for {self.studentname}:')
...             for course, grade in self.grades.items():
...                 if grade is not None:
...                     print(f'{course}: {grade}')
...                 else:
...                     print(f'{course}: No grade yet.')
... 
... print(f'Welcome to {College.collegename}, {College.branch}')
... # Collect student data for registration
... studentname = input('Enter your name: ')
... rollno = input('Enter your roll number: ')
... course = input('Enter your course of study: ')

# Object creation based on user-provided data
student = College(studentname, rollno, course)

while True:
    print('\nPlease select any option: ')
    print('1. Enroll in a new course\n2. Add/Update Grade\n3. View Grades\n4. Stop')
    option = int(input(' '))

    if option == 1:
        course_name = input('Enter the course name you want to enroll in: ')
        student.enroll_course(course_name)

    elif option == 2:
        course_name = input('Enter the course name: ')
        grade = input(f'Enter the grade for {course_name}: ')
        student.add_grade(course_name, grade)

    elif option == 3:
        student.view_grades()

    elif option == 4:
        print('Thanks for using Indian Express College System....')
        break

    else:
        print('Invalid Option! Please select a valid option...')
