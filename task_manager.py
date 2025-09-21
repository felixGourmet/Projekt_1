ukoly = []

def hlavni_menu():
    while True:
        print(
            "Správce úkolů – Hlavní menu\n"
            "1. Přidat nový úkol\n"
            "2. Zobrazit všechny úkoly\n"
            "3. Odstranit úkol\n"
            "4. Konec programu"
        )

        volba = input("Vyberte možnost (1-4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Program byl ukončen.")
            break
        else:
            print("Neplatná volba. Zkuste to znovu.\n")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if nazev != "":
            break
        print("Název úkolu nesmí být prázdný.")

    while True:
        popis = input("Zadejte popis úkolu: ").strip()
        if popis != "":
            break
        print("Popis úkolu nesmí být prázdný.")

    novy_ukol = {"název": nazev, "popis": popis}
    ukoly.append(novy_ukol)
    print(f"Úkol '{nazev}' byl přidán.\n")

def zobrazit_ukoly():
    if not ukoly:
        print("Žádné úkoly.\n")
        return

    print("\nSeznam úkolů:")
    for i, ukol in enumerate(ukoly, start=1):
        print(f"{i}. {ukol['název']} - {ukol['popis']}")
    print("")

def odstranit_ukol():
    if not ukoly:
        print("Seznam úkolů je prázdný.\n")
        return

    zobrazit_ukoly()
    while True:
        zadani = input("Zadejte číslo úkolu, který chcete odstranit: ").strip()
        if zadani.isdigit():
            index = int(zadani) - 1
            if 0 <= index < len(ukoly):
                odebrany = ukoly.pop(index)
                print(f"Úkol '{odebrany['název']}' byl odstraněn.\n")
                break
        print("Neplatný vstup. Zadejte platné číslo úkolu.")

if __name__ == "__main__":
    hlavni_menu()