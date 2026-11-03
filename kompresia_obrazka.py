def spracuj_riadok(riadok):
    """Vráti riadok z núl a jednotiek zapísaný ako počty za sebou idúcich znakov.
    Ak riadok začína jednotkou, na začiatku je 0 (nula núl)."""
    vysledok = []
    if riadok[0] == "1":
        vysledok.append("0")

    pocitadlo = 1
    for i in range(1, len(riadok)):
        if riadok[i] == riadok[i - 1]:
            pocitadlo += 1
        else:
            vysledok.append(str(pocitadlo))
            pocitadlo = 1
    vysledok.append(str(pocitadlo))

    return " ".join(vysledok)


with open("kompresia_obrazka_1.txt", "r") as fr:
    sirka, vyska = fr.readline().split()
    sirka = int(sirka)
    vyska = int(vyska)
    print(f"Šírka: {sirka}, výška: {vyska}, počet bodov: {sirka * vyska}")

    riadky = [r.strip() for r in fr if r.strip()]


with open("kompresia_obrazka_vystup.txt", "w") as fw:
    fw.write(f"{sirka} {vyska}\n")
    for riadok in riadky:
        fw.write(spracuj_riadok(riadok) + "\n")