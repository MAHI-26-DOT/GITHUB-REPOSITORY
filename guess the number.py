import random

target=random.randint(1,100)
while True:
    userchoice=input("guess the target: OR Quit: ")
    if(userchoice=="Quit"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("success: correct guess!")
        break
    elif(userchoice<target):
        print("your number was too small. Take a bigger guess...")
    else:
        print("your number was too big. Take a smaller guess...")
print("---GAME OVER----")