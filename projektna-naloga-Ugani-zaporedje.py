from tkinter import *
from random import randint


ugib = 0
krog = 0
zaporedje = []
zmaga = False
sifra = []
barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'pink', 'chartreuse3', 'SteelBlue1']

#----------------------------------------------------------------------------------------------------------------------#

class Mastermind():
    def __init__(self, okno):
        self.okno = okno

        global ugib, krog, zaporedje, kombinacija
        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'pink', 'chartreuse3', 'SteelBlue1']
        sifra = []

        #GLAVNI MENI
        menu = Menu(okno)
        okno.config(menu=menu)

        #PODMENI DATOTEKA
        file_menu = Menu(menu)
        menu.add_cascade(label='več možnosti', menu=file_menu)

        file_menu.add_command(label='nova igra', command=self.nova_igra)
        file_menu.add_command(label='izhod', command=okno.destroy)


        #SESTAVIMO NAKLJUČNO ZAPOREDJE
        while len(sifra) < 4:
            znak = randint(0, len(barve)-1)
            if barve[znak] not in sifra:
                sifra.append(barve[znak])
        #print(sifra)


#----------------------------------------------------------------------------------------------------------------------#

        #NAVODILA
        navodila = Label(text='\nUGANI ZAPOREDJE \n \nNAVODILA: S pomočjo logičnega razmišljanja '
                              'in s klikanjem na barvaste gumbe \n poizkušajte ugotoviti pravilno zaporedje '
                              'štirih različnih barv, ki ga je za vas pripravil računalnik. \n '
                              'Ob vsaki izpolnjeni vrstici vam program v prvi kvadratek vpiše število barv, '
                              'ki so pravilne in hkrati \n na pravem mestu, v drugi kvadratek pa koliko barv je '
                              'pravilnih, vendar na napačnem mestu. \n Če vam v ponujenem številu poskusov uspe '
                              'ugotoviti pravilno zaporedje, ste zmagali. \n'
                              '\n Igro začnete tako, da zgoraj kliknete na VEČ MOŽNOSTI in nato NOVA IGRA.')
        navodila.grid(row=0, column=0, columnspan=3)


        #POLJE ZA UGIBANJE
        self.polje = Canvas(okno, width=310, height=400)
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
        temno_moder_gumb = Button(okno, width=15, height=1, bg='RoyalBlue3', command=self.izberi_temno_modro)
        temno_moder_gumb.grid(row=5, column=0)

        oranzen_gumb = Button(okno, width=15, height=1, bg='DarkOrange1', command=self.izberi_oranzno)
        oranzen_gumb.grid(row=5, column=1)

        rdec_gumb = Button(okno, width=15, height=1, bg='red3', command=self.izberi_rdeco)
        rdec_gumb.grid(row=5, column=2)

        vijolicen_gumb = Button(okno, width=15, height=1, bg='medium purple', command=self.izberi_vijolicno)
        vijolicen_gumb.grid(row=6, column=0)

        zlat_gumb = Button(okno, width=15, height=1, bg='gold', command=self.izberi_zlato)
        zlat_gumb.grid(row=6, column=1)

        siv_gumb = Button(okno, width=15, height=1, bg='cornsilk3', command=self.izberi_sivo)
        siv_gumb.grid(row=6, column=2)

        roza_gumb = Button(okno, width=15, height=1, bg='pink', command=self.izberi_roza)
        roza_gumb.grid(row=7, column=0)

        zelen_gumb = Button(okno, width=15, height=1, bg='chartreuse3', command=self.izberi_zeleno)
        zelen_gumb.grid(row=7, column=1)

        svetlo_moder_gumb = Button(okno, width=15, height=1, bg='SteelBlue1', command=self.izberi_svetlo_modro)
        svetlo_moder_gumb.grid(row=7, column=2)

