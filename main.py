import time
name=input("Enter your name : ")
recenttime=time.strftime("%H:%M:%S")
a=int(time.strftime("%H"))
b=name.capitalize()
if(4<=a<12) :
    print("Good morning",b,"it's",recenttime)
elif(12<=a<16):
    print("Good noon",b,"it's",recenttime)
elif(16<=a<18):
    print("Good afternoon",b,"it's",recenttime)
elif(18<=a<21):
    print("Good evening",b,"it's",recenttime)
else:
    if(21<=a<4):
        print("Good night",b,"it's",recenttime)
