# print('lmao lmao lmao')

# students = []
# courses = []

# num_students = int(input("Input number of student(s): "))
# def input_students_info():
#     student = {}
#     student['id'] = input("Input student ID: ")
#     student['name'] = input("Input student name: ")
#     student['dob'] = input("Input student date of birth: ")
#     return student
# for _ in range(num_students):
#     student  = input_students_info()
#     students.append(student)

# num_courses = int(input("Input number of course(s): "))
# def input_courses_info():
#     # global course
#     course = {}
#     course['id'] = input("Input course ID: ")
#     course['name'] = input("Input course name: ")
#     return course
# for _ in range(num_courses):
#     course = input_courses_info()
#     courses.append(course)

# def input_student_marks():
#     for course in courses:
#         course_id = input("Enter the course ID to input marks for: ")
#         if course_id == 'None':
#             break
#         else:
#             while course['id'] != course_id:
#                 course_id = input("Enter correct course ID to input marks(Or type 'None' to exit): ")
#                 if course_id == 'None':
#                     break
#             if course_id == 'None':
#                 break
#         for course in courses:
#             if course['id'] == course_id:
#                 for student in students:
#                     marks = float(input(f"Enter marks for student {student['name']} in course {course['name']}: "))
#                     student.setdefault("marks", {})[course_id] = marks
#                 break

# def show_student_marks():
#     for course in courses:
#         course_id = input("Enter the course ID to show student marks for(or type 'None' to exit): ")
#         if course_id == 'None':
#             break
#         else:
#             while course['id'] != course_id:
#                 course_id = input("Enter correct course ID to show student marks(Or type 'None' to exit): ")
#                 if course_id == 'None':
#                     break
#             if course_id == 'None':
#                 break
#         for course in courses:
#             if course["id"] == course_id:
#                 print(f"Course: {course['name']}")
#                 for student in students:
#                     marks = student.get("marks", {}).get(course_id, "N/A")
#                     print(f"Student: {student['name']}, Marks: {marks}")
#                 break

# input_student_marks()
# show_student_marks()

# print(students)
# print(courses)



class Students:
    all = []

    def __init__(self, n, i, b):
        self.name = n
        self.id = i
        self.dob = b

        Students.all.append(self)

    def __repr__(self):   # CHANGE THE REPRESENTING WAY OF THE LIST 
        return f"{self.__class__.__name__}('{self.name}', {self.id}, {self.dob})"
     
class Courses:
    all = []

    def __init__(self, n, i):
        self.name = n
        self.id = i

        Courses.all.append(self)
    
    def __repr__(self):   # CHANGE THE REPRESENTING WAY OF THE LIST 
        return f"{self.__class__.__name__}('{self.name}', {self.id})"
    
def InputMarks():
    for self in Courses.all:
        course_id = input("Enter the course ID to input marks for: ")
        if course_id == 'None':
            break
        else:
            while self.id != course_id:
                course_id = input("Enter correct course ID to input marks(Or type 'None' to exit): ")
                if course_id == 'None':
                    break
            if course_id == 'None':
                break
        for self in Students.all:
            self.mark = float(input(f'Enter mark for student {self.name}: '))

def ShowMarks():
    for self in Courses.all:
        print(f'Course: {self.id}')
        for self in Students.all:
            print(f'Student {self.name}, mark is {self.mark}')
   

Minh = Students('Minh', '22bi13306', '30/01/2004')
Nhu = Students('Nhu', '22bi13353', '14/07/2004')

Math = Courses('Math', 'M.01')
Code = Courses('Code', 'C.01')

print(Students.all)
print(Courses.all)

InputMarks()

ShowMarks()




        


