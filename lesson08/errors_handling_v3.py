def calculate_scores(score: int):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)


def calculate_student_scores(score: int):
    try:
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100")
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)
    except ValueError as ex:
        print(f"Invalid input: {ex}")


if __name__ == '__main__':
    # Method 1\
    marks = float(input("Enter your score: "))
    try:
        calculate_scores(score=marks)
    except ValueError as ex:
        print(f"Invalid input: {ex}")

    # Method 2
    calculate_student_scores(marks)
