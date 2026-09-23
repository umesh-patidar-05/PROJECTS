import random
from Case_logics.stu_attandance import present
from Decorator import decorate
from Processing import delay_wait

  
def random_group():
    
    while True:
        decorate.space()
        n = input("Enter the number of groups: ")
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
    decorate.space()
    
    if n>0 and n<=len(present):
        group = []
        member = len(present)//n
        remainder = len(present)%n
        random_list = present.copy()
        random.shuffle(random_list)
        start = 0
        for i in range(n):
            size = member
            
            if remainder > 0:
                size +=1
                remainder -= 1
            group.append(random_list[start: start+size])
            start += size

        delay_wait.clear()
        decorate.space()
        print("Generating random groups...")
        delay_wait.wait(1.5)
        
        display_group(group)    
    else:
        delay_wait.clear()
        decorate.space()
        delay_wait.wait(0.3)
        print("Please enter a valid number. ")   
        delay_wait.wait(2)
        delay_wait.clear()


def display_group(g):
    delay_wait.clear()
    decorate.space()
    decorate.equal25()
    print("RANDOM GROUPS".center(25))
    decorate.equal25()
    decorate.space()
    for i,s in enumerate(g):
        delay_wait.wait(0.3)
        decorate.hyphen25() 
        print(f" Group {i+1}")
        decorate.hyphen25() 
        for i in range(len(s)):
            print(f" {i+1}. {s[i]}")
        decorate.space()
        decorate.space()
    
    home = input("Press Enter for Menu... ")
    delay_wait.wait(0.5)
    delay_wait.clear()

