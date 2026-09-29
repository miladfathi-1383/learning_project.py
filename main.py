from colorama import Fore,Style,init
import students
init()



def main_menu():
    print('=' * 40)
    print(' '* 10,'TEACHER ASSISTANT')
    print('=' * 40) 
    print('1.Today Record\n2.View History\n3.Student\n4.Exit')


def today_record_menu():
    
    print(Fore.BLUE , '\nToday Reord', Style.RESET_ALL )
    print('1.attendance\n2.Notes\n3.Homework\\Exam\n4.View Today\'s Information\n5.Exit')


def attendance_menu():
    print(Fore.BLUE , '\nAttendance', Style.RESET_ALL )
    print('1.Take today\'s attendance\n2.Edit Today\'s attendance\n3.View Attendance summary\n4.Exit')


def student_menu():
    print(Fore.BLUE , '\nStudent', Style.RESET_ALL )
    print('1.add student\n2.View students\n3.Exit')


while True:
    main_menu()
    print(Fore.GREEN + '\tchoice: ' + Style.RESET_ALL, end='')
    choice = input()
    if choice == '1':
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
                        pass
                    elif choice == '2':
                        pass
                    elif choice == '3':
                        pass
                    elif choice == '4':
                        break
                    else:
                        print(Fore.RED ,'please write number between 1 to 4!', Style.RESET_ALL)

            elif choice == '2':
                pass
            elif choice == '3':
                pass
            elif choice == '4':
                pass
            elif choice == '5':
                break
            else:
                print(Fore.RED ,'please write number between 1 to 5!', Style.RESET_ALL)
    elif choice == '2':
        pass
    elif choice == '3':
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

    elif choice == '4':
        break
    else:
        print(Fore.RED ,'please write number between 1 to 4!', Style.RESET_ALL)
