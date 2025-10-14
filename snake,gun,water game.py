import random

computer = random.choice([1,2,3])
youdict = input("enter the chose (snake,water,gun):")
youstr = {"water":1,"gun":2,"snake":3}
you = youstr[youdict]
reversedict = {1:"water",2:"gun",3:"snake"}

print(f'you choose: {reversedict[you]} \ncomputer choose: {reversedict[computer]}')


if(computer == you):
    print("it's a draw")

else:
    if(computer ==1 and you== 2):
        print("you loss")
    elif(computer == 1 and you == 3):
     print("you won")
    elif(computer == 2 and you == 1):
       print("you loss")
    elif(computer == 2 and you == 3):
       print("you loss")
    elif(computer == 3 and you == 1):
       print("you loss")
    elif(computer == 3 and you == 2):
       print("you won")
    else:
       print("pls enter valid name in the sentence")