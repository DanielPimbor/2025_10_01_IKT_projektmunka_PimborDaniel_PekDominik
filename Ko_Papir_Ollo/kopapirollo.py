import sys
import random

valasz = input('Köszöntelek a "Kő, papír, olló" játékban. Szeretnél játszani? i/n : ')

pontszamod = 0
gep_pontszama = 0

gyozelmek = 0
veresegek = 0
dontetlenek = 0

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
print('Kő üti az ollót, de veszít a papírral szemben.')
print('Papír üti a követ, de veszít az ollóval szemben.')
print('Olló üti a papírt, de veszít a kővel szemben.')

while True:

    while True:
        try:
            valasztas = int(input('Kő, papír vagy olló (1 = Kő, 2 = Papír, 3 = Olló): '))

            if 1 <= valasztas <= 3:
                break

            else:
                print('Helytelen számot adtál meg. (1 = Kő, 2 = Papír, 3 = Olló)')

        except ValueError:
            print('Nem megfelelő szám. (1 = Kő, 2 = Papír, 3 = Olló)')

    gep_valasztasa = random.randint(1, 3)
    fegyverek = {1: "Kő", 2: "Papír", 3: "Olló"}

    print(f'A te választásod: {fegyverek[valasztas]}')
    print(f'A gép választása: {fegyverek[gep_valasztasa]}')

    if (valasztas == 1 and gep_valasztasa == 3) or \
       (valasztas == 2 and gep_valasztasa == 1) or \
       (valasztas == 3 and gep_valasztasa == 2):
        
        print('Gratulálok, te győztél!')

        pontszamod += 1
        gyozelmek += 1

    elif gep_valasztasa == valasztas:
        print('Döntetlen.')

        dontetlenek += 1

    else:
        print('Vesztettél! HAHAHAHA')

        gep_pontszama += 1
        veresegek += 1

    print(f'Pontszámod: {pontszamod}')
    print(f'Gép pontszáma: {gep_pontszama}')

    i = input('Újra játszol? i/n: ')
    
    if i.lower() != 'i':
        print('Végső pontszámok és statisztikák:')

        print(f'Pontszámod: {pontszamod}')
        print(f'Gép pontszáma: {gep_pontszama}')
        print(f'Győzelmek száma: {gyozelmek}')
        print(f'Vereségek száma: {veresegek}')
        print(f'Döntetlenek száma: {dontetlenek}')

        if pontszamod > gep_pontszama:
            print('Megnyerted az egész játékot!')

        elif pontszamod == gep_pontszama:
            print('Döntetlen lett az összmenet.')

        else:
            print('VESZTETTEL HAHAHAHA')

        print('Viszlát!')
        break