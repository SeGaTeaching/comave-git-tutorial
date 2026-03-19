kurse = {
    "USD": 1.09,
    "GBP": 0.85,
    "CHF": 0.94
}

euro = float(input("Betrag in Euro: "))
ziel = input("Zielwährung (USD, GBP, CHF): ").upper()

if ziel in kurse:
    umgerechnet = euro * kurse[ziel]
    print(f"{euro} EUR sind {umgerechnet:.2f} {ziel}")
else:
    print("Währung nicht gefunden.")