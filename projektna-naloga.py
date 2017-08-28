import tkinter as tk
import random

#class Mastermind():
#    def __init__(self, okno):




for i in range(1):
    for j in range(1):
        okno = tk.Tk()
        #NAVODILA
        navodila = tk.Label(text='\nNAVODILA: \n \nV izbranem številu poizkusov poizkušajte ugotoviti pravilno zaporedje štirih različnih barv. '
        '\nČe ga ne ugotovite, vam računalnik pove iskano rešitev.\n'
        'Po vsakem vnosu vam bo program sporočil koliko barv imate '
        'na pravem mestu z besedo "zelena" \nin koliko jih je sicer ustreznih, vendar na '
        'napačnem mestu, z besedo "rumena". Izbirate lahko \nmed barvami rumena, zelena, oranžna, modra, rdeča in siva. '
        'Barve ločujte s presledkom.\n')
        navodila.grid(row=0, column=0, columnspan=3)

        #POLJE ZA UGIBANJE
        polje = tk.Frame(okno, width=100, height=100)
        polje.grid(row=1, column=0)

        #GUMBI Z BARVAMI
        temno_moder_gumb = tk.Button(okno, width=15, height=1, bg='RoyalBlue3')
        temno_moder_gumb.grid(row=5, column=0)

        oranzen_gumb = tk.Button(okno, width=15, height=1, bg='DarkOrange1')
        oranzen_gumb.grid(row=5, column=1)

        rdec_gumb = tk.Button(okno, width=15, height=1, bg='red3')
        rdec_gumb.grid(row=5, column=2)

        vijolicen_gumb = tk.Button(okno, width=15, height=1, bg='medium purple')
        vijolicen_gumb.grid(row=6, column=0)

        zlat_gumb = tk.Button(okno, width=15, height=1, bg='gold')
        zlat_gumb.grid(row=6, column=1)

        siv_gumb = tk.Button(okno, width=15, height=1, bg='cornsilk3')
        siv_gumb.grid(row=6, column=2)

        roza_gumb = tk.Button(okno, width=15, height=1, bg='salmon1')
        roza_gumb.grid(row=7, column=0)

        zelen_gumb = tk.Button(okno, width=15, height=1, bg='chartreuse3')
        zelen_gumb.grid(row=7, column=1)

        svetlo_moder_gumb = tk.Button(okno, width=15, height=1, bg='SteelBlue1')
        svetlo_moder_gumb.grid(row=7, column=2)






        okno.mainloop()




        konec = ''
        while konec == '':
            barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'salmon1', 'chartreuse3', 'SteelBlue1']
            sifra = []


            #sestavimo šifro
            while len(sifra) < 4:
                znak = random.randint(0, 5)
                if barve[znak] not in sifra:
                    sifra.append(barve[znak])


            #ALGORITEM
            for _ in range(9):
                pravilnost = []
                ze_pregledane_barve = []
                izbira = input("vnesi šifro: ").split()
                for barva in range(4):
                    if sifra[barva] == izbira[barva]:
                        pravilnost.append('zelena')
                        ze_pregledane_barve.append(izbira[barva])
                    elif sifra[barva] in izbira and sifra[barva] != izbira[barva]:
                        pravilnost.append('rumena')
                pravilnost = sorted(pravilnost)[::-1]
                if pravilnost == ['zelena', 'zelena', 'zelena', 'zelena']:
                    print('\n')
                    print('Uspelo ti je! :)')
                    break
                print(izbira, pravilnost, sep = '  ', end = '\n')
            print('\n')
            print('Iskana rešitev je bila: {0}'.format(sifra))
            konec = input('Za še eno igro pritisni ENTER.')
            print('\n')
        sifra()


#----------------------------------------------------------------------------------------------------------------------#
#okno = tk.Tk()
#ugani_zaporedje = Mastermind(okno)
#okno.mainloop()