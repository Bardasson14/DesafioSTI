def findStudentIndexByID (id, students):
    for i in range(len(students)):
        if students[i].id == id:
            return i

def getAvgCR(major_id, students, majors):
    major_students = [s for s in students if s.major == major_id]
    total = 0
    for student in major_students:
        total += student.cr
    return round(total/len(major_students))

def calculateFinalCR(students):
    for s in students:
        s.cr = round(s.cr/s.ch)

def displayStudents(students):
    print("------- O CR dos alunos é: --------")
    for s in students:
        print(s.id, ' - ', s.cr)

def displayMajors(students, majors):  
    print("-----------------------------------")
    print("----- Média de CR dos cursos ------")
    parsed_majors = list(map(int, majors))
    sorted_majors = sorted(parsed_majors)
    for i in range(len(sorted_majors)):
        print(sorted_majors[i], ' - ', getAvgCR(str(sorted_majors[i]), students, sorted_majors))

