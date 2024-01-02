# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Function to input the number of students in a class
def input_number_of_students():
    return int(input("Enter the number of students in the class: "))

# Function to input student information
def input_student_information():
    student = {}
    student["id"] = input("Enter student ID: ")
    student["name"] = input("Enter student name: ")
    student["dob"] = input("Enter student date of birth: ")
    return student

# Function to input the number of courses
def input_number_of_courses():
    return int(input("Enter the number of courses: "))

# Function to input course information
def input_course_information():
    course = {}
    course["id"] = input("Enter course ID: ")
    course["name"] = input("Enter course name: ")
    return course

# Function to select a course and input marks for students in that course
def input_student_marks(students, courses):
    course_id = input("Enter the course ID to input marks for: ")
    for course in courses:
        if course["id"] == course_id:
            for student in students:
                marks = float(input(f"Enter marks for student {student['name']} in course {course['name']}: "))
                student.setdefault("marks", {})[course_id] = marks
            break

# Function to list all courses
def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"Course ID: {course['id']}, Course Name: {course['name']}")

# Function to list all students
def list_students(students):
    print("Students:")
    for student in students:
        print(f"Student ID: {student['id']}, Student Name: {student['name']}")

# Function to show student marks for a given course
def show_student_marks(students, courses):
    course_id = input("Enter the course ID to show student marks for: ")
    for course in courses:
        if course["id"] == course_id:
            print(f"Course: {course['name']}")
            for student in students:
                marks = student.get("marks", {}).get(course_id, "N/A")
                print(f"Student: {student['name']}, Marks: {marks}")
            break

# Main function
def main():
    students = []
    courses = []

    num_students = input_number_of_students()
    for _ in range(num_students):
        student = input_student_information()
        students.append(student)

    num_courses = input_number_of_courses()
    for _ in range(num_courses):
        course = input_course_information()
        courses.append(course)

    input_student_marks(students, courses)

    list_courses(courses)
    list_students(students)

    show_student_marks(students, courses)

# Run the main function
if __name__ == "__main__":
    main()
