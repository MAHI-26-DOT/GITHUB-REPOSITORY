import time

timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hour=time.strftime('%H')
print(hour)
if(int(hour)<12):
    print("good morning")
elif(int(hour)<16):
    print("good afternoon")
elif(int(hour)<20):
    print("good evening")
else:
    print("good night")