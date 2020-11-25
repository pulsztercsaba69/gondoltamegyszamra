#1.feladat
gondolt_szám = 4
tipp = input('Szerinted melyik számra gondolok 1 és 5 között? ')
tipp = int(tipp)
if gondolt_szám == tipp:
    print('Eltaláltad!')
    print('Kis ügyes!')
else:
    print('Ez most sajnos nem sikerült...')
    print('De majd legközelebb... talán... ha nagyobb szerencséd lesz...')
print('Pápá!')

#2.feladat (bővítés)
jelszó = '(*Kk34=('
tipp = input('Mi a jelszó? ')
if tipp == jelszó:
    print('Bemehet.')
else:
    print('Hozzáférés megtagadva.')