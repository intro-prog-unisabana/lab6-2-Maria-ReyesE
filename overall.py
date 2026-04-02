def student_averages(students):
    result = {}

    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)

    return result


def assignment_averages(students):
    result = {}
    
    for grades in students.values():
        for assignment, score in grades.items():
            if assignment not in result:
                result[assignment] = []
            result[assignment].append(score)

    for assignment in result:
        avg = sum(result[assignment]) / len(result[assignment])
        result[assignment] = round(avg)

    return result
