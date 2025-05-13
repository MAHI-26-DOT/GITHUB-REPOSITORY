import json

with open("file.py","r") as f:
    print(f.read())
while True: 
    print("*"*30)
    #greet 
    print("welcome to Italian de cafe")
    print("*"*30)
    print("1. SHOW MENU")
    print("2. ORDER ITEMS")
    print("3. UPDATE MENU")
    print("4. ADD REVIEW")
    print("5. EXIT")
    print("*"*30)
    choice=int(input())
    if choice==1:
        print('show menu')
    elif choice==2:
        print('order items')
    elif choice ==3:
        print('update menu')
    elif choice ==4:
        print("add review")
    else:
        print('exit')
        break
    
    