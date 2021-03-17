
# ====================================================================

# Zad1
# Zdefiniuj następujące zbiory, wykorzystując Python comprehension:
#
# A = {1-x: x ∈ <1,10>}
# B = {1,4,16,…,4**7}
# C = {x: x∈B i x jest liczbą podzielną przez 2}

# A)
# lista_a = [x-1 for x in range(1, 11)]
# print(lista_a)

# B)
# czworka = 4
# lista_b = [4**x for x in range(0, 8)]
# print(lista_b)
#
# # C)
# lista_c = [x for x in lista_b if x % 2 == 0]
# print(lista_c)

# ====================================================================

# Zad2
#
# Wygeneruj losowo 10 elementów, zapisz je do listy1, następnie wykorzystując
# Python Comprehension zdefiniuj nową listę, która będzie zawierała
# tylko parzyste elementy

# import random
# lista1 = []
# for x in range(0, 10):
#     n = random.randint(0,100)
#     lista1.append(n)
# print(lista1)
#
# lista2 = [n for n in lista1 if n % 2 == 0]
# print(lista2)

# ====================================================================

# Zad3
#
# Utwórz słownik z produktami spożywczymi do kupienia.
# Klucz to niech będzie nazwa produktu a
# wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.).
# Wykorzystaj Python Comprehension do zdefiniowania nowej listy,
# gdzie będą produkty, których wartość to sztuki.

# dictionary = {
#     "Ryz": "kilogramy",
#     "Jablka": "kilogramy",
#     "Gruszki": "kilogramy",
#     "Ketchup": "sztuki",
#     "Koncentrat Pomidorowy": "sztuki",
#     "Pizza Neapolitanska": "sztuki"
# }
# lista = [key for (key, value) in dictionary.items() if value == 'sztuki']
# print(lista)

# ====================================================================

# Zad4
#
# Zdefiniuj funkcje, która sprawdzi czy trójkąt jest prostokątny.

# def czy_prostokatny(a, b, c):
#     if a*a == b*b + c*c:
#         print("Jest prostokatny")
#         return a*a == b*b + c*c
#     elif b*b == a*a + c*c:
#         print("Jest prostokatny")
#         return b*b == a*a + c*c
#     elif c*c == a*a + b*b:
#         print("Jest prostokatny")
#         return c*c == a*a + b*b
#     else:
#         print("Nie jest prostokatny")
#         return 2
#
# print(czy_prostokatny(3,4,5))

# ====================================================================

# Zad5
#
# Zdefiniuj funkcje która policzy pole trapezu.
# Funkcja ma przyjmować wartości domyślne.
# def pole_trapezu(a = 0, b = 0, h = 0):
#     return (a+b)*h/2
#
# print(pole_trapezu())
# print(pole_trapezu(8, 6, 4))
# print(pole_trapezu(b= 6, a= 8, h = 4))

# ====================================================================

# Zad6.
#
# Zdefiniuj funkcję która będzie liczyć iloczyn elementów ciągu.
# Parametry funkcji a1 (wartość początkowa),
# b (wielkość o ile mnożone są kolejne elementy),
# ile (ile elementów ma mnożyć)
# Ponadto funkcja niech przyjmuje wartości domyślne: a = 1, b = 4, ile = 10

# def ciag(a = 1, b = 4, ile = 10):
#     i = 0
#     suma = 1
#     for i in range(i, ile):
#         mnozenie = a * b
#         suma *= mnozenie
#     return suma
#
# print(ciag())
# print(ciag(2,4,3))

# ====================================================================

# Zad7
#
# Napisz funkcje za pomocą operatora *,
# która wykona te same działanie co w zadaniu 6.

# def ciag(* liczby):
#     iloczyn_calosci = 1
#     for i in range(0,liczby[2]):
#         mnozenie_elementow = liczby[0]*liczby[1]
#         iloczyn_elementow = mnozenie_elementow
#         iloczyn_calosci *= iloczyn_elementow
#     return iloczyn_calosci
#
# print(ciag(2,4,3))

# ====================================================================

# Zad8
#
# Napisz funkcję, która wykorzystuje symbol **. Funkcja ma przyjmować
# listę zakupów w postaci: klucz to nazwa produktu a wartość to jego koszt.
# Funkcja ma zliczyć ile jest wszystkich produktów w ogóle i zwracać całościową
# wartość tych produktów.

# def lista_zakupow(** produkty):
#     ile_produktow = len(produkty)
#     do_zaplaty = sum(produkty.values())
#     return print("Tyle jest produktow", ile_produktow, "Tyle trzeba zaplacic", do_zaplaty)
#
# lista_zakupow(pizza = 19.99, zupa = 8, zelki = 6, klej = 1.99, chipsy = 5.89)

# ====================================================================

# Zad9
#
# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z
# ciągami arytmetycznymi a drugi niech dotyczy działań
# i wzorów związanych z ciągami geometrycznymi.
# from ciagi import *
#
# print(ciaggeo.suma_n_wyrazow_ciagu_geo(2,2,3))
# print(ciaggeo.znajdz_nty_wyraz_ciagu_geo(2,5,8))
# print(ciagarytm.znajdz_n_ty_wyraz_ciagu(10,5,8))
# print(ciagarytm.suma_n_pierwszych_wyrazow_ciagu(10,5))

