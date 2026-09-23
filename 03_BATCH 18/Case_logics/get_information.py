from Student_details import student_information
from Decorator import decorate
from Processing import delay_wait

def details():
    decorate.space()
    stu_name = input("Enter the student name: ").title()
    decorate.space()
    if stu_name in student_information.students_details:
        decorate.equal25()
        print("STUDENT DETAILS".center(25))
        decorate.equal25()
        print(f"  {"Name".ljust(7)}   : {stu_name}")
        decorate.hyphen25()
        for k,v in student_information.students_details[stu_name].items():
            print(f"  {k.capitalize().ljust(7)}   : {v}")
        decorate.hyphen25()
        
    else:
        decorate.hyphen50()
        print(f"No student found with the name {stu_name}.")
        decorate.hyphen50()   

    more_find() 


def more_find():
    decorate.space()
    more = input("Do you want to view another student's details? (Y/N): ").upper()
    decorate.space()
    delay_wait.clear()
    delay_wait.wait(0.2)
    if more == "Y":
        details()
