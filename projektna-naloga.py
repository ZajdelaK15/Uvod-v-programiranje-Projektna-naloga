from tkinter import *
import random

#class Mastermind():
#    def __init__(self, okno):




for i in range(1):
    for j in range(1):
        okno = Tk()
        #NAVODILA
        navodila = Label(text='\nUGANI ZAPOREDJE \n \nNAVODILA: V izbranem številu poizkusov poizkušajte ugotoviti pravilno zaporedje \n '
                              'štirih različnih barv. Ob vsakem vnosu vam program sporoči koliko barv'
                              'je pravilnih \n in hkrati na pravem mestu in koliko barv je pravilnih, vendar na napačnem mestu. \n')
        navodila.grid(row=0, column=0, columnspan=3)


        #POLJE ZA UGIBANJE
        polje = Canvas(okno, width=310, height=400)
        polje.grid(row=1, column=1)
        polje.create_text(215, 50, text=' pravilna \n barva na \n pravem \n mestu', justify='center')
        polje.create_text(280, 50, text=' pravilna \n barva na \n napačnem \n mestu', justify='center')
        for a in range(9):
            vnos = polje.create_rectangle(55, 90+a*30, 165, 110+a*30)
            for b in range(4):
                kvadratki = polje.create_rectangle(60+b*30, 95+a*30, 70+b*30, 105+a*30)
            pravilna_pravilnem = polje.create_rectangle(200, 90+a*30, 230, 110+a*30)
            pravilna_napacnem = polje.create_rectangle(265, 90+a*30, 295, 110+a*30)


        #GUMBI Z BARVAMI
        temno_moder_gumb = Button(okno, width=15, height=1, bg='RoyalBlue3')
        temno_moder_gumb.grid(row=5, column=0)

        oranzen_gumb = Button(okno, width=15, height=1, bg='DarkOrange1')
        oranzen_gumb.grid(row=5, column=1)

        rdec_gumb = Button(okno, width=15, height=1, bg='red3')
        rdec_gumb.grid(row=5, column=2)

        vijolicen_gumb = Button(okno, width=15, height=1, bg='medium purple')
        vijolicen_gumb.grid(row=6, column=0)

        zlat_gumb = Button(okno, width=15, height=1, bg='gold')
        zlat_gumb.grid(row=6, column=1)

        siv_gumb = Button(okno, width=15, height=1, bg='cornsilk3')
        siv_gumb.grid(row=6, column=2)

        roza_gumb = Button(okno, width=15, height=1, bg='salmon1')
        roza_gumb.grid(row=7, column=0)

        zelen_gumb = Button(okno, width=15, height=1, bg='chartreuse3')
        zelen_gumb.grid(row=7, column=1)

        svetlo_moder_gumb = Button(okno, width=15, height=1, bg='SteelBlue1')
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
#okno = Tk()
#ugani_zaporedje = Mastermind(okno)
#okno.mainloop()