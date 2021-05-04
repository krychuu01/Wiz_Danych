import pandas as pd
import numpy as np
import xlrd
import openpyxl

# Zadanie 1
#
# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny w pliku /datasets/imiona.xlsx

# xlsx = pd.ExcelFile('imiona.xlsx')
# df = pd.read_excel(xlsx, header=0)

# ZAD 2
#
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
#
#    1. tylko te rekordy gdzie liczba nadanych imion była mniejsza niż 1000 w danym roku

# print(df[df["Liczba"]<1000])

#    2. tylko rekordy gdzie nadane imię jest takie jak Twoje

# print(df[(df["Imie"]=="GRZEGORZ")])


#    3. sumę wszystkich urodzonych dzieci w całym danym okresie,

# print(sum(df.Liczba))


#    4. sumę dzieci urodzonych w latach 2005-2010

# print(sum(df.Liczba[((df.Rok >= 2005) & (df.Rok <=2010))]))

#    5. sumę urodzonych chłopców w 2000 roku

# print(sum(df.Liczba[((df.Rok == 2005) & (df.Plec == "M"))]))

#    6. najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),

# for x in range(2000, 2018):
#     print('Rok ' + str(x))
#     print(df.Imie[df['Liczba'] == max(df.Liczba[((df.Rok == x) & (df.Plec == 'K'))])])
#     print(df.Imie[df['Liczba'] == max(df.Liczba[((df.Rok == x) & (df.Plec == 'M'))])])

#    7. najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

# print(df.Imie[df.Liczba == max(df.Liczba[(df.Plec == "M")])])
# print(df.Imie[df.Liczba == max(df.Liczba[(df.Plec == 'K')])])


# ZAD 3
# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:

df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

#    1. listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)

# print(df.Sprzedawca.drop_duplicates())

#    2. 5 najwyższych wartości zamówień

# print(df.sort_values(by='Utarg', ascending=False).head(5))

#    3. ilość zamówień złożonych przez każdego sprzedawcę

# print(df.value_counts(df.Sprzedawca))

#    4. sumę zamówień dla każdego kraju

# print(df.groupby('Kraj').Utarg.sum())

#    5. sumę zamówień dla roku 2005, dla sprzedawców z Polski

# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# start_date = pd.to_datetime('1/1/2005')
# end_date = pd.to_datetime('12/31/2005')
#
# print(sum(df.Utarg[(df['Data zamowienia'] >= start_date) &
#                    (df['Data zamowienia'] <= end_date) &
#                    (df['Kraj'] == 'Polska')]))

#    6. średnią kwotę zamówienia w 2004 roku,

# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# start_date = pd.to_datetime('1/1/2004')
# end_date = pd.to_datetime('12/31/2004')
#
# print(np.average(df.Utarg[(df['Data zamowienia'] >= start_date) &
#                    (df['Data zamowienia'] <= end_date)]))

#    7. zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
start_date2004 = pd.to_datetime('1/1/2004')
end_date2004 = pd.to_datetime('12/31/2004')
start_date2005 = pd.to_datetime('1/1/2005')
end_date2005 = pd.to_datetime('12/31/2005')

df2004 = df.loc[(df['Data zamowienia'] >= start_date2004) & (df['Data zamowienia'] <= end_date2004)]
df2005 = df.loc[(df['Data zamowienia'] >= start_date2005) & (df['Data zamowienia'] <= end_date2005)]
df2004.to_csv('zamowienia_2004.csv', sep=';')
df2005.to_csv('zamowienia_2005.csv', sep=';')