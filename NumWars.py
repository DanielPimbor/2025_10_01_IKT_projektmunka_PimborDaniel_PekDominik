import random
import sys
akar = True

print("Üdv a Számháború játékban!")

while akar == True:

    while True:
        num = int(input("Adj meg egy egész számot 1 és 6 között "))
        if 6>num>0:
            V1 = num
            break
        else:
            print("Csak 1 és 6 közötti számot adhatsz meg!")

    print(V1)
    V2 = random.randint(1,6)
    Nyert=0
    Vesztett=0
    Döntetlen=0
    if V1>V2:
        print("Nyertél")
        Nyert=+1
    elif V1<V2:
        print("Vesztettél")
        Vesztett=+1
    elif V1==V2:
        print("Döntetlen!")
        Döntetlen=+1

    print(f"Nyert {Nyert}")
    print(f"Vesztett {Vesztett}")
    print(f"Döntetlen {Döntetlen}")

    akar2 = input("Akrasz még játszani (y/n)")
if akar != "y":
    sys.exit()


