print()
print("A student was absent yesterday, and today Batch Mentor is asking the reason before allowing him into the class.")
print()


name=input("Enter your name: ").upper()


print()
print(f"{name}, why were you absent yesterday?")
print()

print("1. College Work")
print("2. Health Issue")
print("3. Family Function")
print("4. Emmergency")
print("5. Weak reason")
print()


choice=int(input("Reason: "))
print()
match choice:
    case 1:
        mail=input(f",{name}, Did you send an email? -> ").lower()
        print()
        if mail=="yes":
            assignment=input(f"{name}, Have you completed all previous assignments and updated your notes? ").lower()
            print()
            if assignment=="yes":
                print("Okay {name}, you can sit in the classroom.")
            else:    
                print("Please be serious and update your notes and complete assignments today. I’ll allow you this time, but next time you’ll be in trouble.")
            print()    
        else:  
            print("Why didn't you email me? You already knew when you had to go to college")
            print()
            valid=input(f"{name}, Do you have a valid document that shows you actually went to college? ").lower()
            print()
            if valid=="yes":
                print(f",{name}, I’ll allow you this time, but next time you have to email me. Otherwise, you’ll be in trouble.")
            else:
                print(f"{name}, You don’t have a valid document, so you’ll have to stand outside the classroom until lunchtime.")
            
    case 2:
        mail=input("Did you send an email? -> ").lower()
        print()
        if mail=="yes":
            mention=input("Did you mention the doctor's prescription in the email as well?")
            print()
            if mention=="yes":
                assignment=input(f"{name}, Have you completed all previous assignments and updated your notes? ").lower()
                print()
                if assignment=="yes":
                    print(f"Okay {name}, you can sit in the classroom.")
                else:   
                    print("I’ll allow you this time. but I need all the assignments and notes completed till today.")
            else:
                now=input(f"{name}, Do you have the doctor's prescription now? ").lower()
                print()
                if now=="yes":
                    assignment=input("Have you completed all previous assignments and updated your notes? ").lower()
                    if assignment=="yes":
                        print(f"Okay {name}, you can sit in the classroom.")
                    else:
                        print("I’ll allow you this time. but I need all the assignments and notes completed till today.")
                else:
                    print(f"{name}, If you don’t have the prescription, how can I believe that you were really unwell?")
                    print()
                    assignment=input(f"{name}, Have you completed all previous assignments and updated your notes? ").lower()
                    print()
                    if assignment=="yes":
                        print(f"I’ll allow you this time, but next time {name}, you have to bring the doctor's prescription.")
                    else:
                        print(f"{name}, You don't have the prescription and you did not complete the assignments and notes, so you have to stand in today's full lecture.")
                     
               
        else:
            now=input(f"{name}, Do you have the doctor's prescription now? ").lower()
            print()
            if now=="yes":
                assignment=input(f"{name}, Have you completed all previous assignments and updated your notes? ").lower()
                print()
                if assignment=="yes":
                    print(f"Okay {name}, you can sit in the classroom.")
                else:
                    print(f"{name}, I need all the assignments and notes completed till today, and you will have to stand in class today for half an hour.")
            else:
                assignment=input("Have you completed all previous assignments and updated your notes? ").lower()
                print()
                if assignment=="yes":
                    print(f"{name}, You have to stand on the chair for 30 minutes in today's lecture..")
                else:
                    print(f"{name}, You didn't email me, you don't have the prescription, and you did not complete the assignments and notes, so you are not allowed to attend today's lecture")

            
    case 3:
        mail=input("Did you send an email? -> ").lower()
        print()
        if mail=="yes":
            imp=input("Was the family function important?")
            print()
            if imp=="yes":
                assignment=input("Have you completed all previous assignments and updated your notes? ").lower()
                print()
                if assignment=="yes":
                    print(f"Okay {name}, you can sit in the classroom.")
                else:    
                    print("I’ll allow you this time. but I need all the assignments and notes completed till today.")
            else:
                assignment=input("Have you completed all previous assignments and updated your notes? ").lower()
                print()
                if assignment=="yes":
                    print(f"{name} This time I'll allow you, but please avoid unnecessary functions.")
                else:    
                    print(f"{name}, Your function wasn't important either, and you didn't do the work too. How will this work? You will have to stand in your place for 1 hour in today's lecture")
        else:
            print()
            imp=input("Was the family function important?")
            if imp=="yes":
                assignment=input("Have you completed all previous assignments and updated your notes? ").lower()
                print()
                if assignment=="yes":
                    print("This time I'll allow you, but next time you have to email me, otherwise you'll be in trouble.")
                else:  
                    print(f"{name}, You didn't send the email either, and you didn't do the work too. How will this work? You have to stand for 1.5 hours in today's lecture.")
            else:
                print(f"{name}, You didn't send the email either. Your function wasn't important, and you didn't do the work too. How will this work? You don't have permission to attend today's lecture.")
        
    case 4:
        print(f"{name}, is Everything  fine now. Update all the notes and complete the assignment too, okay . you can seat ")
    case 5:
        mail=input("Did you send an email? -> ").lower()
        print()
        if mail=="yes":
            assignment=input("Have you completed all previous assignments and updated your notes? ").lower()
            print()
            if assignment=="yes":
                print(f"{name}, Your reason is not valid, so you will have to stand for 1 hour in today's lecture")
            else:    
                print(f"{name}, You didn't complete the assignment and your reason isn't valid either, so you will have to stand on a chair for 1 hour in today's lecture.")
        else:
            print(f"{name}, You didn't send the email and your reason isn't valid either, so you will have to stand outside the class for the whole day.")
        
    case _:
        mail=input("Did you sent an email? -> ").lower()
        print()
        if mail=="yes":
            print(f"{name}, Your reason is not valid. You are not allowed to enter the class today. Stand outside the class for the whole day.")
        else:
            print(f"{name}, you are not allowed to attend class for next 2 days")