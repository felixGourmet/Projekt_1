ukoly = []

def hlavni_menu():
    while True:
        print(
            "\nSprávce úkolů – Hlavní menu\n"
            "1. Přidat úkol\n"
            "2. Zobrazit úkoly\n"
            "3. Odstranit úkol\n"
            "4. Konec programu"
        )
        volba = input("Vyberte možnost (1-4): ")
        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("\nKonec programu.\n")
            break
        else:
            print("\nNeplatná volba. Zkuste znovu.")

def pridat_ukol():
    nazev = ""
    while nazev == "":
        nazev = input("\nZadejte název úkolu: ")
        if nazev == "":
            print("\nMusíte napsat název.")
    popis = ""
    while popis == "":
        popis = input("Zadejte popis úkolu: ")
        if popis == "":
            print("\nMusíte napsat popis.")
    ukoly.append(nazev + " – " + popis)
    print(f"\nÚkol '{nazev}' byl přidán.")

def zobrazit_ukoly():
    print("\nSeznam úkolů:")
    if len(ukoly) == 0:
        print("Žádné úkoly.")
    else:
        for i in range(len(ukoly)):
            print(f"{i+1}. {ukoly[i]}")

def odstranit_ukol():
    if len(ukoly) == 0:
        print("Žádné úkoly k odstranění.")
        return
    zobrazit_ukoly()
    cislo = input("\nZadejte číslo úkolu, který chcete odstranit: ")
    if cislo.isdigit():
        i = int(cislo) - 1
        if 0 <= i < len(ukoly):
            del ukoly[i]
            print(f"Úkol '{cislo}' byl odstraněn.")
        else:
            print("Takový úkol neexistuje.")
    else:
        print("Zadejte platné číslo.")

if __name__ == "__main__":
    hlavni_menu()
