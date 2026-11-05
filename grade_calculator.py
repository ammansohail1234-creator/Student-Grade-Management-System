
def calculate_grade(marks):
    """Calculate a student's grade."""

    average = sum(marks) / len(marks)

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def calculate_average(marks):
    """Calculate average marks."""

    if not marks:
        return 0

    return sum(marks) / len(marks)
