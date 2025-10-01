valasz = input('Köszöntelek a "Kő, papír, olló" játékban. Szeretnél játszani? i/n : ')

while True:
    if valasz == 'i':
        print('Örülök, hogy így döntöttél!')
        break

    elif valasz == 'n':
        print('Pápá!')
        break

    else:
        valasz = input('Nem megfelelő válasz próbáld újra: ')
