# -------------Makler Programm----------------
# Made by: Bennet Griese und Kaikleefeld
# Datum: 29.01.2023 
# ---------------------------------------------

from colorama import Fore, Style
from raum import Raum
import os

räume = [] # Liste für die Raumnamen

while True:
    print(Fore.CYAN + "\nWillkommen beim Makler-Tool!" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Fläche hinzufügen" + Style.RESET_ALL)
    print(Fore.GREEN + "2. Gesamtfläche berechnen" + Style.RESET_ALL)
    print(Fore.RED + "3. Beenden" + Style.RESET_ALL)
    auswahl = input("Bitte treffen Sie eine Auswahl (1, 2 oder 3): ")
    
    if auswahl == '1': # Fläche hinzufügen
        try:
            name = input(Fore.GREEN + "Bitte geben Sie den Raumnamen ein: " + Style.RESET_ALL)
            laenge = float(input(Fore.GREEN + "Bitte geben Sie die Länge ein: " + Style.RESET_ALL))
            breite = float(input(Fore.GREEN + "Bitte geben Sie die Breite ein: " + Style.RESET_ALL))
            räume.append(Raum(name,laenge,breite)) # Raumnamen in Liste einfügen
            print(Fore.YELLOW + f"Raum {name} hinzugefügt." + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + "Fehler bei der Eingabe: ", e)
            print(Style.RESET_ALL)
            input()
            os.system('cls' if os.name == 'nt' else 'clear')
            
    elif auswahl == '2': # Gesamtfläche berechnen und Räume ausgeben
        gesamtflaeche = sum(int(raum.getFläche()) for raum in räume) # Berechnung der Gesamtfläche
        print(Fore.YELLOW + f"Die Gesamtfläche beträgt: {gesamtflaeche}" + Style.RESET_ALL)
        for raum in räume: # Ausgabe der Räume1 und Flächen
            print(Fore.YELLOW + "-------------------" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Raum: {raum.getName()}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Fläche: {raum.getFläche()}" + Style.RESET_ALL)
        break # Programm beenden
    elif auswahl == '3': # Programm beenden
        print(Fore.RED + "Das Programm wird beendet." + Style.RESET_ALL)
        break # Programm beenden
    else:
        print(Fore.RED + "Ungültige Auswahl. Bitte versuchen Sie es erneut." + Style.RESET_ALL) # Fehlerbehandlung für falsche Eingabe
