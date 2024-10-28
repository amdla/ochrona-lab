"""
to jest lepsze ogolnie, bo nie trzeba czekac 10 minut na wynik, tylko kilka sekund
kwestia paradoksu urodzinowego jak cos ;3
"""

import hashlib
import random
import string


def generate_random_text(length=10):
    """Generuje losowy ciąg znaków składający się z liter i cyfr."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# Lista do przechowywania dokumentów i ich 7-znakowych prefiksów hashy
hashes = []

found_collision = False

while not found_collision:
    # Generowanie losowego dokumentu
    doc = generate_random_text()
    hash_value = hashlib.md5(doc.encode()).hexdigest()  # Używanie MD5 dla przykładu
    hash_prefix = hash_value[:6]  # Pierwsze 6 znaków hash

    # Sprawdzanie kolizji
    for stored_doc, stored_prefix in hashes:
        if stored_prefix == hash_prefix:
            print(f"Kolizja znaleziona!\nDoc1: {stored_doc}, Hash1: {hashlib.md5(stored_doc.encode()).hexdigest()}\n"
                  f"Doc2: {doc}, Hash2: {hash_value}")
            found_collision = True
            break

    # Dodawanie dokumentu i jego 7-znakowego prefiksu hash do listy
    hashes.append((doc, hash_prefix))
