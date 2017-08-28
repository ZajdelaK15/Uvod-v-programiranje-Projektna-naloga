import tkinter as tk
import random


okno = tk.Tk()
navodila = tk.Label(okno, text='\nNAVODILA: \n \nV izbranem številu poizkusov poizkušajte ugotoviti pravilno zaporedje štirih različnih barv. '
'\nČe ga ne ugotovite, vam računalnik pove iskano rešitev.\n'
'Po vsakem vnosu vam bo program sporočil koliko barv imate '
'na pravem mestu z besedo "zelena" \nin koliko jih je sicer ustreznih, vendar na '
'napačnem mestu, z besedo "rumena". Izbirate lahko \nmed barvami rumena, zelena, oranžna, modra, rdeča in siva. '
'Barve ločujte s presledkom.\n')
navodila.grid(row=0, column=0)
okno.mainloop()


konec = ''
while konec == '':
    stevila = ['1', '2', '3', '4', '5', '6']
    sifra = []


    #NASTAVITVE
    dolzina_sifre = input('Napiši, kako dolgo šifro želiš. Izbiraš lahko med 4, 5 ali 6. Nato pritisni enter. \nIZBIRA: ')
    while dolzina_sifre not in ('4', '5', '6'):
        print('Vnesen podatek ni bil 4, 5 ali 6. Poizkusi ponovno.')
        dolzina_sifre = input('Napiši, kako dolgo šifro želiš. Izbiraš lahko med 4, 5 ali 6. Nato pritisni enter. \nIZBIRA: ')
    dolzina_sifre = int(dolzina_sifre)

    #sestavimo šifro
    while len(sifra) < dolzina_sifre:
        znak = random.randint(0, 5)
        if stevila[znak] not in sifra:
            sifra.append(stevila[znak])

    stevilo_poskusov = input('Napiši, koliko poskusov želiš imeti. Nato pritisni enter. \nŠTEVILO POSKUSOV: ')
    while stevilo_poskusov.isdigit() == False:
        print('Vnesen podatek ni število. Vpiši število! ')
        stevilo_poskusov = input('Napiši, koliko poskusov želiš imeti. Nato pritisni enter. \nŠTEVILO POSKUSOV: ')
    stevilo_poskusov = int(stevilo_poskusov)
    print('\n')


    #ALGORITEM
    while stevilo_poskusov > 0:
        pravilnost = []
        ze_pregledana_stevila = []
        izbira = input("vnesi šifro: ").split()
        try:
            for stevilo in range(len(sifra)):
                if sifra[stevilo] == izbira[stevilo]:
                    pravilnost.append('zelena')
                    ze_pregledana_stevila.append(izbira[stevilo])
                elif sifra[stevilo] in izbira and sifra[stevilo] != izbira[stevilo]:
                    pravilnost.append('rumena')
            pravilnost = sorted(pravilnost)[::-1]
            if pravilnost == ['zelena', 'zelena', 'zelena', 'zelena']:
                print('\n')
                print('Uspelo ti je! :)')
                break
            print(izbira, pravilnost, sep = '  ', end = '\n')
            stevilo_poskusov -= 1
        except:
            print('Vnos ni bil pravilen.')
    print('\n')
    print('Iskana rešitev je bila: {0}'.format(sifra))
    konec = input('Za še eno igro pritisni ENTER.')
    print('\n')
sifra()
