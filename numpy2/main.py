import numpy as np
# Zadanie 1
#
# Utwórz dwie macierze 1x3 różnych wartości a następnie wykonaj operację mnożenia.

# a = np.array([5, 10, 15])
# b = np.array([3, 6, 9])
#
# print(a*b)

# Zadanie 2
#
# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

# a = np.arange(9).reshape(3, 3)
# b = np.arange(16).reshape(4, 4)
#
# print(a.min(axis=0))
# print(a.min(axis=1))
#
# print(b.min(axis=0))
# print(b.min(axis=1))

# Zadanie 3
#
# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.

# print(a.dot(b))

# Zadanie 4
#
# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała
# liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.

# a = np.array([2, 4, 8]).reshape(1, 3)
# b = np.array([4.5, 6.9, 8.2]).reshape(1, 3)
#
# c = a*b
# print(c)

# Zadanie 5
#
# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus
# dla każdej z jej wartości i zapisz do zmiennej “a”.

# a = np.array([90, 20, 50, 30, 10, 60]).reshape(2, 3)
# print(a)
# c = np.sin(a)
# a = c
# print(a)

# Zadanie 6

# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus
# dla każdej z jej wartości i zapisz do zmiennej “b”.

# b = np.array([90, 20, 50, 30, 10, 60]).reshape(2, 3)
# print(b)
# c = np.cos(b)
# b = c
# print(b)

# Zadanie 7

# Wykonaj funkcję dodawania obu macierzy zapisanych wcześniej do zmiennych a i b.

# dodawanie = np.add(a,b)
# print("Macierze po dodaniu: ", dodawanie)

# Zadanie 8

# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

# a = np.arange(9).reshape(3, 3)
#
# for x in a:
#     print(x)

# Zadanie 9
#
# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element
# korzystając z opcji “spłaszczenia” macierzy. (użyj funkcji flat())

# a = np.arange(9).reshape(3, 3)
#
# for x in a.flat:
#     print(x)

# Zad 10.
# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

# a = np.arange(81).reshape(9, 9)
# print(a)
# a = a.reshape(81, 1)
# print(a)
# a = a.reshape(1, 81)
# print(a)
# a = a.reshape(27, 3)
# print(a)
# a = a.reshape(3, 27)
# print(a)

# Zadanie 11
#
# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

# a = np.array([12, 5, 1, 2, 3, 15, 48, 98, 41, 11, 13, 12])
#
# macierz_1 = a.reshape(3,4)
# macierz_2 = a.reshape(4,3)
# macierz_3 = a.reshape(2,6)
#
# print(macierz_1.ravel())
# print(macierz_2.ravel())
# print(macierz_3.ravel())
