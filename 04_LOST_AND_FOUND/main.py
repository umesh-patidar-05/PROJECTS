from service.student_service import StudentService
from service.lost_service import LostService


while True:
    print("""========================================
       LOST & FOUND MANAGEMENT SYSTEM
========================================""")
    print()
    print(" 1. Student Management")
    print(" 2. Lost Item Management")
    print(" 3. Found Item Management")
    print(" 4. Matching")
    print(" 5. Reports / Statistics")
    print(" 6. Exit")
    print()
    choice = int(input("Enter your choice: "))
    print()

    match choice:

        case 1:
            while True:
                print("1. View All Students")
                print("2. Search Student by ID")
                print("3. Add New Student")
                print("4. Home")
                print()
    
                search = int(input("Enter your choice: "))
                print()
                match search:
                    case 1:
                        print()
                        service = StudentService()
                        students = service.get_all_students()
                        print("="*93)
                        print("Student ID".center(15), "Student Name".center(20), "Mobile Number".center(20), "Department".center(30))
                        print("="*93)
                        for student in students:
                            print("|",str(student[0]).center(10),"|",student[1].center(20),"|",student[2].center(20),"|",student[3].center(30),"|")
                            print("-"*93)
                        print()
                        input("Press Enter to back...")
                        print()


    
                    case 2:
                        idd = int(input("Enter Student ID: ")) 
                        print()
                        service = StudentService()
                        student = service.get_student_by_id(idd)
                        if student is not None:
                            print("-"*40)
                            print("Studnt ID     : ",student[0])
                            print("-"*40)
                            print("Student Name  : ",student[1])
                            print("-"*40)
                            print("Mobile Number : ",student[2]) 
                            print("-"*40)
                            print("Department    :",student[3])  
                            print("-"*40)
    
                        else:
                            print("No student found with this id")     
                        print()
                        input("Press Enter to back...")
                        print()


                    case 3:
                        name = input("Enter new Student Name: ").strip() 
                        number = input("Enter Mobile number(10 digits): ").strip()
                        dept_name = input("Enter Department name: ").strip()
                        print()

                        service = StudentService()
                        student_id = service.new_student(name, number, dept_name)
                        print()
                        if student_id is not None:
                            print("Your Student Id is: ",student_id)
                        print()
                        input("Press Enter to back...")
                        print()    


                    case 4:
                        break

                    case _:
                        
                        print("invalid choice: ")
                        print()
                        input("Press Enter to back...")

        case 2:
            while True:
                print("1. See All Lost Items")
                print("2. Report Lost Item")
                print("3. View Lost Item Status")
                print("4. Home")
                print()

                search = int(input("Enter your choice: "))
                print()
                match search:

                    case 1:
                        print()
                        service = LostService()
                        lost_items = service.get_all_lost_items()
                        print("="*92)
                        print("ITEM".center(25), "DATE".center(25), "LOCATION".center(20), "STATUS".center(20))  
                        print("="*92)
                        for item in lost_items:
                            print("|",str(item[0]).center(25),"|" ,str(item[1]).center(20),"|", str(item[2]).center(20),"|", str(item[3]).center(15),"|")
                            print("-"*92)
                        print()
                        input("Press Enter to back...")




                
   


                
                 