# 1. Úloha: Sčítací past
cislo1 = int(input("Zadej první číslo: "))
cislo2 = int(input("Zadej druhé číslo: "))

print("Součet je:", cislo1 + cislo2)

print()


# 2. Úloha: Opakovač jména
jmeno = input("Zadej jméno: ")
pocet = int(input("Kolikrát se má vypsat? "))

print(jmeno * pocet)

print()


# 3. Úloha: Rok narození
vek = int(input("Kolik ti je let? "))
rok_narozeni = 2026 - vek

print(f"Narodil ses přibližně v roce {rok_narozeni}")

print()


# 4. Úloha: Výplata v hotovosti
mzda = int(input("Zadej hodinovou mzdu: "))
hodiny = int(input("Kolik hodin jsi odpracoval/a? "))

vyplata = mzda * hodiny
print(f"Tvoje výplata je: {vyplata} Kč")

print()


# 5. Úloha: Magická matematika
cislo = int(input("Zadej číslo: "))

vysledek = (cislo + 10) * 2
print(f"Výsledek je: {vysledek}")
