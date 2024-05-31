from time import *;
import random as r;

def mistake(para,user):
    error =0
    for i in range(len(para)):
        try:
            if para[i] != user[i]:
                error = error +1
        except:
            error = error +1
    return error

def speed_type(tiems,timee,userinput):
    
    speed = timee - tiems
    roundspeed = round(speed,2)
    finalspeed = len(userinput)/roundspeed
    return round(finalspeed)




while True:
        s=input("Take the test yes/no :")
        if s=="yes":
            test=["""Video games are typically into a wide range of genres based on their style of gameplay and target audience.""",
                    "hello world",
                    "This is your first typing test"]
            testy=r.choice(test)
            print("                                            =====Typing Speed =====")
            print(testy)
            print()
            time_start =time()
            use = input("Enter here : ")
            time_end =time()


            print("Your Speed is :",speed_type(time_start,time_end,use)," w/sec")
            print("Error : ",mistake(testy,use))
        elif s=="no":
            print("Thank you")
            break
        else:
            print("invalid input")