# -------------Makler Programm----------------
# Made by: Bennet Griese und Klaikleefeld
# Datum: 29.01.2023 
# ---------------------------------------------

from colorama import Fore, Style

flaechen = []
raumname = []

while True:
    print(Fore.CYAN + "\nWillkommen beim Makler-Tool!" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Fläche hinzufügen" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Gesamtfläche berechnen" + Style.RESET_ALL)
    auswahl = input("Bitte treffen Sie eine Auswahl (1 oder 2): ")

    if auswahl == '1':
        name = input("Bitte geben Sie den Raumnamen ein: ")
        laenge = float(input("Bitte geben Sie die Länge ein: "))
        breite = float(input("Bitte geben Sie die Breite ein: "))
        flaeche = laenge * breite
        raumname.append(name)
        flaechen.append(flaeche)
        print(Fore.YELLOW + f"Fläche {flaeche} hinzugefügt." + Style.RESET_ALL)
    elif auswahl == '2':
        gesamtflaeche = sum(flaechen)
        print(Fore.YELLOW + f"Die Gesamtfläche beträgt: {gesamtflaeche}" + Style.RESET_ALL)
        for items in raumname:
            print(Fore.YELLOW + "-------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Raum: {items}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Fläche: {flaechen[raumname.index(items)]}" + Style.RESET_ALL)
        break
    else:
        print(Fore.RED + "Ungültige Auswahl. Bitte versuchen Sie es erneut." + Style.RESET_ALL)