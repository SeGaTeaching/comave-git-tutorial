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
    aufgabe_hinzufuegen("Git lernen")
    aufgabe_hinzufuegen("Demo vorbereiten")
    aufgaben_anzeigen()