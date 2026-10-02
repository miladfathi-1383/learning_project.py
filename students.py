
from colorama import Fore, Style, init
import json
from datetime import datetime
init()

last_id = None
first_id = 1000
ID_list = []
students = []


class Student:
    def __init__(self, name, age, student_id, attendance = None, note = '') -> None:
        self.name = name
        self.age = age
        self.student_id = student_id
        self.attendance = attendance
        self.note = note



def load_student():
    global students
    global last_id

    with open('students.json', 'r') as file:
        data = json.load(file)

    last_id = data['last_id']

    for student_data in data['students']:
        student = Student(
            student_data['name'],
            student_data['age'],
            student_data['ID']
        )

        students.append(student)
        ID_list.append(student.student_id)


def save_student():
    data = []

    for student in students:
        data.append({
            'name': student.name,
            'age': student.age,
            'ID': student.student_id

        })

    data_save = {
        'last_id': last_id,
        'students': data
    }

    with open('students.json', 'w') as file:
        json.dump(data_save, file, indent=4)


def get_name():

    while True:
        name = input('Name: ').strip()

        if name and name.replace(' ', '').isalpha():
            return name

        print(Fore.RED,'Please write a correct name!',Style.RESET_ALL)


def get_age():

    while True:
        try:
            age = int(input('age:'))

            if age <= 0:
                print('age shoud be bigger than zero!')
                continue

            elif age > 110:
                print('age should less than 110!')
                continue

            else:
                return age

        except:
            print('write corect age')


def add_student():
    global last_id

    name = get_name()
    age = get_age()

    if len(ID_list) == 0:
        student_id = first_id
        last_id = first_id

    else:
        last_id += 1
        student_id = last_id

    ID_list.append(student_id)

    student = Student(name, age, student_id)

    students.append(student)

    save_student()


def show_student():
    if len(students)== 0:
        print(Fore.RED,'you dont have any student!',Style.RESET_ALL)

    else:
        for student in students:
            print('name:',student.name, '\nage:',student.age, '\nID:', student.student_id)
            print(Fore.CYAN,'*'*40,Style.RESET_ALL)




def save_attendance():
    data = []
    today = datetime.now().strftime("%Y-%m-%d")
    for student in students:
        data.append({
            'name': student.name,
            'ID': student.student_id,
            'attendance': student.attendance
            
        })

    data_save = {
        'date' : today,
        'attendance': data
    }


    with  open('records.json', 'r') as file:
        records = json.load(file)

        
    for record in records['records']:
        if record['date'] == today:
            record['attendance'] = data
            break
    else:
        records['records'].append(data_save)  


    with open('records.json', 'w') as file:
        json.dump(records, file, indent=4)




def student_attendance():
    print(Fore.CYAN,'today:',datetime.now().strftime("%Y-%m-%d | %H:%M"), Style.RESET_ALL)
    if len(students) == 0:
        print(Fore.RED,'you dont have any student!',Style.RESET_ALL)
    else:
        for student in students:
            while True:
                print('name:',student.name)
                print('1.present   2.absent   3.late   4.exused')
                attendance = input('\tattendance:')
                if attendance == '1' or '':
                    student.attendance = 'present'
                    break
                elif attendance == '2':
                    student.attendance = 'absent'
                    break
                elif attendance == '3':
                    student.attendance = 'late'
                    break
                elif attendance == '4':
                    student.attendance = 'exused'
                    break
                else:
                    print(Fore.RED ,'please write number between 1 to 4!', Style.RESET_ALL)
                    continue
        save_attendance()        


def view_attendance_summary():
    with  open('records.json', 'r') as file:
        records = json.load(file)   
    present =0
    late = 0
    absent = 0
    exused = 0
    year = input('year:')
    month = input('month:')
    day = input('day:')
    selected_date = datetime(int(year), int(month), int(day))
    selected_date = selected_date.strftime('%Y-%m-%d')
    for record in records['records']:
        if record['date'] == selected_date:
            for student in record['attendance']:

                if student['attendance'] == 'present':
                    present +=1
                elif student['attendance'] == 'absent':
                    absent +=1
                elif student['attendance'] == 'late':
                    late +=1
                elif student['attendance'] == 'exused':
                    exused+=1
    print(Fore.RED ,'present:',present,'\tabsent:',absent,'\tlate:',late,'\taxused:',exused, Style.RESET_ALL)
    for student in record['attendance']:
        print('name:',student['name'],'\tattendance:', student['attendance'])
        print(Fore.YELLOW ,'*'*40, Style.RESET_ALL)






def save_notes():
    data = []
    today = datetime.now().strftime("%Y-%m-%d")
    for student in students:
        data.append({
            'name': student.name,
            'ID': student.student_id,
            'note': student.note            
        })

    data_save = {
        'date' : today,
        'notes': data
    }


    with  open('notes.json', 'r') as file:
        records = json.load(file)

        
    for record in records['records']:
        if record['date'] == today:
            record['notes'] = data
            break
    else:
        records['records'].append(data_save)  


    with open('notes.json', 'w') as file:
        json.dump(records, file, indent=4)



    
def add_notes():
    print(Fore.CYAN,'today:',datetime.now().strftime("%Y-%m-%d | %H:%M"), Style.RESET_ALL)
    while True:
        if len(students) == 0:
            print(Fore.RED,'you dont have any student!',Style.RESET_ALL)
            break
        else :
            student_name_id = input('enter your student id or name:')
            for student in students:
                if student_name_id==student.name or student_name_id== str(student.student_id) :
                    teacher_note = input('enter your note for:')
                    student.note  =  teacher_note
                    save_notes()
                    break
                
        break


def view_notes():
    with  open('notes.json', 'r') as file:
        records = json.load(file)



    year = input('year:')
    month = input('month:')
    day = input('day:')
    selected_date = datetime(int(year), int(month), int(day))
    selected_date = selected_date.strftime('%Y-%m-%d')
    for record in records['records']:
        if record['date'] == selected_date:
            for student in record['notes']:
                print('name:',student['name'],'\tnotes:', student['note'])
                print(Fore.YELLOW ,'*'*40, Style.RESET_ALL)








load_student()

