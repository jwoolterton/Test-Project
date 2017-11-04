import random
x=11
y="Jack"

print("my name is {0} i'm {1} years old".format(y,x))
turns=input("how many dice rolls?")
for n in range(1,int(turns)+1):
    i = random.randint(1,6)
    print(i)

    if i==6:
        print("you win!!!")
    elif i==1:
        print("you lose!!!")
    else:
        print("nothing happens!!!")

