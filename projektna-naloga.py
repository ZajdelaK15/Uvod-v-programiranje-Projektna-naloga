from tkinter import *
from random import randint


ugib = 0
krog = 0
zaporedje = []
zmaga = False
sifra = []
kombinacija = []

#----------------------------------------------------------------------------------------------------------------------#

class Mastermind():
    def __init__(self, master):

        global ugib, krog, zaporedje, kombinacija
        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'salmon1', 'chartreuse3', 'SteelBlue1']
        sifra = []


        #GLAVNI MENI
        menu = Menu(master)
        master.config(menu=menu)

        #PODMENI DATOTEKA
        file_menu = Menu(menu)
        menu.add_cascade(label='več možnosti', menu=file_menu)

        file_menu.add_command(label='nova igra', command=self.nova_igra)
        file_menu.add_command(label='izhod', command=master.destroy)


        #SESTAVIMO NAKLJUČNO ZAPOREDJE
        for c in range(4):
            barva = randint(0, len(barve)-1)
            sifra.append(barve[barva])
            del barve[barva]
            #print(sifra)


#----------------------------------------------------------------------------------------------------------------------#

        #NAVODILA
        navodila = Label(text='\nUGANI ZAPOREDJE \n \nNAVODILA: S pomočjo logičnega razmišljanja '
                              'in s klikanjem na barvaste gumbe \n poizkušajte ugotoviti pravilno zaporedje '
                              'štirih različnih barv, ki ga je za vas pripravil računalnik. \n '
                              'Ob vsaki izpolnjeni vrstici vam program v prvi kvadratek vpiše število barv, '
                              'ki so pravilne in hkrati \n na pravem mestu, v drugi kvadratek pa koliko barv je pravilnih, '
                              'vendar na napačnem mestu. \n Če vam v ponujenem številu poskusov uspe ugotoviti pravilno zaporedje, ste zmagali.\n')
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

    def nova_igra(self):
        global zmaga, sifra, ugib, krog, kombinacija
        zmaga = False
        barve = ['RoyalBlue3', 'DarkOrange1', 'red3', 'medium purple', 'gold', 'cornsilk3', 'salmon1', 'chartreuse3', 'SteelBlue1']
        sifra = []
        for c in range(4):
            barva = randint(0, len(barve)-1)
            sifra.append(barve[barva])
            del barve[barva]
            #print(sifra)
        ugib = 0
        krog = 0
        kombinacija = []
        self.polje.delete('all')
        self.polje.create_text(215, 50, text=' pravilna \n barva na \n pravem \n mestu', justify='center')
        self.polje.create_text(280, 50, text=' pravilna \n barva na \n napačnem \n mestu', justify='center')
        for i in range(9):
            vnos = self.polje.create_rectangle(55, 90+i*30, 165, 110+i*30)
            for j in range(4):
                kvadratki = self.polje.create_rectangle(60+j*30, 95+i*30, 70+j*30, 105+i*30)
            pravilna_na_pravilnem = self.polje.create_rectangle(200, 90+i*30, 230, 110+i*30)
            pravilna_na_napacnem = self.polje.create_rectangle(265, 90+i*30, 295, 110+i*30)


    def izberi_barvo(self, colour):
        global zaporedje, krog, ugib, zmaga, kombinacija
        zaporedje = []
        if (krog != 9) and (zmaga == False):
            if colour in zaporedje:
                opozorilo = Message(master=None, text='Barve v zaporedju so različne.')
                opozorilo.pack()
                potrditev = Button(master=None, text='v redu')
                potrditev.pack()
            elif ugib == 3:
                kvadratki = self.polje.create_rectangle(60+ugib*30, 95+krog*30, 70+ugib*30, 105+krog*30, fill=colour)
                zaporedje.append(colour)
                kombinacija.append(zaporedje) #drugače je index out of range


                p_n_p = 0 #pravilna barva na pravilnem mestu
                p_n_n = 0 #pravilna barva na napacnem mestu
                for b in range(4):
                    if kombinacija[krog][b] == sifra[b]:
                        p_n_p += 1
                    elif (kombinacija[krog][b] in sifra) and (zaporedje[krog][b] != sifra[b]):
                        p_n_n += 1
                    else:
                        pass
                prvi_kvadratek = self.polje.create_rectangle(210, 100+krog*30, text=p_n_p)
                drugi_kvadratek = self.polje.create_rectangle(275, 100+krog*30, text=p_n_n)
                if p_n_p == 4:
                    dobro_sporocilo = Message(master=None, text='Bravo, uspelo vam je.')
                    dobro_sporocilo.pack()
                    odgovor1 = Button(master=None, text='nova igra', command=self.nova_igra)
                    odgovor1.pack()
                    odgovor2 = Button(master=None, text='končaj', command=None.destroy)
                    odgovor2.pack()
                    zmaga = True
                elif krog == 8:
                    slabo_sporocilo = Message(master=None, text='Žal ste izgubili. Želite poizkusiti ponovno?')
                    slabo_sporocilo.pack()
                    odgovor3 = Button(master=None, text='da', command=self.nova_igra)
                    odgovor3.pack()
                    odgovor4 = Button(master=None, text='ne', command=None.destroy)
                    odgovor4.pack()


                ugib = 0
                zaporedje = []
                krog += 1
            else:
                if ugib == 0:
                    zaporedje = []
                kvadratki = self.polje.create_rectangle(60+ugib*30, 95+krog*30, 70+ugib*30, 105+krog*30, fill=colour)
                zaporedje.append(colour)
                ugib += 1


    def nastavi_temno_modro(self):
        self.izberi_barvo('RoyalBlue3')

    def nastavi_oranzno(self):
        self.izberi_barvo('DarkOrange1')

    def nastavi_rdeco(self):
        self.izberi_barvo('red3')

    def nastavi_vijolicno(self):
        self.izberi_barvo('medium purple')

    def nastavi_zlato(self):
        self.izberi_barvo('gold')

    def nastavi_sivo(self):
        self.izberi_barvo('cornsilk3')

    def nastavi_roza(self):
        self.izberi_barvo('salmon1')

    def nastavi_zeleno(self):
        self.izberi_barvo('chartreuse3')

    def nastavi_svetlo_modro(self):
        self.izberi_barvo('SteelBlue1')



