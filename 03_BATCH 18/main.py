from Decorator import decorate
from Date_Time import date
from Case_logics import stu_attandance, get_information, group_generateor, random_questions, personal_quiz
from Processing import delay_wait


def main():
    delay_wait.clear()

    while True:
        delay_wait.wait(0.3)
        decorate.equal50()
        print("INFOBEANS BATCH 18 MANAGER".center(50))    
        decorate.equal50()
        
        delay_wait.wait(0.1)
        decorate.space()
        print(f" Today is {date.today()} and only {date.days_left()} days are left.")
        decorate.space()
        print(" MENU")
        decorate.hyphen50()
        delay_wait.wait(0.1)
        print(" 1. Attendance")
        delay_wait.wait(0.1)
        print(" 2. Attendance Report")
        delay_wait.wait(0.1)
        print(" 3. Absent Students List")
        delay_wait.wait(0.1)
        print(" 4. Student Information")
        delay_wait.wait(0.1)
        print(" 5. Random Group Maker")
        delay_wait.wait(0.1)
        print(" 6. Random Quiz")
        delay_wait.wait(0.1)
        print(" 7. Student Quiz")
        delay_wait.wait(0.1)
        print(" 8. Exit")
        delay_wait.wait(0.1)
        decorate.hyphen50()
        decorate.space()
        delay_wait.wait(0.2)
        choice = input("Enter your choice: ")
        match choice:

            case "1":
                delay_wait.clear()
                if stu_attandance.attand_complete == "no":
                    stu_attandance.attandance()     
                    print("Attendance saved successfully.")
                    delay_wait.wait(2)
                    delay_wait.clear()
                else:
                    decorate.space()
                    decorate.hyphen50()
                    print("Attendance already completed. You cannot mark it again.")    
                    decorate.hyphen50()
                    decorate.space()
                    delay_wait.wait(2.5)
                    delay_wait.clear()  
            
            case "2":
                delay_wait.clear()
                decorate.space()
                if stu_attandance.attand_complete=="yes":
                    stu_attandance.attandance_report()
                else:
                    
                    decorate.hyphen50()
                    print("Please complete the attendance first.".center(50))    
                    decorate.hyphen50()
                    decorate.space()
                    delay_wait.wait(1.5)
                    delay_wait.clear()

            case "3":
                delay_wait.clear()
                if stu_attandance.attand_complete=="yes":
                    stu_attandance.absent_list()
                else:
                    decorate.space()
                    decorate.hyphen50()
                    print("Please complete the attendance first.".center(50))            
                    decorate.hyphen50()
                    decorate.space()
                    delay_wait.wait(1.5)
                    delay_wait.clear()
    
            case "4":
                delay_wait.clear()
                get_information.details()
                decorate.space()
                
            case "5":
                delay_wait.clear()
                if stu_attandance.attand_complete=="yes":
                    delay_wait.wait(0.2)
                    group_generateor.random_group()
                else:
                    decorate.space()
                    decorate.hyphen50()
                    print("Please complete the attendance first.".center(50))    
                    decorate.hyphen50()
                    delay_wait.wait(1.5)
                    delay_wait.clear()
                decorate.space()
                
                

            case "6":
                delay_wait.clear()
                if stu_attandance.attand_complete=="yes":
                    random_questions.random_quiz()
                else:
                    
                    decorate.space()
                    decorate.hyphen50()
                    print("Please complete the attendance first.".center(50))    
                    decorate.hyphen50()
                    delay_wait.wait(1.5)
                    delay_wait.clear()

            case "7":
                delay_wait.clear()
                delay_wait.wait(0.3)           
                personal_quiz.quiz()    
            
            case "8":
                delay_wait.clear()
                decorate.space()
                decorate.hyphen50()
                print(" Thank You for Using".center(50))
                print("INFOBEANS BATCH 18 MANAGER".center(50))
                decorate.hyphen50()
                break

            case _:

                delay_wait.clear()
                delay_wait.wait(0.2)
                decorate.space()
                decorate.hyphen50()
                print("Invalid choice. Please try again.".center(50))
                decorate.hyphen50()
                delay_wait.wait(2)
                delay_wait.clear()

main()
