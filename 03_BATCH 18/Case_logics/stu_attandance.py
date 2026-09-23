from Student_details import student_information
from Decorator import decorate
from Processing import delay_wait

present = []
absent = []
attand_complete = "no"


def attandance():
    global attand_complete
    decorate.space()
    delay_wait.wait(1)
    decorate.hyphen50()
    print(" Enter P for Present and A for Absent: ")
    decorate.hyphen50()
    decorate.space()
    for student in student_information.total_students:
        while True:
            status = input(f" {student.ljust(15)}: ").upper()
            if status == "P":
                present.append(student)
                break
            elif status == "A":
                absent.append(student)
                break
            else:
                print("Use only P (Present) or A (Absent).")
    attand_complete = "yes"           
    decorate.hyphen50() 
    decorate.space()



def attandance_report():
    decorate.equal25()
    print(" ATTENDANCE REPORT".center(25)) 
    decorate.equal25()
    delay_wait.wait(0.1)
    print(f"Present Students :  {len(present)}".center(25))
    delay_wait.wait(0.1)
    print(f"Absent Students  :  {len(absent)}".center(25))
    decorate.hyphen25()
    delay_wait.wait(0.1)
    print(f"Total Students   :  {len(present)+len(absent)}".center(25))
    decorate.hyphen25()
    decorate.space()
    home = input("Press Enter for Menu... ")
    delay_wait.wait(0.1)
    delay_wait.clear()

  


def absent_list():  
    decorate.space()
    decorate.equal25()
    print("ABSENT STUDENT LIST".center(25))
    decorate.equal25()      
    if len(absent) == 0:
        print("Great! No students are absent today.")
    else:
        for i in range(len(absent)):
            print(f"{i+1}. {absent[i]}")
    decorate.hyphen25()
    decorate.space()
    home = input("Press Enter for Menu... ")
    delay_wait.wait(0.5)
    delay_wait.clear()