name=input("Hii Please Enter Your Name: ")
print()
print(f"Welcome {name} to our Cafe ")
print()
bill=0
count=1
b=0
c1=0
c2=0
c3=0
c4=0
c5=0
ord=""
while count==1:
    while True:
        print("What do you want to eat")
        print()
        print("Our cafe special:")
        print("1. Burger    ₹100")
        print("2. Pizza     ₹200")
        print("3. Momos     ₹80")
        print("4. Sandwich  ₹70")
        print("5. Noodles   ₹120")
        print()
        choice=int(input("Order please = "))
        print()
        match choice:
            case 1:
                food="BURGER"
                price= 100
                quantity=int(input(f"Enter {food} quantity: "))
                c1+=quantity
                break
            case 2:
                food="PIZZA"
                price= 200
                quantity=int(input(f"Enter {food} quantity: "))
                c2+=quantity
                break
            case 3:
                food="MOMOS"
                price= 80
                quantity=int(input(f"Enter {food} quantity: "))
                c3+=quantity
                break
            case 4:
                food="SANDWICH"
                price= 70
                quantity=int(input(f"Enter {food} quantity: "))
                c4+=quantity
                break
            case 5:
                food="NOODLES"
                price= 120
                quantity=int(input(f"Enter {food} quantity: "))
                c5+=quantity
                break
            case _:
                print("\n please enter right order...\n")

    
    food_price=price*quantity
    print()
    bottle=input("Do you need water bottle(₹20) (yes/no): ").lower()
    if bottle=="yes":
        bquantity=int(input("Enter bottle quantity: "))
        bottle_price=20
        b+=bquantity
    else:
        bottle_price=0    
    bill=bill+bottle_price+food_price
    
    ord=ord+ food + str(quantity)+ "\n"
    print()   
    more=input("Do you want order more(yes/no): ").lower()
    if more=="yes":
        count=1
    else:
        count=0


print("-------------------------------------------------------")
print("Food       quantity    price    Amount")
print("-------------------------------------------------------")
if c1>0:
    print(f"Burger        {c1}      100       {c1*100}")
if c2>0:
    print(f"Pizza         {c2}      200       {c2*200}")
if c3>0: 
    print(f"Momos         {c3}      80        {c3*80}")
if c4>0:
    print(f"Sanwich       {c4}      70        {c4*70}")
if c5>0:
    print(f"Noodles       {c5}      120       {c5*120}")
if b>0:
    print(f"bottle        {b}      20        {b*20}")
print("--------------------------------------------------------")
    
print("                   Sub Total = ",bill)
gst=bill*5/100
print("                   GST(5%) = ",gst)
print("------------------------------------------------------")
total=bill+gst
print("                   GRAND TOTAL = ",total)
print("-------------------------------------------------------")

print(f"Thank you so much {name}! Hope to see you again at our cafe.")
