import random

from Questions import questions_250
from Student_details import student_information
from Decorator import decorate
from Processing import delay_wait

def quiz():
    marks = []
    status = []
    ques = questions_250.questions.copy()
    random.shuffle(ques)
    decorate.space()
    stu_name = input("Enter the student name: ").title()
    decorate.space()
    if stu_name in student_information.students_details:
        while True:
            n = input("Enter the number of questions : ")
            decorate.space()
            try:
                n = int(n)
                break
            except:
                delay_wait.clear()
                decorate.space()
                print("Please enter a valid number. ")   
                delay_wait.wait(2)
                delay_wait.clear()
        if n>0:
            for i in range(n):
                decorate.hyphen50()
                print(f"Q{i+1}",ques[i]["question"])
                decorate.space()
                print(" A).",ques[i]["A"])
                print(" B).",ques[i]["B"])
                print(" C).",ques[i]["C"])
                print(" D).",ques[i]["D"])
                decorate.hyphen50()
                
                while True:
                    mark = input("Enter your option: ").upper()
                    decorate.space()
                    decorate.space()
                    if mark in "ABCD":
                        if ques[i][mark] ==ques[i]["answer"]:
                        
                            status.append("Correct")
                            marks.append(1)
                            break
                        else:
                            status.append("Wrong")
                            marks.append(0)
                            break
                    else:
                        print("Choose correct option(A/B/C/D): ")        
                        continue
            delay_wait.wait(1.5)
            delay_wait.clear()        
            result(stu_name ,marks, status)

        else:
            delay_wait.clear()
            decorate.space()
            delay_wait.wait(0.3)
            print("Please enter a valid number. ")   
            delay_wait.wait(2)
            delay_wait.clear()        
        
    else:
        decorate.hyphen50()
        print(f"No student found with the name {stu_name}.")
        decorate.hyphen50()   
    more_find()



def more_find():
    decorate.space()
    more = input("Another student test ? (Y/N): ").upper()
    decorate.space()
    delay_wait.clear()
    delay_wait.wait(0.2)
    if more == "Y":
        quiz()



def result(nam,mar, sta):
    decorate.equal50()
    print("QUIZ RESULT".center(50))        
    decorate.equal50()
    print(f" Name : {nam}")
    decorate.hyphen50()
    print(f" {"Question":<10} {"Status":<10} {"Marks":<10}")    
    decorate.hyphen50()
    for i in range(len(mar)):
        print(f" {i+1:<10} {sta[i]:<10} {mar[i]:<10}") 
    decorate.hyphen50()
    print(f"   Total Marks   : {sum(mar)} / {len(mar)}")   
    decorate.hyphen50()