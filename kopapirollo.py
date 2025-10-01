valasz = input('Köszöntelek a "Kő, papír, olló" játékban. Szeretnél játszani? i/n : ')

import sys

import random

while True:
    if valasz == 'i':
        print('Örülök, hogy így döntöttél!')
        break

    elif valasz == 'n':
        print('Pápá!')
        sys.exit()

    else:
        valasz = input('Nem megfelelő válasz próbáld újra: ')

print('Szabályok!')
print('"Kő" üti az ollót, de veszít a papírral szemben. \n"Papír" üti a követ, de veszít az ollóval szemben. \n"Olló" üti a papírt, de veszít a kővel szemben.')

i = '1'
while i == '1':

    while True:
        try:
            valasztas = int(input('Kő, papír vagy olló (1 = Kő, 2 = Papír, 3 = Olló): '))
            if 1 <= valasztas <= 3:
                break
            else:
                print('Helytelen számot adtál meg. (1 = Kő, 2 = Papír, 3 = Olló) ')
        except ValueError:
            print('Nem megfelelő szám. (1 = Kő, 2 = Papír, 3 = Olló) ')

    gep_valasztasa = random.randint(1,3)

    fegyverek = {1: "Kő", 2: "Papír", 3: "Olló"}

    print(f'A te választásod: {fegyverek[valasztas]}')
    print(f'A gép választása: {fegyverek[gep_valasztasa]}')

    if (valasztas == 1 and gep_valasztasa == 3) or \
        (valasztas == 2 and gep_valasztasa == 1) or \
        (valasztas == 3 and gep_valasztasa == 2):
        print('Gratulálok, te győztél!')

    elif gep_valasztasa == valasztas:
        print('Döntetlen.')

    else:
        print('Vesztettél! HAHAHAHA')

i = input('Újra : 1 , Bezárás : 2 => ')

if i != '1':
    print('Viszlát!')
    break


