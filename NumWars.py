import random
import sys

print("Üdv a Számháború játékban!")



while True:
    num = int(input("Adj meg egy egész számot 1 és 6 között "))

    if 6 >= num >= 1:
        break

    else:
        print("Csak 1 és 6 közötti számot adhatsz meg!")

print(f'{num}')
num2 = random.randint(1,6)

Nyert=0
Vesztett=0
Döntetlen=0

if num > num2:
    print("Nyertél")
    Nyert=+1

elif num < num2:
    print("Vesztettél")
    Vesztett=+1

else:
    print("Döntetlen!")
    Döntetlen=+1

print(f"Nyert {Nyert}")
print(f"Vesztett {Vesztett}")
print(f"Döntetlen {Döntetlen}")




