questions=[["which language was used to create facebook?","Python","French","Javascript","Php","None",4]
["which language was used to create facebook?","Python","French","Javascript","Php","None",4]
["which language was used to create facebook?","Python","French","Javascript","Php","None",4]
["which language was used to create facebook?","Python","French","Javascript","Php","None",4]]
levels=[1000,2000,3000,5000,10000,24000,40000,55000,62000,160000]
money=0
for i in range(len(questions)):
    question=questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(f"a.{question[1]}      b.{question[2]}")
    print(f"c.{question[3]}      d.{question[4]}")
    reply=int(input("enter the answer (1-4): "))
    if(reply ==question[-1]):
        print(f"correct answer, you have won Rs.{levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=32000
        elif(i==14):
            money=100000
    else:
        print("wrong answer")
        break
print("your take home money is {money}")