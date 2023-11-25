import random

ch = "Y"

while ch == "Y" :
    ch = input("Enter Y to roll a dice and enter N to quit the program ")
    n = random.randint(1,6)
    if(n == 1) :
        print("[    ]\n[  0 ]\n[    ]")
    elif(n==2) :
        print("[0   ]\n[    ]\n[   0]")
    elif(n==3) :
        print("[0   ]\n[  0  ]\n[   0]")
    elif(n==4) :
        print("[0  0]\n[    ]\n[0  0]")
    elif(n==5) :
        print("[0  0]\n[  0  ]\n[0  0]")
    elif(n==6) :
        print("[0  0]\n[0  0]\n[0  0]")
