import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("guess the number b/w(1,100):"))
    if a>n:
        print("lower  number please")
    elif a<n:
        print("higher number please")
    else:
        print("invalid input, try again")


print(f'you have guessed the number {n} at guesses of {guesses}')