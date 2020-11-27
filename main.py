import csv
from helpers import *
from student import Student

def readFile(fileName):
    students = []
    majors = []
    
    with open (fileName, newline = '') as dataset:
        reader = csv.reader(dataset, delimiter=',')
        next(reader)

        for row in reader:
            
            id = row[0]
            major = row[2]
            ch = int(row[4])
            cr = int(row[3])*ch
            i = findStudentIndexByID(id, students)
            
            if i == None:
                newStudent = Student(id, major)
                students.append(newStudent)
                students[-1].cr += cr
                students[-1].ch += ch 
                
            else:
                i = findStudentIndexByID(id, students)
                students[i].cr += cr
                students[i].ch += ch
            
            if major not in majors:
                majors.append(major)

    calculateFinalCR(students)
    return students, majors

def main():

    try:
        students, majors = readFile('notas.csv')
        displayStudents(students)
        displayMajors(students, majors)
    
    except FileNotFoundError:
        print('Erro: não foi possível encontrar o arquivo')

main()