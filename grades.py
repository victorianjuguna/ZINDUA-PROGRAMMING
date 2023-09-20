def calculate_grade(score):
    if 70 <= score <= 100:
        return "A"
    elif 60 <= score < 69:
        return "B"
    elif 50 <= score < 59:
        return "C"
    elif 40<= score < 49:
        return "D"
    elif 0 <= score < 39:
        return "F"
    else:
        return "Invalid score"

try:
    score = float(input("Enter the student's score: "))
    if 0 <= score <= 100:
        grade = calculate_grade(score)
        print(f"The student's grade is: {grade}")
    else:
        print("Invalid score. Score must be between 0 and 100.")
except ValueError:
    print("Invalid input. Please enter a valid numeric score.")
