if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

student_notes = student_marks[query_name]

student_average = sum(student_notes)/len(student_notes)
format_student_average = "{:.2f}".format(student_average)
print(format_student_average)