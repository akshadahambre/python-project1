def welcome():
    print(" Welcome to Student Grade Management System ")
    print("You can add students, enter their marks, and view grades.\n")

def get_student_details():
    name = input("Enter student name: ")
    while True:
        try:
            marks = float(input(f"Enter marks for {name} (0-100): "))
            if 0 <= marks <= 100:
                return name, marks
            else:
                print(" Marks should be between 0 and 100.")
        except ValueError:
            print(" Invalid input! Enter a number.")

def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B+"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "F"

def display_students(students):
    print("\n Student Grades ")
    print("---------------------------")
    print(f"{'Name':15} {'Marks':10} {'Grade':5}")
    print("---------------------------")
    for student in students:
        print(f"{student['name']:15}  {student['marks']:<10} {student['grade']:5}")
    print("---------------------------\n")

def main():
    welcome()
    students = []

    while True:
        print("Options:")
        print("1. Add a student")
        print("2. View all students and grades")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name, marks = get_student_details()
            grade = calculate_grade(marks)
            students.append({'name': name, 'marks': marks, 'grade': grade})
            print(f" Student {name} added successfully!\n")
        elif choice == '2':
            if students:
                display_students(students)
            else:
                print(" No students added yet!\n")
        elif choice == '3':
            print(" Exiting Student Grade Management System. Goodbye!")
            break
        else:
            print(" Invalid choice! Enter 1, 2, or 3.\n")

# Run the program
main()