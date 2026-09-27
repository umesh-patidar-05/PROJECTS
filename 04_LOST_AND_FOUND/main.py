from service.student_service import StudentService
from service.lost_service import LostService
from service.found_service import FoundService
from service.matching_service import MatchingService
from service.reports_service import ReportsService
from operate import clear_terminal as t

while True:
    t.clear()
    print()
    print("""========================================
       LOST & FOUND MANAGEMENT SYSTEM
========================================""")
    print()
    print(" 1. Student Management")
    print(" 2. Lost Item Management")
    print(" 3. Found Item Management")
    print(" 4. Matching")
    print(" 5. Reports")
    print(" 6. Exit")
    print()
    choice = int(input("Enter your choice: "))
    t.clear()
    print()

    match choice:

        case 1:
            while True:
                print("Student Management")
                print()
                print("1. View All Students")
                print("2. Search Student by ID")
                print("3. Enroll New Student")
                print("4. Home")
                print()
    
                search = int(input("Enter your choice: "))
                t.clear()
                print()
                match search:
                    case 1:
                        print("ALL STUDENTS ARE:")
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
                        t.clear()


    
                    case 2:
                        print("Search Student by ID")
                        print()
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
                        t.clear()
                        print()


                    case 3:
                        print("Enroll New Student")
                        print()
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
                        t.clear()
                        print()    


                    case 4:
                        break

                    case _:
                        
                        print("invalid choice: ")
                        print()
                        input("Press Enter to back...")
                        t.clear()
        case 2:
            while True:
                print()
                print("Lost Item Management:")
                print()
                print("1. See All Lost Items")
                print("2. Report Lost Item")
                print("3. View Lost Item Status")
                print("4. Home")
                print()

                search = int(input("Enter your choice: "))
                t.clear()
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
                        t.clear()

                    case 2:
                        print()
                        stu_id = int(input("Enter your student ID: "))
                        print()
                        item_name = input("Enter lost Item name: ").strip()
                        date = input("Enter lost date(yyyy-mm-dd): ").strip()
                        address = input("Enter address: ").strip()
                        
                        lost_service = LostService()
                        stu_service = StudentService()
                        student = stu_service.get_student_by_id(stu_id)
                        print()
                        
                        if student is not None:
                            if date[4] == '-' and date[7] =='-':
                                lost = lost_service.new_lost_report(stu_id, item_name, date, address)
                                print(lost)
                                
                            else:
                                print("incorrect date...")    

                        else:
                            print("No student available with this id. plz enroll first") 
                        print()    
                        input("Press Enter to back...")
                        t.clear()

                    case 3:
                        print()
                        stu_id = int(input("Enter your Student ID: "))
                        print()
                        lost_service = LostService()
                        stu_service = StudentService()
                        student = stu_service.get_student_by_id(stu_id)
                        if student is not None:
                                                
                            lost_items = lost_service.lost_item_status(stu_id)
                            if lost_items is None:
                                print("no lost items: ")

                            else:
                                print("Your Lost Items: ")
                                for n, item in enumerate(lost_items):
                                    print(f"{n+1}. {item[0]}")
                                print()    
                                try:
                                    select = int(input("Select item: "))
                                    print()
                                    1 <= select <= len(lost_items)
                                    print("-"*30)
                                    print("Item: ", lost_items[select-1][0])
                                    print("-"*30)
                                    print("Lost Date: ",lost_items[select-1][1])
                                    print("-"*30)
                                    print("Location: ",lost_items[select-1][2])
                                    print("-"*30)
                                    print("Status: ",lost_items[select-1][3])
                                    print("-"*30)
                                except Exception as e:
                                    print("plz select correct item")        

                        else:
                            print("No student available with this id. plz enroll first") 
                        print()    
                        input("Press Enter to back...")
                        t.clear()
                        print()

                    case 4:
                        break

                    case _:
                        print("invalid choice: ")
                        print()
                        input("Press Enter to back...") 
                        t.clear()
                        

        case 3:
            while True:
                print()
                print("Found Item Management:")
                print()
                print("1. See All Found Items")
                print("2. Report Found Item")
                print("3. View Found Item Status")
                print("4. Home")
                print()
                search = int(input("Enter your choice: "))
                t.clear()
                print()
                match search:

                    case 1:
                        print()
                        service = FoundService()
                        found_items = service.get_all_found_items()
                        print("="*92)
                        print("ITEM".center(25), "DATE".center(25), "LOCATION".center(20), "STATUS".center(20))  
                        print("="*92)
                        for item in found_items:
                            print("|",str(item[0]).center(25),"|" ,str(item[1]).center(20),"|", str(item[2]).center(20),"|", str(item[3]).center(15),"|")
                            print("-"*92)
                        print()
                        input("Press Enter to back...")
                        t.clear()

                    case 2:
                        print()
                        stu_id = int(input("Enter your student ID: "))
                        print()
                        item_name = input("Enter found Item name: ").strip()
                        date = input("Enter found date(yyyy-mm-dd): ").strip()
                        address = input("Enter address: ").strip()
                        
                        found_service = FoundService()
                        stu_service = StudentService()
                        student = stu_service.get_student_by_id(stu_id)
                        print()
                        
                        if student is not None:
                            if date[4] == '-' and date[7] =='-':
                                found = found_service.new_found_report(stu_id, item_name, date, address)
                                print(found)
                                
                            else:
                                print("incorrect date...")    

                        else:
                            print("No student available with this id. plz enroll first") 
                        print()    
                        input("Press Enter to back...")                            
                        t.clear()
                        
                                                
                    case 3:
                        print()
                        stu_id = int(input("Enter your Student ID: "))
                        print()
                        found_service = FoundService()
                        stu_service = StudentService()
                        student = stu_service.get_student_by_id(stu_id)
                        if student is not None:
                                                
                            found_items = found_service.lost_item_status(stu_id)
                            if found_items is None:
                                print("no found items: ")

                            else:
                                print("Found Items are: ")
                                print()
                                for n, item in enumerate(found_items):
                                    print(f"{n+1}. {item[0]}")
                                print()    
                                try:
                                    select = int(input("Select item: "))
                                    print()
                                    1 <= select <= len(found_items)
                                    print("-"*30)
                                    print("Item: ", found_items[select-1][0])
                                    print("-"*30)
                                    print("Lost Date: ",found_items[select-1][1])
                                    print("-"*30)
                                    print("Location: ",found_items[select-1][2])
                                    print("-"*30)
                                    print("Status: ",found_items[select-1][3])
                                    print("-"*30)
                                except Exception as e:
                                    print("plz select valid item")        

                        else:
                            print("No student available with this id. plz enroll first") 
                        print()    
                        input("Press Enter to back...")
                        t.clear()
                        print()

                    case 4:
                        break

                    case _:
                        
                        print("invalid choice: ")
                        print()
                        input("Press Enter to back...")
                        t.clear()

                    
        case 4:
            while True:
                print()
                print("Matching: ")
                print()
                print("1. Find & Confirm Match")
                print("2. Claim Matched Item")
                print("3. Home") 
                print()
                search = int(input("Enter your choice: "))
                t.clear()
                print()
                match search:

                    case 1:
                        item_name = input("Enter lost item name: ").strip()
                        address = input("Enter address: ").strip()
                        date = input("Enter lost date(yyyy-mm-dd): ").strip()

                        match_service = MatchingService()                        
                        lost_service = LostService()
                        
                        print()
                        
                        if date[4] == '-' and date[7] =='-':
                            confirm = match_service.confirm_lost_item(item_name, address, date)
                            if confirm is not None:
                                if confirm[5] == 2:
                                    print("Lost item already found")

                                elif confirm[5] == 3:
                                    print("Lost item already claimed")

                                else:        

                                    match_items = match_service.matching_found_items(item_name, address)
            
                                    if match_items is None:
                                        print("No possible match found.")
            
                                    else:
                                        print("Possible Match Found")
                                        for n, item in enumerate(match_items):
                                            print()
                                            print("Found: ",n+1)
                                            print("Item Name: ", item[0]) 
                                            print("Found Date: ", item[1])
                                            print("Location: ", item[2])
                                            print("Found BY: ", item[3])
                                            print("Mobile no: ", item[4])
                                        print()
                                     
                                        while True:
                                            match = int(input("Select match: "))
                                            if 1 <= match <= len(match_items):
                                                print()
                                                final = input("Are you sure this is your item? (Y/N)").lower()
                                                if final == 'y':
                                                    print()
                                                    change = match_service.lost_table_status_change( 2,confirm[0])
                                                    print(change)
    
                                                break
                                            else:
                                                print("incorrect match")
                                                print()


                            else:
                                print("Please report your lost item first")

                            
                        else:
                            print("incorrect date...")    

                        print()
                        input("Press Enter to back...")
                        t.clear()

                    case 2:
                        stu_id = int(input("Enter your student ID: "))
                        stu_service = StudentService()
                        student = stu_service.get_student_by_id(stu_id)
                        if student is not None:
                                                
                            match_service = MatchingService()
                            items = match_service.confirm_student_in_lost(stu_id)
                            if items is not None:
                                
                                res = []
                                for n, item in enumerate(items):

                                    found = match_service.matching_found_items(item[2], item[4])
                                    if found is not None:
                                        l = [item[0], found[0][5]]
                                        res.append(l)
                                        print()
                                        print("Found: ",len(res))
                                        print("Item Name: ", item[2]) 
                                        print()

                                
                                
                                if res != []:
                                    while True:
                                        match = int(input("Select match: "))
                                        if 1 <= match <= len(res):
                                            print()
                                            final = input("claim confirmation (Y/N)").lower()
                                            if final == 'y':
                                                print()
                                                change_lost = match_service.lost_table_status_change(3, res[match-1][0])
                                                change_found = match_service.found_table_status_change(3, res[match-1][1])


                                                print("Item claimed successfully ")
                                            break
                                        else:
                                            print("incorrect match")
                                            print()             
                                else:
                                    print("You have no matched items to claim.")                              
                                
                            else:
                                print("You have no matched items to claim.")

                        else:
                            print("No student available with this id. plz enroll first") 
                        print()
                        input("Press Enter to back...")
                        t.clear()



                    case 3:
                        break       

                    case _:
                        print("invalid choice: ")
                        print()
                        input("Press Enter to back...") 
                        t.clear()

        case 5:
            print()
            print("REPORTS: ")
            print()
            report = ReportsService()
            print("Total Lost Items    : ", report.all_lost_itmes())
            print("-"*27)
            print("Total Claimed Items : ", report.all_claimed_items())
            print("-"*27)
            print("Pending Lost Items  : ", report.all_pending_items())
            print("-"*27)
            print("Total Found Items   : ", report.all_found_items())
            print("-"*27)
            print()
            input("Press Enter to back...") 
            t.clear()


        case 6:
            print("THANKS FOR USING LOST AND FOUND MANAGEMENT SYSTEM")
            break

        case _:
            print("invalid choice....plz enter correct choice.....")
            print()
            input("Press Enter to back...") 
            t.clear()



            






                
                      


   


                
   


                
                 