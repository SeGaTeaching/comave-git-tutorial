# Aufgaben werden als Liste von Dictionaries gespeichert
aufgaben = []

def aufgabe_hinzufuegen(titel):
    """Fügt eine neue Aufgabe zur Liste hinzu."""
    aufgabe = {
        "id": len(aufgaben) + 1,
        "titel": titel,
        "erledigt": False
    }
    aufgaben.append(aufgabe)
    print(f"Aufgabe '{titel}' hinzugefügt.")

def aufgaben_anzeigen():
    """Zeigt alle Aufgaben mit Status an."""
    if not aufgaben:
        print("Keine Aufgaben vorhanden.")
        return
    for aufgabe in aufgaben:
        status = "✓" if aufgabe["erledigt"] else "○"
        print(f"[{status}] {aufgabe['id']}. {aufgabe['titel']}")

def aufgabe_erledigen(aufgabe_id):
    """Markiert eine Aufgabe anhand ihrer ID als erledigt."""
    for aufgabe in aufgaben:
        if aufgabe["id"] == aufgabe_id:
            aufgabe["erledigt"] = True
            print(f"Aufgabe '{aufgabe['titel']}' als erledigt markiert.")
            return
    print(f"Keine Aufgabe mit ID {aufgabe_id} gefunden.")
    
def aufgabe_loeschen(aufgabe_id):
    """Entfernt eine Aufgabe dauerhaft aus der Liste."""
    global aufgaben
    vorher = len(aufgaben)
    aufgaben = [a for a in aufgaben if a["id"] != aufgabe_id]
    if len(aufgaben) < vorher:
        print(f"Aufgabe {aufgabe_id} gelöscht.")
    else:
        print(f"Keine Aufgabe mit ID {aufgabe_id} gefunden.")

if __name__ == "__main__":
    print("Willkommen zu deiner To-Do-Liste!")
    
    while True:
        print("\n--- Menü ---")
        print("1: Aufgabe hinzufügen")
        print("2: Aufgaben anzeigen")
        print("3: Aufgabe erledigen")
        print("4: Aufgabe löschen")
        print("5: Programm beenden")
        
        auswahl = input("Was möchtest du tun? (1-5): ")
        
        if auswahl == "1":
            titel = input("Titel der neuen Aufgabe: ")
            aufgabe_hinzufuegen(titel)
            
        elif auswahl == "2":
            aufgaben_anzeigen()
            
        elif auswahl == "3":
            try:
                id_eingabe = int(input("ID der erledigten Aufgabe: "))
                aufgabe_erledigen(id_eingabe)
            except ValueError:
                print("Fehler: Bitte gib eine gültige Zahl als ID ein.")
                
        elif auswahl == "4":
            try:
                id_eingabe = int(input("ID der zu löschenden Aufgabe: "))
                aufgabe_loeschen(id_eingabe)
            except ValueError:
                print("Fehler: Bitte gib eine gültige Zahl als ID ein.")
                
        elif auswahl == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
            
        else:
            print("Ungültige Eingabe. Bitte wähle eine Zahl zwischen 1 und 5.")