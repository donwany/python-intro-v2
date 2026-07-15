from grades import calculate_student_average, calculate_student_grade, calculate_student_grade_v2, assign_student_grade
from arith import add, subtract, multiply, divide

math_score = 85.
science_score = 90.
english_score = 78.
number_of_subjects = 3

total_score = math_score + science_score + english_score
average_score = total_score / number_of_subjects

print(f"Average score is: {average_score:.4f}")
print(f"Average score is: {round(average_score, 4)}")

# convert the above code to reusable function 

# version 1
avg = calculate_student_average(math_score, science_score, english_score, number_of_subjects)
print(f"Average score is: {avg:.4f}")

# version 2
avg = calculate_student_average(math_score=49., science_score=99., english_score=67., number_of_subjects=3)
print(f"Average score is: {avg:.4f}")

# version 3
avg = calculate_student_average(math_score=math_score, science_score=science_score, english_score=english_score, number_of_subjects=number_of_subjects)
print(f"Average score is: {avg:.4f}")

# version 4
avg = calculate_student_average(math_score=49., science_score=99., english_score=67.)
print(f"Average score is: {avg:.4f}")
# version 5
avg = calculate_student_average()
print(f"Average score is: {avg:.4f}")

print("-"*50)

results = calculate_student_grade(math_score=49., science_score=99., english_score=67.)
print(f"Results: {results}")


avg, grade = calculate_student_grade_v2(math_score=49., science_score=99., english_score=67.)
print(f"Average score is: {avg} and the grade of the student is: {grade}")

print("-"*50)
avg = calculate_student_average(math_score=49., science_score=99., english_score=67., number_of_subjects=3)
print(f"Average score is: {avg}")

grade = assign_student_grade(average_score=avg)
# grade = assign_student_grade(avg)
print(f"Student grade is: {grade}")
