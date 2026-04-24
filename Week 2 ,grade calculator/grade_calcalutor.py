def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def get_encouraging_message(grade):
    messages = {
        "A": "Outstanding! You're absolutely crushing it",
        "B": "Very Good! Keep it up",
        "C": "Good effort! A little more push and you'll shine",
        "D": "Don't give up! Keep working hard, you can do better",
        "F": "Believe in yourself! Every expert was once a beginner. Keep going!"
    }
    return messages[grade]


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Invalid input! Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input! Please enter a numeric value.")


def main():
    print("=" * 40)
    print(" STUDENT GRADE CALCULATOR")
    print("=" * 40)

    name = input("Enter student name: ").strip()
    while not name:
        print(" Name cannot be empty. Please try again.")
        name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade = get_grade(marks)
    message = get_encouraging_message(grade)

    print()
    print("=" * 40)
    print(f" RESULT FOR {name.upper()}:")
    print(f"   Marks  : {marks}/100")
    print(f"   Grade  : {grade}")
    print(f"   Message: {message}")
    print("=" * 40)

if __name__ == "__main__":
    main(