#    def preveri_vneseno_zaporedje(self):
#        global zmaga, krog, sifra, kombinacija
#        p_n_p = 0 #pravilna barva na pravilnem mestu
#        p_n_n = 0 #pravilna barva na napacnem mestu
#        for b in range(0, 4):
#            if kombinacija[krog][b] == sifra[b]:
#                p_n_p += 1
#            elif (kombinacija[krog][b] in sifra) and (zaporedje[krog][b] != sifra[b]):
#                p_n_n += 1
#        prvi_kvadratek = self.polje.create_rectangle(210, 100+krog*30, text=p_n_p)
#        drugi_kvadratek = self.polje.create_rectangle(275, 100+krog*30, text=p_n_n)
#        if krog == 8:
#            slabo_sporocilo = Message(master=None, text='Žal ste izgubili. Želite poizkusiti ponovno?')
#            slabo_sporocilo.pack()
#            odgovor1 = Button(master=None, text='da', command=self.nova_igra)
#            odgovor1.pack()
#            odgovor2 = Button(master=None, text='ne', command=None.destroy)
#            odgovor2.pack()
#        elif p_n_p == 4:
#            dobro_sporocilo = Message(master=None, text='Bravo, uspelo vam je.')
#            dobro_sporocilo.pack()
#            odgovor3 = Button(master=None, text='nova igra', command=self.nova_igra)
#            odgovor3.pack()
#            odgovor4 = Button(master=None, text='končaj', command=None.destroy)
#            odgovor4.pack()
#            zmaga = True


#----------------------------------------------------------------------------------------------------------------------#
okno = Tk()
igra = Mastermind(okno)
okno.mainloop()