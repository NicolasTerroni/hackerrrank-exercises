def find_lowest_grade_students(students_dict):
    lowest_grade_value = 100.0
    for key, value in students_dict.items():
        if value < lowest_grade_value:
            lowest_grade_value = value

    lowest_grade_students = [name for name, grade in students_dict.items() if grade == lowest_grade_value]
    return lowest_grade_students

if __name__ == '__main__':
    students_grades = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_grades[name]=score

lowest_grade_students = find_lowest_grade_students(students_grades)

for student in lowest_grade_students:
    students_grades.pop(student)

second_lowed_students = find_lowest_grade_students(students_grades)
for i in sorted(second_lowed_students):
    print(i)


# Dicts are more usefull, sorry