# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Hello world!')
imie="Ewa"
print(imie)
print(type(imie))
nazwisko="Neska"
print(imie,nazwisko)
print(imie,"to",nazwisko)

rok=int(input("Podaj rok:"))
czy_rok_jest_wielkorotnoscia_4=(rok%4==0)
wykluczamy_rok_podzielny_na_100=(rok%100!=0)
wielokrotnosc_400=(rok%400==0)
czy_przestepny=wielokrotnosc_400 or wykluczamy_rok_podzielny_na_100 and czy_rok_jest_wielkorotnoscia_4
print("Czy rok", rok, "jest przestepny?", czy_przestepny)
#int oznacza, ze cokolwiek z inputa nie wpadnie to zostanie zamienione na liczbe

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
