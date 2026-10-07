from students import students
from datetime import datetime
from colorama import Fore, Style, init
import json
init()


def add_homework():
    print(Fore.CYAN,'today:',datetime.now().strftime("%Y-%m-%d | %H:%M"),Style.RESET_ALL)
    while True:
        if len(students) == 0:
            print(Fore.RED,'you dont have any student!',Style.RESET_ALL)
            break
        else:
            student_name_id = input('student name or id:')
            for student in students:
                if (student_name_id == student.name or student_name_id == str(student.student_id)):
                    homework = input('enter your homework for:')
                    student.homework = homework
                    save_homework()
                    break
            else:
                print(Fore.RED,'student not found!',Style.RESET_ALL)
            break


def save_homework():
    data = []
    today = datetime.now().strftime("%Y-%m-%d")
    for student in students:
        data.append({
            'name': student.name,
            'ID': student.student_id,
            'homework': student.homework            
        })

    data_save = {
        'date' : today,
        'homework': data
    }


    with  open('homework.json', 'r') as file:
        records = json.load(file)

        
    for record in records['records']:
        if record['date'] == today:
            record['notes'] = data
            break
    else:
        records['records'].append(data_save)  


    with open('homework.json', 'w') as file:
        json.dump(records, file, indent=4)