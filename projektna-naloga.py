from tkinter import *
from random import randint

#----------------------------------------------------------------------------------------------------------------------#

class Mastermind():
    def __init__(self, master):

        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'salmon1', 'chartreuse3', 'SteelBlue1']
        sifra = []
        zmaga = False

        #GLAVNI MENI
        menu = Menu(master)
        master.config(menu=menu)

        #PODMENI DATOTEKA
        file_menu = Menu(menu)
        menu.add_cascade(label='več možnosti', menu=file_menu)

        file_menu.add_command(label='nova igra', command=self.ponastavi)
        file_menu.add_command(label='izhod', command=master.destroy)


        #SESTAVIMO NAKLJUČNO ZAPOREDJE
        while len(sifra) < 4:
            barva = randint(0, len(barve)-1)
            if barve[barva] not in sifra:
                 sifra.append(barve[barva])
            #print(sifra)

#            #ALGORITEM
#            for _ in range(9):
#                pravilnost = []
#                ze_pregledane_barve = []
#                izbira = input("vnesi šifro: ").split()
#                for barva in range(4):
#                    if sifra[barva] == izbira[barva]:
#                        pravilnost.append('zelena')
#                        ze_pregledane_barve.append(izbira[barva])
#                    elif sifra[barva] in izbira and sifra[barva] != izbira[barva]:
#                        pravilnost.append('rumena')
#                pravilnost = sorted(pravilnost)[::-1]
#                if pravilnost == ['zelena', 'zelena', 'zelena', 'zelena']:
#                    print('\n')
#                    print('Uspelo ti je! :)')
#                    break
#                print(izbira, pravilnost, sep = '  ', end = '\n')
#            print('\n')
#            print('Iskana rešitev je bila: {0}'.format(sifra))
#            konec = input('Za še eno igro pritisni ENTER.')
#            print('\n')
#        sifra()





#----------------------------------------------------------------------------------------------------------------------#

        #NAVODILA
        navodila = Label(text='\nUGANI ZAPOREDJE \n \nNAVODILA: V izbranem številu '
                              'poizkusov poizkušajte ugotoviti pravilno zaporedje \n '
                              'štirih različnih barv. Ob vsakem vnosu vam program sporoči koliko barv'
                              'je pravilnih \n in hkrati na pravem mestu in koliko barv je pravilnih, '
                              'vendar na napačnem mestu. \n')
        navodila.grid(row=0, column=0, columnspan=3)


        #POLJE ZA UGIBANJE
        self.polje = Canvas(master, width=310, height=400)
        self.polje.grid(row=1, column=1)
        self.polje.create_text(215, 50, text=' pravilna \n barva na \n pravem \n mestu', justify='center')
        self.polje.create_text(280, 50, text=' pravilna \n barva na \n napačnem \n mestu', justify='center')
        for i in range(9):
            vnos = self.polje.create_rectangle(55, 90+i*30, 165, 110+i*30)
            for j in range(4):
                kvadratki = self.polje.create_rectangle(60+j*30, 95+i*30, 70+j*30, 105+i*30)
            pravilna_na_pravilnem = self.polje.create_rectangle(200, 90+i*30, 230, 110+i*30)
            pravilna_na_napacnem = self.polje.create_rectangle(265, 90+i*30, 295, 110+i*30)


        #GUMBI Z BARVAMI
        temno_moder_gumb = Button(master, width=15, height=1, bg='RoyalBlue3', command=self.nastavi_temno_modro)
        temno_moder_gumb.grid(row=5, column=0)

        oranzen_gumb = Button(master, width=15, height=1, bg='DarkOrange1', command=self.nastavi_oranzno)
        oranzen_gumb.grid(row=5, column=1)

        rdec_gumb = Button(master, width=15, height=1, bg='red3', command=self.nastavi_rdeco)
        rdec_gumb.grid(row=5, column=2)

        vijolicen_gumb = Button(master, width=15, height=1, bg='medium purple', command=self.nastavi_vijolicno)
        vijolicen_gumb.grid(row=6, column=0)

        zlat_gumb = Button(master, width=15, height=1, bg='gold', command=self.nastavi_zlato)
        zlat_gumb.grid(row=6, column=1)

        siv_gumb = Button(master, width=15, height=1, bg='cornsilk3', command=self.nastavi_sivo)
        siv_gumb.grid(row=6, column=2)

        roza_gumb = Button(master, width=15, height=1, bg='salmon1', command=self.nastavi_roza)
        roza_gumb.grid(row=7, column=0)

        zelen_gumb = Button(master, width=15, height=1, bg='chartreuse3', command=self.nastavi_zeleno)
        zelen_gumb.grid(row=7, column=1)

        svetlo_moder_gumb = Button(master, width=15, height=1, bg='SteelBlue1', command=self.nastavi_svetlo_modro)
        svetlo_moder_gumb.grid(row=7, column=2)

#----------------------------------------------------------------------------------------------------------------------#

    def ponastavi(self):
        zmaga = False
        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'salmon1', 'chartreuse3', 'SteelBlue1']
        sifra = []
        while len(sifra) < 4:
            barva = randint(0, len(barve)-1)
            if barve[barva] not in sifra:
                sifra.append(barve[barva])
            #print(sifra)
        self.polje.delete('all')
        for i in range(9):
            vnos = self.polje.create_rectangle(55, 90+i*30, 165, 110+i*30)
            for j in range(4):
                kvadratki = self.polje.create_rectangle(60+j*30, 95+i*30, 70+j*30, 105+i*30)
            pravilna_na_pravilnem = self.polje.create_rectangle(200, 90+i*30, 230, 110+i*30)
            pravilna_na_napacnem = self.polje.create_rectangle(265, 90+i*30, 295, 110+i*30)

    def nastavi_barvo(self, colour):
        pass

    def nastavi_temno_modro(self):
        self.nastavi_barvo('RoyalBlue3')

    def nastavi_oranzno(self):
        self.nastavi_barvo('DarkOrange1')

    def nastavi_rdeco(self):
        self.nastavi_barvo('red3')

    def nastavi_vijolicno(self):
        self.nastavi_barvo('medium purple')

    def nastavi_zlato(self):
        self.nastavi_barvo('gold')

    def nastavi_sivo(self):
        self.nastavi_barvo('cornsilk3')

    def nastavi_roza(self):
        self.nastavi_barvo('salmon1')

    def nastavi_zeleno(self):
        self.nastavi_barvo('chartreuse3')

    def nastavi_svetlo_modro(self):
        self.nastavi_barvo('SteelBlue1')











#----------------------------------------------------------------------------------------------------------------------#
okno = Tk()
igra = Mastermind(okno)
okno.mainloop()