"""
w tym to nie rozumiem polecenia D:
"""


def trivial_hash(dane):
    hash_val = 0
    for znak in dane:
        hash_val += ord(znak)
    return hash_val % 999


def znajdz_kolizje(tekst, docelowy_hash):
    # Ustawiamy początkowy hash tekstu
    current_hash = trivial_hash(tekst)
    modyfikowany_tekst = tekst

    # Dodajemy białe znaki, aż hash się zgodzi z docelowym
    while current_hash != docelowy_hash:
        # Dodajemy białe znaki na końcu tekstu dla zmiany hashu
        modyfikowany_tekst += " "  # Można także używać "\t" lub "\n" dla innych białych znaków
        current_hash = trivial_hash(modyfikowany_tekst)

    return modyfikowany_tekst, current_hash


# Testowanie z przykładowym tekstem i docelowym hashem
tekst = "To  jest  przykładowy  tekst"
docelowy_hash = 123

modyfikowany_tekst, uzyskany_hash = znajdz_kolizje(tekst, docelowy_hash)

print("Oryginalny tekst:", tekst)
print("Modyfikowany tekst:", repr(modyfikowany_tekst))  # repr pokaże białe znaki
print("Docelowy hash:", docelowy_hash)
print("Uzyskany hash:", uzyskany_hash)

# ?????????????????????????????????????
