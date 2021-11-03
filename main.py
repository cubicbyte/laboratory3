import os

def readFile(group):
    if isinstance(group, int):
        group = str(group)

    filename = 'group_' + group + '.txt'
    filepath = 'files/' + filename
    exists = os.path.exists('./' + filepath)

    if not exists:
        return None

    fs = open(filepath, mode='r', encoding='utf-8')
    rows = fs.readlines()
    students = {}

    for row in rows:
        row = row.replace('\n', '')
        if len(row) <= 1:
            continue
        chunks = row.split(' ')
        score = int(chunks[0])
        name = chunks[1] + ' ' + chunks[2]
        students[name] = score

    fs.close()
    return students

def writeFile(group, students):
    if isinstance(group, int):
        group = str(group)

    filename = 'group_' + group + '.txt'
    filepath = 'files/' + filename
    fs = open(filepath, mode='w', encoding='utf-8')

    for student in students:
        score = students[student]
        fs.write(str(score) + ' ' + student + '\n')

    fs.close()

def appendFile(group, student, score):
    if isinstance(group, int):
        group = str(group)
    if isinstance(score, int):
        score = str(score)

    filename = 'group_' + group + '.txt'
    filepath = 'files/' + filename
    fs = open(filepath, mode='a', encoding='utf-8')
    fs.write(score + ' ' + student + '\n')
    fs.close()

def sortFile(group):
    students = readFile(group)
    
    if students == None:
        return None
    
    sortedKeys = sorted(students, key=students.get)
    sortedStudents = {}
    for key in sortedKeys:
        sortedStudents[key] = students[key]
    
    writeFile(group, sortedStudents)
    return sortedStudents

def readDir():
    for filename in os.listdir('files'):
        group = filename.replace('group_', '').replace('.txt', '')
        students = readFile(group)
        studentsCount = len(students)
        print('Группа: ' + group + ', кол-во студентов: ' + str(studentsCount))

def findStudent(group, student):
    students = readFile(group)
    
    if students == None or not student in students:
        return None

    return students[student]

def unitFiles():
    filesList = os.listdir('files')
    fs = open('files/unitedGroups.txt', mode='w', encoding='utf-8')
    for filename in filesList:
        rfs = open('files/' + filename, mode='r', encoding='utf-8')
        lines = rfs.readlines()
        for line in lines:
            fs.write(line)
        rfs.close()
    fs.close()
    
while True:
    print('0 - завершить работу\n1 - вывести список групп\n2 - получить список студентов\n3 - перезаписать группу\n4 - добавить студента в группу\n5 - отсортировать группу по баллам\n6 - посмотреть балл студента\n7 - обьединить группы в одну')
    choice = input('Выберите действие >> ')

    if choice == '0':
        break
    elif choice == '1':
        readDir()
    elif choice == '2':
        group = input('Введите номер группы >> ')
        print(readFile(group))
    elif choice == '3':
        group = input('Введите номер группы >> ')
        students = {}
        while True:
            fname = input('Введите имя студента >> ')
            sname = input('Введите фамилию студента >> ')
            score = int(input('Введите балл студента >> '))
            students[fname + ' ' + sname] = score

            choice = input('Продолжить? (n - нет) >> ')
            if choice == 'n':
                break
        writeFile(group, students)
    elif choice == '4':
        group = input('Введите номер группы >> ')
        fname = input('Введите имя студента >> ')
        sname = input('Введите фамилию студента >> ')
        score = int(input('Введите балл студента >> '))
        appendFile(group, fname + ' ' + sname, score)
    elif choice == '5':
        group = input('Введите номер группы >> ')
        sortFile(group)
    elif choice == '6':
        group = input('Введите номер группы >> ')
        fname = input('Введите имя студента >> ')
        sname = input('Введите фамилию студента >> ')
        print(findStudent(group, fname + ' ' + sname))
    elif choice == '7':
        unitFiles()
    else:
        print('Неизвестная операция')
        break