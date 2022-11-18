def rok_przystepny(year):

    czy_przestepny = (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)

    print('Czy rok', year, 'jest przestępny?', czy_przestepny)

    return czy_przestepny

if __name__ == '__main__':
    rok = int(input("Podaj rok"))
    rok_przystepny(rok)
