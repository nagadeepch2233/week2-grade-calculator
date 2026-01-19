def determine_grade(avg):
    if 90 <= avg <= 100:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 60 <= avg < 70:
        return "D"
    else:
        return "F"

def grade_comment(grade):
    comments = {
        "A": "Excellent",
        "B": "Very good",
        "C": "Good, keep improving",
        "D": "Needs improvement",
        "F": "Fail, must work harder"
    }
    return comments.get(grade, "No comment")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a number.")

def get_mark(prompt):
    while True:
        try:
            mark = float(input(prompt))
            if 0 <= mark <= 100:
                return mark
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")

def enter_students():
    num_students = get_positive_int("How many students? ")

    results = []

    for i in range(num_students):
        print(f"\nEntering data for Student {i + 1}")
        name = input("Student name: ")

        marks = []
        for s in range(1, 4):
            marks.append(get_mark(f"Enter marks for subject {s}: "))

        average = sum(marks) / len(marks)
        grade = determine_grade(average)
        comment = grade_comment(grade)

        results.append({
            "name": name,
            "marks": marks,
            "average": average,
            "grade": grade,
            "comment": comment
        })

    return results

def display_results(results):
    print("\n" + "-" * 75)
    print(f"{'Name':15}{'Sub1':>7}{'Sub2':>7}{'Sub3':>7}{'Avg':>8}{'Grade':>8}  Comment")
    print("-" * 75)

    averages = []

    for r in results:
        
        averages.append(r["average"])
        print(
            f"{r['name']:15}"
            f"{r['marks'][0]:7.1f}"
            f"{r['marks'][1]:7.1f}"
            f"{r['marks'][2]:7.1f}"
            f"{r['average']:8.2f}"
            f"{r['comment']}"
        )

    print("-" * 75)
    print(f"Class Average: {sum(averages) / len(averages):.2f}")
    print(f"Highest Average: {max(averages):.2f}")
    print(f"Lowest Average: {min(averages):.2f}")

def search_student(results):
    name = input("Enter student name to search: ").lower()
    for r in results:
        if r["name"].lower() == name:
            print("\nStudent Found:")
            print(r)
            return
    print("Student not found.")

def save_to_file(results):
    filename = "student_results.txt"
    with open(filename, "w") as file:
        for r in results:
            file.write(
                f"{r['name']}, Marks: {r['marks']}, "
                f"Average: {r['average']:.2f}, "
                f"Grade: {r['grade']}, Comment: {r['comment']}\n"
            )
    print(f"Results saved to {filename}")

def menu():
    results = []

    while True:
        print("\n--- Student Grade Calculator Menu ---")
        print("1. Enter student data")
        print("2. Display results")
        print("3.Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            results = enter_students()
        elif choice == "2":
            if results:
                display_results(results)
            else:
                print("No data available.")
        elif choice == "3":
            if results:
                search_student(results)
            else:
                print("No data available.") 
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
