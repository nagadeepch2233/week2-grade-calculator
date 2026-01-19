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

        maths = get_mark("Enter Maths marks: ")
        science = get_mark("Enter Science marks: ")
        social = get_mark("Enter Social marks: ")

        marks = [maths, science, social]

        average = sum(marks) / 3
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
    print(f"{'Name':15}{'Maths':>7}{'Science':>9}{'Social':>9}{'Avg':>8}{'Grade':>8}  Comment")
    print("-" * 75)

    averages = []

    for r in results:
        averages.append(r["average"])
        print(
            f"{r['name']:15}"
            f"{r['marks'][0]:7.1f}"
            f"{r['marks'][1]:9.1f}"
            f"{r['marks'][2]:9.1f}"
            f"{r['average']:8.2f}"
            f"{r['grade']:>8}  "
            f"{r['comment']}"
        )

    print("-" * 75)
    print(f"Class Average: {sum(averages) / len(averages):.2f}")
    print(f"Highest Average: {max(averages):.2f}")
    print(f"Lowest Average: {min(averages):.2f}")

def menu():
    results = []
    
    while True:
        print("\n--- Student Grade Calculator Menu ---")
        print("1. Enter student data")
        print("2. Display results")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            results = enter_students()
        elif choice == "2":
            if results:
                display_results(results)
            else:
                print("No data available.")
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
