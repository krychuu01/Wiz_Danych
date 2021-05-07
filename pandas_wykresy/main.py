import numpy as np
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

# Zadanie 1

# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku. (imiona.xlsx)

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# suma_dla_roku = df.groupby(['Rok']).agg({'Liczba': ['sum']})
# wykres = suma_dla_roku.plot.line()
# plt.title('Liczba urodzeń dzieci dla danego roku')
# plt.xticks(np.arange(2000, 2018, 1.0))
# plt.xlabel("Lata")
# plt.ylabel("Ilość")
# plt.legend()
# plt.show()



# Zadanie 2
#
# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)
#
# suma_dla_plci = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres = suma_dla_plci.plot.bar()
# plt.title('Liczba urodzeń dzieci z podziałem na płeć')
# plt.xlabel("Płeć")
# plt.yticks(np.arange(0, 4500000, 500000))
# plt.ylabel("Liczba urodzeń")
# plt.gcf().axes[0].yaxis.get_major_formatter().set_scientific(False)
# plt.legend()
# plt.show()



# Zadanie 3
#
# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# df = df[(df['Rok'] >= 2013) & (df['Rok'] <= 2017)]
# suma_dla_plci = df.groupby(['Plec']).agg({'Liczba': ['sum']})
# wykres = suma_dla_plci.plot.pie(subplots= True, autopct='%.2f %%', fontsize=18, figsize=(5, 5), legend=(0, 0))
# plt.legend(loc="upper right")
# plt.show()



# Zadanie 4
#
# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez
# poszczególnych sprzedawców (zbiór danych zamówienia.csv).

# df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=',')
#
# wykres = df.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
# wykres = wykres.plot.bar()
# plt.title('Ilosc złożonych zamówień przez poszczegolnych sprzedawców')
# plt.xlabel("Sprzedawca")
# plt.xticks(rotation=25)
# plt.ylabel("Liczba zamówień")
# plt.legend()
# plt.show()
