valasz = input('Köszöntelek a "Kő, papír, olló" játékban. Szeretnél játszani? i/n : ')

import sys

while True:
    if valasz == 'i':
        print('Örülök, hogy így döntöttél!')
        break

    elif valasz == 'n':
        print('Pápá!')
        sys.exit()

    else:
        valasz = input('Nem megfelelő válasz próbáld újra: ')
