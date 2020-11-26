import csv
from helpers import *
from student import Student

def main():
    
    students = []
    majors = []
    
    with open ('notas.csv', newline = '') as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)

        for row in reader:
            newElement = False

            id = row[0]
            major = row[2]
            ch = float(row[4])
            cr = float(row[3])*ch
            
            if findStudentIndexByID(id, students) == None:
               newStudent = Student(id, major)
               students.append(newStudent)
               newElement = True

            if major not in majors:
                majors.append(major)

            if (newElement):
                students[-1].cr += cr
                students[-1].ch += ch 

            else:
                i = findStudentIndexByID(id, students)
                students[i].cr += cr
                students[i].ch += ch

    for s in students:
        s.cr = round(s.cr/s.ch)

    displayStudents(students)
    displayMajors(students, majors)


main()