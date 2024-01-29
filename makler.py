# -------------Makler Programm----------------
# Made by: Bennet Griese und Klaikleefeld
# Datum: 29.01.2023
# ---------------------------------------------


flaechen = []

while True:
    print("\nWillkommen beim Makler-Tool!")
    print("1. Fläche hinzufügen")
    print("2. Gesamtfläche berechnen")
    auswahl = input("Bitte treffen Sie eine Auswahl (1 oder 2): ")

    if auswahl == '1':
        laenge = float(input("Bitte geben Sie die Länge ein: "))
        breite = float(input("Bitte geben Sie die Breite ein: "))
        flaeche = laenge * breite
        flaechen.append(flaeche)
        print(f"Fläche {flaeche} hinzugefügt.")
    elif auswahl == '2':
        gesamtflaeche = sum(flaechen)
        print(f"Die Gesamtfläche beträgt: {gesamtflaeche}")
        break
    else:
        print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")