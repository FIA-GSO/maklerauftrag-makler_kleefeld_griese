# -------------Makler Programm----------------
# Made by: Bennet Griese und Kaikleefeld
# Datum: 29.01.2023 
# ---------------------------------------------

from colorama import Fore, Style

flaechen = [] # Liste für die Flächen
raumname = [] # Liste für die Raumnamen

while True:
    print(Fore.CYAN + "\nWillkommen beim Makler-Tool!" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Fläche hinzufügen" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Gesamtfläche berechnen" + Style.RESET_ALL)
    print(Fore.RED + "3. Beenden" + Style.RESET_ALL)
    auswahl = input("Bitte treffen Sie eine Auswahl (1, 2 oder 3): ")

    if auswahl == '1': # Fläche hinzufügen
        name = input("Bitte geben Sie den Raumnamen ein: ")
        laenge = float(input("Bitte geben Sie die Länge ein: "))
        breite = float(input("Bitte geben Sie die Breite ein: "))
        flaeche = laenge * breite # Berechnung der Raumfläche
        raumname.append(name) # Raumnamen in Liste einfügen
        flaechen.append(flaeche) # Flächen in Liste einfügen
        print(Fore.YELLOW + f"Fläche {flaeche} hinzugefügt." + Style.RESET_ALL)
    elif auswahl == '2': # Gesamtfläche berechnen und Räume ausgeben
        gesamtflaeche = sum(flaechen) # Berechnung der Gesamtfläche
        print(Fore.YELLOW + f"Die Gesamtfläche beträgt: {gesamtflaeche}" + Style.RESET_ALL)
        for items in raumname: # Ausgabe der Räume und Flächen
            print(Fore.YELLOW + "-------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Raum: {items}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Fläche: {flaechen[raumname.index(items)]}" + Style.RESET_ALL)
        break # Programm beenden
    elif auswahl == '3': # Programm beenden
        print(Fore.RED + "Das Programm wird beendet." + Style.RESET_ALL)
        break # Programm beenden
    else:
        print(Fore.RED + "Ungültige Auswahl. Bitte versuchen Sie es erneut." + Style.RESET_ALL) # Fehlerbehandlung für falsche Eingabe
