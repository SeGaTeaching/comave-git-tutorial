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


if __name__ == "__main__":
    aufgabe_hinzufuegen("Git lernen")
    aufgabe_hinzufuegen("Demo vorbereiten")
    aufgaben_anzeigen()