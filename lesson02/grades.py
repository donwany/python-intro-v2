def calculate_student_average(math_score: float = 50.0, science_score: float=50.0, english_score: float=50.0, number_of_subjects: int = 3) -> float:
    total_score = math_score + science_score + english_score
    average_score = total_score / number_of_subjects
    return round(average_score, 2)

def assign_student_grade(average_score: float) -> str:

    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    else:
        grade = 'F'

    return grade


def calculate_student_grade(math_score: float = 50.0, science_score: float=50.0, english_score: float=50.0, number_of_subjects: int = 3) -> dict:
    total_score = math_score + science_score + english_score
    average_score = total_score / number_of_subjects

    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    else:
        grade = 'F'

    return {"avg": round(average_score, 2), "grade": grade, "total_score": total_score}


def calculate_student_grade_v2(math_score: float = 50.0, science_score: float=50.0, english_score: float=50.0, number_of_subjects: int = 3):
    total_score = math_score + science_score + english_score
    average_score = total_score / number_of_subjects

    if average_score >= 90:
        grade = 'A'
    elif average_score >= 80:
        grade = 'B'
    elif average_score >= 70:
        grade = 'C'
    else:
        grade = 'F'

    return round(average_score, 2), grade

def calc_stu_avg():
    pass

def calculateStudentAverage():
    pass