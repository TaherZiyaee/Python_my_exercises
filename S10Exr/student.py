class Student:
    def __int__(self, name: str, score: float) -> None:
        self.name = name
        self.age = 0
        self.score = score

    def get_student_specs(self):
        print("-- Please enter student specifications --")
        self.name = input("Name: ")
        self.age = input("Age: ")
        self.score = input("Score: ")

    def show_student(self):
        print(f"Name: {self.name}\nAge: {self.age}\nScore: {self.score}")


student = None


def get_student():
    global student
    if not student:
        student = Student()
    return student


def main():
    student = get_student()
    student.get_student_specs()


if __name__ == "__main__":
    main()
