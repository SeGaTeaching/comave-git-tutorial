# To-Do-Liste (Konflikt-Version mit alternativem User-Input)
aufgaben = []

def aufgabe_hinzufuegen(titel):
    # Alles in einer Zeile, um die Struktur zu ändern
    aufgaben.append({"id": len(aufgaben) + 1, "titel": titel, "erledigt": False})
    print(f"++ Erfolgreich: '{titel}' wurde notiert.")

def aufgaben_anzeigen():
    if len(aufgaben) == 0: # Andere Abfrage als vorher (if not aufgaben)
        print("=> Aktuell sind keine To-Dos vorhanden.")
        return
    for item in aufgaben:
        markierung = "[X]" if item["erledigt"] else "[ ]"
        print(f"{markierung} {item['id']} | {item['titel']}")

def aufgabe_erledigen(aufgabe_id):
    for item in aufgaben:
        if item["id"] == aufgabe_id:
            item["erledigt"] = True
            print(f"++ Erledigt: '{item['titel']}' ist abgehakt!")
            return
    print(f"-- Fehler: Die ID {aufgabe_id} gibt es nicht.")
    
def aufgabe_loeschen(aufgabe_id):
    global aufgaben
    start_anzahl = len(aufgaben)
    aufgaben = [item for item in aufgaben if item["id"] != aufgabe_id]
    if len(aufgaben) < start_anzahl:
        print(f"++ Gelöscht: To-Do mit ID {aufgabe_id} entfernt.")
    else:
        print(f"-- Fehler: Nichts zum Löschen unter ID {aufgabe_id} gefunden.")

if __name__ == "__main__":
    print("=== TO-DO MANAGER START ===")
    
    programm_laeuft = True # Statt 'while True' nutzen wir eine Variable
    
    while programm_laeuft:
        # Menü in einer Zeile statt mehreren Print-Statements
        print("\n1) Neu | 2) Zeigen | 3) Abhaken | 4) Löschen | 5) Ende")
        
        # Anderer Input-Text
        aktion = input("Wähle eine Aktion (1-5): ")
        
        # Komplett andere Struktur: match/case statt if/elif
        match aktion:
            case "1":
                aufgabe_hinzufuegen(input("Name des neuen To-Dos: "))
            case "2":
                aufgaben_anzeigen()
            case "3":
                try:
                    aufgabe_erledigen(int(input("Welche ID soll abgehakt werden? ")))
                except ValueError:
                    print("Zahl erwartet!")
            case "4":
                try:
                    aufgabe_loeschen(int(input("Welche ID soll gelöscht werden? ")))
                except ValueError:
                    print("Zahl erwartet!")
            case "5":
                print("Manager wird geschlossen. Ciao!")
                programm_laeuft = False # Bricht die Schleife ab (statt 'break')
            case _:
                print("Ungültige Eingabe, versuche es nochmal.")