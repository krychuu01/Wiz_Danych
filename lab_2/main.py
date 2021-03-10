# Zad 1.
#
# Napisz skrypt, w którym tworzysz listę z ulubionymi filmami,
# a następnie odwróć całą listę.
# Po odwróceniu listy dodaj kilka pozycji
# (dodane pozycje mają zostać dodane od 5 indeksu,
# cała lista mam zawierać 10 pozycji)

# lista = ['Skazani na Shawshank','Nietykalni','Zielona Mila',
#          'Ojciec Chrzestny','Dwunastu gniewnych ludzi']
# lista.reverse()
# lista.extend(['Forrest Gump','Lot nad kukulczym gniazdem',
#               'Wladca Pierscieni: Druzyna Pierscienia',
#               'Wladca Pierscieni: Powrot Krola','Django'])
# print(lista)

# ==================================================================

# Zad 2.
# Stwórz skrypt, w którym utworzysz słownik z filmami z zadania 1.
# Pomyśl co może być kluczem.

# slownik = { 'dramat' :["Forrest Gump","Ojciec Chrzestny","Zielona Mila",
#                      "Skazani na Shawshank","Lot nad kukulczym Gniazdem"],
#
#             'komedia':["Forrest Gump","Nietykalni"],
#
#             'fantasy':["Wladca Pierscieni: Druzyna Pierscienia",
#                        "Wladca Pierscieni: Powrot Krola"]}
#
# print(slownik['dramat'])

# ==================================================================

# Zad 3.
# Stwórz skrypt, gdzie utworzysz słownik z nazwami przedmiotów
# z obecnego semestru oraz ich skrótami. Policz liczbę elementów w słowniku.

# slownik = {'nazwa_przedmiotu': ["Komputerowe wspomaganie projektowania", "Programowanie Strukturalne",
# #                                 "Etyka", "Jezyk Angielski", "Wizualizacja Danych", "Matematyka Dyskretna",
# #                                 "Analiza Matematyczna"],
# #
# #             'skroty': ["CAD", "P.S", "ET", "J.A", "W.D", "M.D", "A.M"]}
# #
# # print(len(slownik['skroty'])+len(slownik['nazwa_przedmiotu']))

# ==================================================================

# Zad 4.
# Napisz skrypt gdzie wczytasz liczbę dowolnego typu i podnieś ją
# do tej samej potęgi. Użyj funkcji input. (liczba typu float)

# liczba = float(input("Wprowadz liczbe: "))
# print(pow(liczba,liczba))

# ==================================================================

# Zad 5.
# Napisz skrypt gdzie wczytasz dowolny ciąg znaków,
# i policzysz wystąpienie litery a. Użyj instrukcji readline() i write()).

# file = open("text.txt", "w")
# file.write("aabbaabbaa")
# file.close()
# file = open("text.txt", "r")
# data = (file.readline())
# how_much=data.count("a")
#
# print("How much letters : ",how_much)

# ==================================================================

# Zad 6.
# Wczytaj trzy liczby całkowite a,b,c i
# sprawdź czy liczba a jest parzysta oraz czy jednocześnie b>c

# a = int(input("Wprowadz liczbe a: "))
# b = int(input("Wprowadz liczbe b: "))
# c = int(input("Wprowadz liczbe c: "))
#
# if (a%2==0) & (b>c):
#     print("liczba a jest parzysta i jednoczesnie b jest wieksze od c")
# else:
#     print("liczba a nie jest parzysta, lub b nie jest wieksze od c")

# ==================================================================

# Zad 7.
# Napisz skrypt, gdzie stworzysz listę składającą się z liczb
# typu int i float. Następnie za pomocą pętli for
# oblicz sumę elementu obecnego z poprzednim.

# list = [2, 3.14, 5, 2.73]
# for i in range(0, len(list)):
#     suma = list[i] + list[i-1]
#     print(suma)

# ==================================================================

# Zad 8.
# Napisz skrypt, który za pomocą pętli while pobiera 10 liczb,
# a następnie dodaje do listy tylko liczby parzyste.

# list = []
# z = 0
# while z < 10:
#     a = int(input("Enter a number: "))
#     if (a%2==0):
#         list.append(a)
#     z += 1
# print("\nList with even numbers", list)

# ==================================================================

# Zad 9.
# Napisz skrypt, ktory rysuje nastepujaca litere

# for x in range(0, 1):
#     print('OOOOOOOOOO')
#     for i in range(0, 4):
#         print('O        O')
#     print('OOOOOOOOOO')

# ==================================================================

# Zad 10.
# Napisz skrypt, w którym użytkownik ma podać liczbę
# i który będzie wyłapywał błąd gdy użytkownik poda literę zamiast cyfry.

try:
    a = int(input("Enter a number: "))
    print("Your number:", a)
except ValueError:
    print("Please input a number, not a symbol")
