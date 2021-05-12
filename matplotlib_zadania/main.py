import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt


# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html


# Zadanie 1

# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].
# Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’)
# oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).


# wartosci = np.arange(1, 21, 1)
# plt.plot(wartosci, 1 / wartosci, label="1/x")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.xlim([1, 20])
# plt.ylim([0, 1])
# plt.legend()
# plt.show()


# Zadanie 2
#
# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

# wartosci = np.arange(1, 21, 1)
# plt.plot(wartosci, 1 / wartosci, 'g>:', label="1/x")
# plt.title("Wykres funkcji f(x) dla x[1,20]")
# plt.xlabel("x")
# plt.ylabel("f(x)")
# plt.xlim([1, 20])
# plt.ylim([0, 1])
# plt.legend()
# plt.show()

# Zadanie 3
#
# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x)
# dla x ϵ [0, 30] z krokiem 0.1. Dodaj etykiety i legendę do wykresu.

# x = np.arange(0, 31, 0.1)
# sin = np.sin(x)
# cos = np.cos(x)
# plt.plot(x, sin, 'r', label="sinus")
# plt.plot(x, cos, 'b', label="cosinus")
# plt.legend()
# plt.show()

# Zadanie 4
#
# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji,
# tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

# x = np.arange(0, 31, 0.1)
# sin = np.sin(x)
# cos = np.sin(x)
# plt.plot(x, -sin, 'r', label="sinus1")
# plt.plot(x, sin+2, 'b', label="sinus2")
# plt.legend()
# plt.show()


# Zadanie 5
#
# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris)
# wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’,
# dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością
# absolutną z różnicy wartości poszczególnych elementów wektorów x oraz y.


# dane = pd.read_csv("iris.csv", )
# df = pd.DataFrame(dane)
# plt.scatter('sepal_length', 'sepal_width', c='c', s=abs(df['sepal_length'] - df['sepal_width']), data=df)
# plt.xlabel('sepal_length')
# plt.ylabel('sepal_width')
# plt.show()


# Zadanie 6
#
# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami
# dzieci przedstawiony w lekcji 8. Następnie na jednym płótnie wyświetl
# 3 wykresy (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety.
# Poustawiaj różne kolory dla wykresów.

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# df_mezczyzni = df[(df["Plec"] == 'M')]
# df_kobiety = df[(df["Plec"] == 'K')]
#
# x1 = ['Kobiety', 'Mezczyzni']
# kobiety_rok = df_kobiety['Rok']
# mezczyzni_rok = df_mezczyzni['Rok']
# x2 = df['Rok']
#
# y1 = [3521321, 3714961]
# kobiety_liczba = df_kobiety['Liczba']
# mezczyzni_liczba = df_mezczyzni['Liczba']
# y2 = df['Liczba']
#
# # 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.

# plt.subplot(1, 3, 1)
# plt.bar(x1, y1)
# plt.title('wykres 1')
# plt.ylabel('liczba urodzen')
# plt.xlabel('plec')

# # 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet,
# # druga dla mężczyzn dla każdego roku z osobna.
# # Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.

# plt.subplot(1, 3, 2)
# plt.plot(kobiety_rok, kobiety_liczba, 'r', mezczyzni_rok, mezczyzni_liczba, 'b')
# plt.title('wykres 2')
# plt.ylabel('liczba urodzen kobiet i mezczyzn na poszczegolny rok')
# plt.xlabel('rok')
#
# # 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.
#
# plt.subplot(1, 3, 3)
# plt.plot(x2, y2, 'green')
# plt.title('wykres 3')
# plt.ylabel('liczba urodzen na kazdy rok')
# plt.xlabel('rok')
#
# plt.show()


# Zadanie 7
#
# Korzystając z pliku zamówienia.csv (Pandas) policz sumy zamówień dla każdego sprzedawcy
# i wyświetl wykres kołowy z procentowym udziałem każdego sprzedawcy w ogólnej sumie zamówień.
# Poszukaj w Internecie jak dodać cień do takiego wykresu i jak działa atrybut ‘explode’ tego wykresu.
# Przetestuj ten atrybut na wykresie.

# dane = pd.read_csv("zamowienia.csv", sep=";")
# df = pd.DataFrame(dane)
# suma_dla_sprzedawcy = df.groupby(['Sprzedawca']).agg({'Utarg': ['sum']})
# explode = (0.1, 0.1, 0.1, 0.1, 0, 0, 0.1, 0.1, 0.1)
# suma_dla_sprzedawcy.plot.pie(explode=explode, subplots=True, shadow=True)
# plt.legend()
# plt.show()