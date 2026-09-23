import random

from Decorator import decorate
from Case_logics import stu_attandance
from Questions import questions_250
from Processing import delay_wait


def random_quiz():

    random_student = stu_attandance.present.copy()
    random_question = questions_250.questions.copy()

    random.shuffle(random_student)
    random.shuffle(random_question)

    correct = []
    wrong = []

    for i in range(len(random_student)):
        decorate.space()
        print(f"Question {i+1}")
        delay_wait.wait(1.5)
        print("              for ",random_student[i].upper())
        delay_wait.wait(1.5)
        
        decorate.hyphen50()
        print(" ",random_question[i]["question"])
        decorate.space()
        print(" A).",random_question[i]["A"])
        print(" B).",random_question[i]["B"])
        print(" C).",random_question[i]["C"])
        print(" D).",random_question[i]["D"])
        decorate.hyphen50()
        while True:
            mark = input("Enter your option: ").upper()
            decorate.space()
            if mark in "ABCD":
                delay_wait.wait(1)
                if random_question[i][mark] == random_question[i]["answer"]:
                    print("Status : Correct")
                    correct.append(random_student[i])
                    break
                else:
                    print("Status : Wrong")
                    wrong.append(random_student[i])
                    decorate.space()
                    delay_wait.wait(0.5)
                    print("correct answer is: ",random_question[i]["answer"])
                    break
                
            else:
                print("Choose correct option(A/B/C/D): ")        
                continue

        decorate.space()
        if i<len(random_student)-1:
            more = input("do you want to conitnue(Y/N): ").upper()
            delay_wait.clear()

            if more == "Y":
                continue
            else:
                break
    delay_wait.wait(2)
    delay_wait.clear()
    result_random(correct,wrong)

def result_random(corr,wro):
    decorate.space()    
    delay_wait.wait(0.3)
    decorate.equal25()
    print("RANDOM QUIZ RESULT".center(25))
    decorate.equal25()

    decorate.space()
    print("Correct Answers :",len(corr))
    delay_wait.wait(0.2)
    decorate.hyphen25()
    for i in range(len(corr)):
        print(f"{i+1}. {corr[i]}")

    delay_wait.wait(0.2)
    decorate.space()
    print("Wrong Answers :",len(wro))
    decorate.hyphen25()
    delay_wait.wait(0.2)
    for i in range(len(wro)):
        print(f"{i+1}. {wro[i]}")
    decorate.space()
    delay_wait.wait(0.3)
    home = input("Press Enter for Menu... ")
    delay_wait.wait(0.5)
    delay_wait.clear()