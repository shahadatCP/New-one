class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(self, student_info):
        self.student_list.append(student_info)


class Student:
    def __init__(self, student_id, name, department, is_enrolled):
        self.__student_id = student_id
        self.__name = name
        self.__department = department
        self.__is_enrolled = is_enrolled

    @property
    def student_id(self):
        return self.__student_id
    
    @property
    def is_enrolled(self):
        return self.__is_enrolled
    
    @is_enrolled.setter
    def is_enrolled(self, value):
        self.__is_enrolled = value
    
    def enroll_student(self):
        if not self.is_enrolled:
            self.is_enrolled = True
            print(f'{self.__name} enrolled successfully')
            return
        print(f'{self.__name} already enrolled')

    def drop_student(self):
        if self.is_enrolled:
            self.is_enrolled = False
            print(f'Student {self.student_id} has been dropped')
            return
        print(f'{self.__name} is not enrolled yet')
    
    def view_student_info(self):
        print(f'ID: {self.student_id}, Name: {self.__name}, Department: {self.__department}, Enrolled:{self.is_enrolled}')



s1 = Student('S101', 'Alice Smith', 'Computer Science', False)
StudentDatabase.add_student(s1)
s2 = Student('S102', 'Bob Johnson', 'Mathematics', False)
StudentDatabase.add_student(s2)
s3 = Student('S103', 'Charlie Lee', 'Physics', False)
StudentDatabase.add_student(s3)



while True:
    print("\n--- Student Management Menu ---")
    print("1. View All Students")
    print("2. Enroll Student")
    print("3. Drop Student")
    print("4. Exit")

    choice = input('Enter your choice (1-4): ')

    if choice == '1':
        for student in StudentDatabase.student_list:
            student.view_student_info()
    
    elif choice == '2':
        id = input('Enter Student ID to enroll: ')
        yes = False
        for student in StudentDatabase.student_list:
            if student.student_id == id:
                student.enroll_student()
                yes = True
                break
        if not yes:
            print(f'Error: No student found with ID {id}')
    
    elif choice == '3':
        id = input('Enter Student ID to drop: ')
        yes = False
        for student in StudentDatabase.student_list:
            if student.student_id == id:
                student.drop_student()
                yes = True
                break
        if not yes:
            print(f'Error: No student found with ID {id}')
    
    elif choice == '4':
        print('Program exit successfully')
        break

    else:
        print('Please choose the correct option')