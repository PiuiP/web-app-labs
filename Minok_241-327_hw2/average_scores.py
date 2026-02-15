def compute_average_scores(scores):
    subjects = len(scores)
    if subjects <= 0 or subjects > 100:
        return 'X is out of range (0, 100]'
    students = len(scores[0])
    if students <= 0 or students > 100:
        return 'N is out of range (0, 100]'
    students_scores = [0] * students
    for j in range(0, subjects):
        students_scores = [students_scores[i] + scores[j][i] for i in range(0, students)]
    return [i / subjects for i in students_scores]

