
rok=int(input("Podaj rok:"))
czy_rok_jest_wielkorotnoscia_4=(rok%4==0)
wykluczamy_rok_podzielny_na_100=(rok%100!=0)
wielokrotnosc_400=(rok%400==0)
czy_przestepny=wielokrotnosc_400 or wykluczamy_rok_podzielny_na_100 and czy_rok_jest_wielkorotnoscia_4
print("Czy rok", rok, "jest przestepny?", czy_przestepny)
