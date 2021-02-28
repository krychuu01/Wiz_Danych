from math import *

# ZAD 1
# Napisz pierwszy skrypt, w którym zadeklarujesz po
# dwie zmienne każdego typu a nastepnie wyświetl te zmienne.

# int1 = 5
# int2 = 3
# float1 = 3.14
# float2 = 11.12
# string1 = "I like html and css"
# string2 = "I need to learn JS"
# complex1 = complex(2, -3)
# complex2 = complex(8, -3)
#
# print(int1, int2, float1, float2, string1, string2, complex1, complex2)

# =======================================================================

# ZAD 2
# Stwórz skrypt kalkulator, w którym wykorzystasz
# wszystkie podstawowe działania arytmetyczne

# a = 6
# b = 4
# c = 3
#
# dodawanie = a + b
# odejmowanie = a - c
# mnozenie = a * c
# dzielenie = a/b
#
# print(dodawanie,odejmowanie,mnozenie,dzielenie)

# =======================================================================

# ZAD 3
# Napisz skrypt, w którym stworzysz operatory
# przyrostkowe dla operacji: +,-,*,/,**,%

# a = 6
# b = 4
#
# a += b    #ADDING
# a -= b    #SUBSTRACTION
# a *= b    #MULTIPLICATION
# a /= b    #DIVISION
# a **= b   #EXPONENTATION
# a %= b    #MODULUS

# =======================================================================

# ZAD 4
# Napisz skrypt, który policzy i wyświetli następujące wyrażenia
# Do tych zadań, trzeba użyć 'from math import *'
#1.

# print(exp(10))

#2.

# sinus = pow(sin(8), 2)
# logarithm = 5 + sinus
# dzialanie = pow(log(logarithm, e), 1/6)
# print(dzialanie)

#3 i #4.
# x = 3.55
# y = 4.80
# print(ceil(x))
# print(floor(y))
# Funkcja ceil zaokrągla ułamek do góry
# Funkcja floor zaokrągla ułamek do dołu

# =======================================================================

# ZAD 5
# Zapisz swoje imie i nazwisko w odzielnych zmiennych wszystkie wielkimi literami.
# Użyj odpowiedniej metody by wyświetlić je napisane tak,
# ze pierwsza litera jest wielka a pozostałe małe.

# first_name = "GRZEGORZ"
# last_name = "KRYCH"
# print(first_name.capitalize() + " " + last_name.capitalize())

# =======================================================================

# ZAD 6
# Napisz skrypt, gdzie w zmiennej string zapiszesz fragment tektsu piosenki
# z powtarzającymi się słowami np. "la la la".
# Następnie użyj odpowiedniej funkcji, która zliczy
# występowanie słowa "la". (Trzeba użyć metody count)

# text = "This is ten percent luck Twenty percent skill " \
#        "Fifteen percent concentrated power of will  " \
#        "Five percent pleasure Fifty percent pain"
#
# how_much = text.count("percent")
#
# print(how_much)

# =======================================================================

# ZAD 7
# Do poszczególnych elementów łańcucha mozemy się odwoływać przez podanie indeksu.
# Np. pierwszy znak zapisany w zmiennej imie uzyskamy przez imie[0].
# Zapisz dowolną zmienną łańcuchową i wyświetl jej drugą i ostatnią literę, wykorzystująć indeksy.

# word = "math"
# print(word[1] + word[3])

# =======================================================================

# ZAD 8
# Zmienne łańcuchowe możemy dzielić.
# Wykorzystaj zmienną z zadania 6 i spróbuj ją podzielić na poszczególne wyrazy.
# (Trzeba użyć metody split)

# text = "This is ten percent luck Twenty percent skill " \
#        "Fifteen percent concentrated power of will  " \
#        "Five percent pleasure Fifty percent pain"
#
# splitted_text = text.split()
#
# print(splitted_text)

# ZAD 9
# Napisz skrypt, w którym zadeklarujesz zmiennie typu:
# string, float i szesnatkowe.
# Nastepnie wyświetl je wykorzystując odpowiednie formatowanie.

# string = "cookies"
# float = 3.14
# hex_number = 127
#
# print("%s %f %s" % (string, float, hex(hex_number)))