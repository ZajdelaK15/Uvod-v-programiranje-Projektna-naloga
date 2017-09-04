
import random

navodila = print('\n UGANI ZAPOREDJE \n \n NAVODILA: \n V izbranem številu poizkusov poizkušajte ugotoviti '
                 'pravilno zaporedje štirih različnih barv.'
                 '\n Če zaporedja ne ugotovite, vam računalnik pove iskano rešitev.'
                 '\n Po vsakem vnosu vam bo program sporočil koliko barv imate na pravem mestu z besedo "zelena" '
                 '\n in koliko jih je sicer ustreznih, vendar na napačnem mestu, z besedo "rumena". '
                 '\n Izbirate lahko med barvami B-bela, R-rumena, O-oranžna, Z-zelena, M-modra, V-vijolična, '
                 'S-siva, Č-črna in T-turkizna.'
                 '\n Barve ločujte s presledkom.')

konec = ''
while konec == '':
    barve = ['B', 'R', 'O', 'Z', 'M', 'V', 'S', 'Č', 'T']
    sifra = []


    #NASTAVITVE
    dolzina_sifre = input('\n Napiši, kako dolgo šifro želiš. Izbiraš lahko med 4, 5 ali 6. Nato pritisni enter. \n IZBIRA: ')
    while dolzina_sifre not in ('4', '5', '6'):
        print('Vnesen podatek ni bil 4, 5 ali 6. Poizkusi ponovno.')
        dolzina_sifre = input('Napiši, kako dolgo šifro želiš. Izbiraš lahko med 4, 5 ali 6. Nato pritisni enter. \n IZBIRA: ')
    dolzina_sifre = int(dolzina_sifre)

    #sestavimo šifro
    while len(sifra) < dolzina_sifre:
        znak = random.randint(0, 5)
        if barve[znak] not in sifra:
            sifra.append(barve[znak])

    stevilo_poskusov = input(' Napiši, koliko poskusov želiš imeti. Nato pritisni enter. \n ŠTEVILO POSKUSOV: ')
    while stevilo_poskusov.isdigit() == False:
        print('Vnesen podatek ni število. Vpiši število! ')
        stevilo_poskusov = input('Napiši, koliko poskusov želiš imeti. Nato pritisni enter. \n ŠTEVILO POSKUSOV: ')
    stevilo_poskusov = int(stevilo_poskusov)
    print('\n')



    while stevilo_poskusov > 0:
        pravilnost = []
        ze_pregledane_barve = []
        zaporedje = input("vnesi šifro: ").split()
        try:
            for znak in range(len(sifra)):
                if sifra[znak] == zaporedje[znak]:
                    pravilnost.append('zelena')
                    ze_pregledane_barve.append(zaporedje[znak])
                elif sifra[znak] in zaporedje and sifra[znak] != zaporedje[znak]:
                    pravilnost.append('rumena')
            pravilnost = sorted(pravilnost)[::-1]
            if pravilnost == ['zelena', 'zelena', 'zelena', 'zelena']:
                print('\n')
                print('Uspelo ti je! :)')
                break
            print(zaporedje, pravilnost, sep = '  ', end = '\n')
            stevilo_poskusov -= 1
        except:
            print('Vnos ni bil pravilen.')
    print('\n')
    print('Iskana rešitev je bila: {0}'.format(sifra))
    konec = input('Za še eno igro pritisni ENTER.')
    print('\n')
sifra()
