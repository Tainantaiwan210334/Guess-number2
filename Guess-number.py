import random  

a=random.randint(1,10) 
print("Hi~Hi~ Guess the number?")

b=int(input('輸入1~10的數字:'))
for i in range(1,5):
    if b<a:
        b=int(input("數字太小，Try again!")) 
    elif b>a:
        b=int(input("數字太大，Try again!")) 
    else:
        print("right")
        break
if b!=a:
    print(f"stupid Ans:{a}")
