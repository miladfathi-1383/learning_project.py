from colorama import Fore,Style,init
import students
import homework
init()



def main_menu():
    print('=' * 40)
    print(' '* 10,'TEACHER ASSISTANT')
    print('=' * 40) 
    print('1.Today Record\n2.View History\n3.Student\n4.homework\n5.exam\n6.Exit')


def today_record_menu():
    
    print(Fore.BLUE , '\nToday Reord', Style.RESET_ALL )
    print('1.attendance\n2.Notes\n3.Homework\\Exam\n4.View Today\'s Information\n5.Exit')


def attendance_menu():
    print(Fore.BLUE , '\nAttendance', Style.RESET_ALL )
    print('1.Take today\'s attendance\n2.Edit Today\'s attendance\n3.View Attendance summary\n4.Exit')



def note_menu():
    print(Fore.BLUE , '\nnotes', Style.RESET_ALL )
    print('1.add notes\n2.View notes\n3.delete notes\n4.Exit')



def student_menu():
    print(Fore.BLUE , '\nStudent', Style.RESET_ALL )
    print('1.add student\n2.View students\n3.Exit')


def homework_menu():
    print(Fore.BLUE , '\nHomework', Style.RESET_ALL )
    print('1.asign homework to one student\n2.assign homework to All student\n3.view homework\n4.edit homework\n4.delete homework\n5.Exit')




while True:
    main_menu()
    print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
    choice = input()
    if choice == '1': #today record
        while True:
            today_record_menu()
            print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
            choice = input()
            if choice == '1':
                while True:
                    attendance_menu()
                    print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
                    choice = input()  
                    if choice == '1':
                        students.student_attendance()
                    elif choice == '2':
                        pass
                    elif choice == '3':
                        students.view_attendance_summary()
                    elif choice == '4':
                        break
                    else:
                        print(Fore.RED ,'please write number between 1 to 4!', Style.RESET_ALL)

            elif choice == '2':
                while True:
                    note_menu()
                    print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
                    choice = input()
                    if choice == '1':
                        students.add_notes()
                    elif choice == '2':
                        students.view_notes()
                    elif choice == '3':
                        students.delete_notes()
                    elif choice == '4':
                        break
                    else:
                        print(Fore.RED ,'please write number between 1 to 4!', Style.RESET_ALL)
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                break
            else:
                print(Fore.RED ,'please write number between 1 to 5!', Style.RESET_ALL)
    elif choice == '2':#view history
        pass
    elif choice == '3':#student
        while True:
            student_menu()
            print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
            choice = input()          
            if choice == '1':
                students.add_student()
            elif choice == '2':
                students.show_student()     
            elif choice == '3':
                break
            else:
                print(Fore.RED ,'please write number between 1 to 3!', Style.RESET_ALL)

    elif choice == '4':#homework
        while True:
            homework_menu()
            print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
            choice = input() 
            if choice == '1':
                homework.add_homework()
            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                pass
            elif choice == '6':
                break
            else:
                print(Fore.RED ,'please write number between 1 to 6!', Style.RESET_ALL)

    elif choice == '5':#exam
        pass
    elif choice == '6':#exit
        break
    else:
        print(Fore.RED ,'please write number between 1 to 4!', Style.RESET_ALL)













