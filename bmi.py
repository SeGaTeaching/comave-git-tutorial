# Einfacher BMI-Rechner

# Eingaben abfragen
gewicht = float(input("Gib dein Gewicht in kg ein: "))
groesse = float(input("Gib deine Größe in Metern ein (z.B. 1.75): "))

# BMI berechnen
# Formel: Gewicht / (Größe * Größe)
bmi = gewicht / (groesse ** 2)

print(f"\nDein BMI beträgt: {bmi:.2f}")

# Einordnung
if bmi < 18.5:
    print("Kategorie: Untergewicht")
elif 18.5 <= bmi < 25:
    print("Kategorie: Normalgewicht")
elif 25 <= bmi < 30:
    print("Kategorie: Übergewicht")
else:
    print("Kategorie: Adipositas (starkes Übergewicht)")