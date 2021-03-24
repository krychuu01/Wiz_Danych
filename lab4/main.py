# =======================================================

# Zad.1
# Wygeneruj liczby z przedziału <0,30>, następnie
# pomnóż je przez 2 i zapisz do pliku
#
# import random
# lista = []
# for x in range(0, 10):
#     n = random.randint(0,30)
#     lista.append(n)
#
# new_list = [x*2 for x in lista]
#
# plik = open("zad1.txt","w+")
# plik.write(str(new_list))
# plik.close()

# =======================================================

# Zad.2
# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
#
# plik = open("zad1.txt", "r")
# print(plik.readline())

# =======================================================

# Zad.3
# Wykorzystując komendę with zapisz kilka linijek tekstu do
# pliku a następnie wyświetl je na ekranie.

# tekst = "Raz dwa trzy\n"
# tekst2 = "Trzy cztery piec\n"
# tekst3 = "hello hello world world\n"
#
# with open("zad3.txt", "w+") as plik:
#     plik.write(tekst)
#     plik.write(tekst2)
#     plik.write(tekst3)
#
# with open("zad3.txt", "r") as plik:
#     for linia in plik:
#         print(linia,end="")

# ZAD 4.
# class NaZakupy:
#     ilosc = None
#     cena_jed = None
#     nazwa_produktu = None
#     jednostka_miary = None
#
#     def __init__(self, ilosc, cena_jed, nazwa_produktu, jednostka_miary):
#         self.ilosc = ilosc
#         self.cena_jed = cena_jed
#         self.nazwa_produktu = nazwa_produktu
#         self.jednostka_miary = jednostka_miary
#
#     def wyswietl_produkt(self):
#         print(self.nazwa_produktu, self.cena_jed, self.jednostka_miary)
#
#     def ile_produktu(self):
#         print(self.ilosc, self.jednostka_miary)
#
#     def ile_kosztuje(self):
#         rownanie = self.ilosc * self.cena_jed
#         print(('%(z1).2f %(z2)s kosztuje %(z3).2f' %
#                {'z1': self.ilosc, 'z2': self.nazwa_produktu, 'z3': rownanie}))
#
#
# nazakupy = NaZakupy(12, 7.99, "Najlepsze Kraftowe Piwo", "sztuk(a)")
# nazakupy.wyswietl_produkt()
# nazakupy.ile_produktu()
# nazakupy.ile_kosztuje()

# ZAD 5.
# class ciag_arytemtyczny:
#     pierwszy_wyraz = 0
#     roznica = 0
#     nty_wyraz = 0
#     nty = 0.0
#
#     def wyswietl_dane(self, pierwszy_wyraz, roznica, nty_wyraz):
#         self.pierwszy_wyraz = pierwszy_wyraz
#         self.roznica = roznica
#         self.nty_wyraz = nty_wyraz
#         print(('Pierwszy wyraz ciagu = %(z1)d \n'
#                'roznica = %(z2)d  \n'
#                'nty_wyraz = %(z3)d \n'
#                          % {'z1': self.pierwszy_wyraz, 'z2': self.roznica, 'z3': self.nty_wyraz}))
#
#     def pobierz_parametry(self):
#         print("Podaj parametry ")
#         self.pierwszy_wyraz = int(input("Pierwszy element ciagu: "))
#         self.roznica = int(input("Roznica ciagu: "))
#         self.nty_wyraz = int(input("Nty wyraz ciagu: "))
#
#     def policz_sume(self):
#         ciag.pobierz_parametry()
#         nty = self.pierwszy_wyraz + (self.nty_wyraz - 1) * self.roznica
#         suma = ((self.pierwszy_wyraz + nty) * self.nty_wyraz) / 2
#         return print("Suma wynosi", suma)
#
#     def policz_elementy(self):
#         ciag.pobierz_parametry()
#         self.liczba_elementow = ((self.nty_wyraz - self.pierwszy_wyraz) / self.roznica) + 1
#         return print("Liczba elementow wynosi = ", self.liczba_elementow)
#

# ciag = ciag_arytemtyczny()
# ciag.wyswietl_dane(15, 10, 5)
# ciag.pobierz_parametry()
# ciag.policz_sume()
# ciag.policz_elementy()

# ZAD 6.
# class Robaczek:
#     x = 3
#     y = 3
#     krok = 1
#
#     def __init__(self, x, y, krok):
#         self.x = x
#         self.y = y
#         self.krok = krok
#
#     def pokaz_gdzie_jestes(self):
#         return print("pozycja x = ",self.x ,"pozycja y =",self.y)
#
#     def idz_w_gore(self, ile_krokow):
#         self.ile_krokow = ile_krokow
#         ile_w_gore = self.ile_krokow * self.krok
#         self.y += ile_w_gore
#
#     def idz_w_dol(self, ile_krokow):
#         self.ile_krokow = ile_krokow
#         ile_w_dol = self.ile_krokow * self.krok
#         self.y -= ile_w_dol
#
#     def idz_w_lewo(self, ile_krokow):
#         self.ile_krokow = ile_krokow
#         ile_w_lewo = self.ile_krokow * self.krok
#         self.x -= ile_w_lewo
#
#     def idz_w_prawo(self, ile_krokow):
#         self.ile_krokow = ile_krokow
#         ile_w_prawo = self.ile_krokow * self.krok
#         self.x += ile_w_prawo
#
#
# robak = Robaczek(3,3,1)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_gore(2)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_lewo(2)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_gore(2)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_prawo(20)
# robak.pokaz_gdzie_jestes()
# robak.idz_w_dol(5)
# robak.pokaz_gdzie_jestes()



