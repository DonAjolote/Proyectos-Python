import random

num = random.randint(1,15)
lim = 16

while True:
    b = int(input("Adivina el numero del 1 al 15: "))
    if b >= lim:
        print("Fuera de rango")
    elif b > num:
        print("Muy alto")
    elif b < num:
        print("Muy bajo")
    else:
        print("Acertaste\n")