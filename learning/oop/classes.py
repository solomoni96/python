class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):
        return self.grade


class Course:
    school_name = "Something Academy"

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if (len(self.students) >= self.capacity):
            print(f"At capacity! {student.name} can't join...\n")
            return

        self.students.append(student)

        print(f"{student.name} has joined the course!")
        Course.greeting()

    def get_average_grade(self):
        average = 0
        for st in self.students:
            average += st.get_grade()

        average = average / len(self.students)

        print(f"Average grade for {self.name} is {average}\n")

    @classmethod
    def greeting(cls):
        print(f"Welcome to {cls.school_name}!\n")

    @staticmethod
    def opening_msg():
        print("A new course is available.\n")


student1 = Student('Joe', 21, 92)
student2 = Student('Jill', 21, 76)
student3 = Student('James', 21, 94)

course = Course("English", 2)
Course.opening_msg()

course.add_student(student1)
course.add_student(student2)
course.add_student(student3)

course.get_average_grade()
