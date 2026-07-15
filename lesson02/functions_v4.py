def calculate_student_average(
    math_score: float = 50.0,
    science_score: float = 50.0,
    english_score: float = 50.0,
    number_of_subjects: int = 3,
) -> float:
    total_score = math_score + science_score + english_score
    average_score = total_score / number_of_subjects
    return round(average_score, 2)


# *args (arguments) and **kwargs (key-word arguments)

def stock_prices(*args, **kwargs):
    print(f"argument is: {args}")
    print(f"kwargs is: {kwargs}")


math_score = 85.
science_score = 90.
english_score = 78.
number_of_subjects = 3

# args
avg = calculate_student_average(math_score, science_score, english_score, number_of_subjects)
print(f"Average score is: {avg:.4f}")

# kwargs 
avg = calculate_student_average(math_score=math_score, science_score=science_score, english_score=english_score, number_of_subjects=number_of_subjects)
print(f"Average score is: {avg:.4f}")

stock_prices(60, 87, 95, 77, name="TESLA", exchange="NY", price=450.0, ceo="Elon Musk")