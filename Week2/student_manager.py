# Global variable example - accessible everywhere
student_database = []

class Student:
    def __init__(self, name, age, student_id):
        # These are local to the object instance
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        # Function 1: method inside the class
        return f"Name: {self.name}, Age: {self.age}"

def collect_student_data():
    # Function 2: gets input from user
    # 'count' is a local variable only used in this function
    count = 3
    print(f"Enter details for {count} students:")

    for i in range(count):
        print(f"\nStudent {i + 1}:")
        name = input("Enter name: ")

        # Basic validation for age
        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                print("Age must be a number. Try again.")

        student_id = input("Enter student ID: ")

        # Create Student object and add to global list
        new_student = Student(name, age, student_id)
        student_database.append(new_student)

def print_student_list():
    # Function 3: prints the results
    print("\n--- Student List ---")
    # Sort by age to show 'in order' requirement
    sorted_students = sorted(student_database, key=lambda s: s.age)

    for student in sorted_students:
        print(student.display_info())

if __name__ == "__main__":
    collect_student_data()
    print_student_list()