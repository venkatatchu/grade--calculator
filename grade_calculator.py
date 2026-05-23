def get_grade(marks):
    if marks >= 90:
        return "A", "Excellent! Outstanding performance! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 🔥"
    elif marks >= 70:
        return "C", "Good! You're doing well! 👍"
    elif marks >= 60:
        return "D", "Average. You can do better! 💪"
    else:
        return "F", "Failed. Please study harder! 📚"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid! Marks must be between 0 and 100. Try again.")
        except ValueError:
            print("❌ Invalid! Please enter a number. Try again.")


def main():
    name = input("Enter student name: ")
    marks = get_valid_marks()
    grade, message = get_grade(marks)

    print(f"\n🎯 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


main()
