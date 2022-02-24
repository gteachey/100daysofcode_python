my_student = {
    'name': 'Rolf Smith',
    'grades': [80, 79, 100, 92]
}


def average_grade(student):
    return sum(student['grades']) / len(student['grades'])


print(average_grade(my_student))
