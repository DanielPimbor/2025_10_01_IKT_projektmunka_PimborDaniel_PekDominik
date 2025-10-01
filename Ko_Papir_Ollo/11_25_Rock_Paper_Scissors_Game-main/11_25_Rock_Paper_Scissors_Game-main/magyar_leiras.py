"""
Feladatleírás: Kő, Papír, Olló játék
Készíts egy Kő, Papír, Olló játékot, amelyet a felhasználó a számítógép ellen játszhat! A program működésének követelményei a következők:

Feladat követelményei:

1.Bevezető szöveg:
A program indításakor üdvözölje a játékost, például: "Üdvözölek a Kő, Papír, Olló játékban!".

2.Játékos választása:
A felhasználó adja meg a választását (pl. "kő", "papír", vagy "olló") szöveges formában.

3. Gép választása:
A program véletlenszerűen válasszon egyet a három lehetőség közül: "kő", "papír", vagy "olló".

4. Győztes meghatározása:
A program állapítsa meg, hogy a játékos nyert, vesztett, vagy döntetlen lett az eredmény:
"Kő" üti az ollót, de veszít a papírral szemben.
"Papír" üti a követ, de veszít az ollóval szemben.
"Olló" üti a papírt, de veszít a kővel szemben.

5. Eredmények összegzése:
A program folyamatosan vezesse, hány győzelme, veresége, és döntetlenje van a játékosnak:
Győzelem esetén növelje a "nyerések" számlálót.
Vereség esetén növelje a "vesztések" számlálót.
Döntetlen esetén növelje a "döntetlenek" számlálót.

6. Új játék lehetősége:
A kör végén kérdezze meg a program a felhasználót, hogy szeretne-e tovább játszani:
Ha a válasz "i", a játék folytatódjon.
Ha a válasz "n", a program fejezze be a futást.

7. Játék vége:
A program a kilépés előtt írja ki az összesített eredményeket (győzelmek, vereségek, döntetlenek).

Példafutás:
```python
Üdvözölek a Kő, Papír, Olló játékban!"
Válasz karaktert: Kő, Papír, Olló ->kő
gép választása:papír
vesztettél
nyerések:0, vesztések:1, döntetlenek:0
Akarsz még játszani? (i/n) i
```

Extra tippek fejlesztéshez:
Tedd a választásokat nem érzékennyé a kis- és nagybetűkre (pl. "kő" és "KŐ" egyaránt működjön).
Hozz létre egy hibakezelést, amely újra bekéri a választást, ha a felhasználó érvénytelen bemenetet adott meg.
Írj egy összefoglalót a játék végén, például: "Köszönjük a játékot! A végső eredmény: 3 győzelem, 2 vereség, 1 döntetlen."
Kihívás: Alakítsd át a játékot úgy, hogy a felhasználó egyszerre több körös versenyt is játszhasson, ahol pl. az első, aki 5 győzelmet ér el, az lesz a végső nyertes!
"""