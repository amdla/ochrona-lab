"""
paradoks urodzinowy czy jakos tak - dodawaj znaki do dokumentu tak dlugo, az nastapi kolizja z innym dokumentem
(no w sensie ze hash bedzie taki sam dla obu)
"""


def trivial_hash(dane):
    hash_val = 0
    for znak in dane:
        hash_val += ord(znak)
    return hash_val % 999


# Przygotowanie dwóch różnych dokumentów
doc1 = "To jest pierwszy dokument."
doc2 = ""

hash1 = trivial_hash(doc1)
hash2 = trivial_hash(doc2)

while hash1 != hash2:
    # Modyfikujemy dokument, dodając znak lub zmieniając treść
    doc2 += "a"
    hash2 = trivial_hash(doc2)

print("Dokument 1:", doc1)
print("Hash 1:", hash1)

print("Dokument 2:", doc2)
print("Hash 2:", hash2)
