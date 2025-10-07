import random
import sys

Nyert=0
Vesztett=0
Döntetlen=0
print("")
print("Üdv a Számháború játékban!")
print("")
print("---------------------------------------")
print("")


while True:
    while True:
        num = int(input("Adj meg egy egész számot 1 és 6 között "))
        print("")
        print("---------------------------------------")

        if 6 >= num >= 1:
            break

        else:
            print("")
            print("Csak 1 és 6 közötti számot adhatsz meg!")
            print("")
            print("---------------------------------------")

    num2 = random.randint(1,6)

    print(f'Gép: {num2}')
    print("")

    
    if num > num2:
        print("\033[32mNyertél!\033[0m")   
        Nyert+=1

    elif num < num2:
        print("\033[31mVesztettél!\033[0m")
        Vesztett+=1

    else:
        print("\033[33mDöntetlen!\033[0m")
        Döntetlen+=1
    print("---------------------------------------")
    print(f"\033[32mNyert {Nyert}\033[0m")
    print(f"\033[31mVesztett {Vesztett}\033[0m")
    print(f"\033[33mDöntetlen {Döntetlen}\033[0m")
    print("---------------------------------------")
    while True:
        print("")
        yn = input("Szeretnél újra játszani? (y/n) ")
        print("")
        print("---------------------------------------")
        if yn == "y":
            break
        elif yn == "n":
            break
        else:
            print("Próbáld újra")
    if yn =="n":
        break
print("Végeredmény:")
print(f"\033[32mNyert {Nyert}\033[0m")
print(f"\033[31mVesztett {Vesztett}\033[0m")
print(f"\033[33mDöntetlen {Döntetlen}\033[0m")
print("Köszönöm a játékot")
print("---------------------------------------")


"""
Forrás a színes szöveghez
https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
"""