#----------------------------------------------------------------------------------------------------------------------#

    def nova_igra(self):
        global zmaga, sifra, ugib, krog
        zmaga = False
        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'pink', 'chartreuse3', 'SteelBlue1']
        ugib = 0
        krog = 0
        self.polje.delete('all')
        sifra = []
        while len(sifra) < 4:
            znak = randint(0, len(barve)-1)
            if barve[znak] not in sifra:
                sifra.append(barve[znak])
        print(sifra)
        self.polje.create_text(215, 50, text=' pravilna \n barva na \n pravem \n mestu', justify='center')
        self.polje.create_text(280, 50, text=' pravilna \n barva na \n napačnem \n mestu', justify='center')
        for i in range(9):
            vnos = self.polje.create_rectangle(55, 90+i*30, 165, 110+i*30)
            for j in range(4):
                kvadratki = self.polje.create_rectangle(60+j*30, 95+i*30, 70+j*30, 105+i*30)
            pravilna_na_pravilnem = self.polje.create_rectangle(200, 90+i*30, 230, 110+i*30)
            pravilna_na_napacnem = self.polje.create_rectangle(265, 90+i*30, 295, 110+i*30)


    def izberi_barvo(self, barva):
        global zaporedje, krog, ugib, zmaga, barve
        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'pink', 'chartreuse3', 'SteelBlue1']
        if (krog != 9) and (zmaga == False):
            if barva in zaporedje:
                opozorilno_okno = Toplevel()
                opozorilo = Message(opozorilno_okno, text='Barve v zaporedju so različne.')
                opozorilo.grid(row=0, column=0)
                potrditev = Button(opozorilno_okno, text='v redu', command=opozorilno_okno.destroy)
                potrditev.grid(row=0, column=1)
            elif ugib == 3:
                kvadratki = self.polje.create_rectangle(60+ugib*30, 95+krog*30, 70+ugib*30, 105+krog*30, fill=barva)
                zaporedje.append(barva)
                self.preveri_vneseno_zaporedje()
                #print(zaporedje, krog)
                ugib = 0
                zaporedje = []
                krog += 1
            else:
                kvadratki = self.polje.create_rectangle(60+ugib*30, 95+krog*30, 70+ugib*30, 105+krog*30, fill=barva)
                zaporedje.append(barva)
                #print(zaporedje)
                ugib += 1


    def izberi_temno_modro(self):
        self.izberi_barvo('RoyalBlue3')

    def izberi_oranzno(self):
        self.izberi_barvo('DarkOrange1')

    def izberi_rdeco(self):
        self.izberi_barvo('red3')

    def izberi_vijolicno(self):
        self.izberi_barvo('medium purple')

    def izberi_zlato(self):
        self.izberi_barvo('gold')

    def izberi_sivo(self):
        self.izberi_barvo('cornsilk3')

    def izberi_roza(self):
        self.izberi_barvo('pink')

    def izberi_zeleno(self):
        self.izberi_barvo('chartreuse3')

    def izberi_svetlo_modro(self):
        self.izberi_barvo('SteelBlue1')



    def preveri_vneseno_zaporedje(self):
        global sifra, krog, zaporedje, zmaga
        p_n_p = 0 #pravilna barva na pravilnem mestu
        p_n_n = 0 #pravilna barva na napacnem mestu
        #print(zaporedje)
        for b in range(len(sifra)):
            if sifra[b] == zaporedje[b]:
                p_n_p += 1
            elif (zaporedje[b] in sifra) and (sifra[b] != zaporedje[b]):
                p_n_n += 1
        prvi_kvadratek = self.polje.create_text(210, 100+krog*30, text=p_n_p)
        drugi_kvadratek = self.polje.create_text(275, 100+krog*30, text=p_n_n)
        if p_n_p == 4:
            d_s = Toplevel()
            dobro_sporocilo = Message(d_s, text='Bravo, uspelo vam je.')
            dobro_sporocilo.grid(row=0, column=0, columnspan=2)
            odgovor3 = Button(d_s, text='nova igra', command=self.nova_igra)
            odgovor3.grid(row=2, column=0)
            odgovor4 = Button(d_s, text='končaj', command=okno.destroy)
            odgovor4.grid(row=3, column=0)
            zmaga = True
        elif krog == 8:
            s_s = Toplevel()
            slabo_sporocilo = Message(s_s, text='Žal ste izgubili. Želite poizkusiti ponovno?')
            slabo_sporocilo.grid(row=0, column=0, columnspan=2)
            odgovor1 = Button(s_s, text='da', command=self.nova_igra)
            odgovor1.grid(row=1, column=0)
            odgovor2 = Button(s_s, text='ne', command=okno.destroy)
            odgovor2.grid(row=1, column=1)
        else:
            pass


#----------------------------------------------------------------------------------------------------------------------#
okno = Tk()
igra = Mastermind(okno)
okno.mainloop()
