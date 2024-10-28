import hashlib
import random
import string


def add_random_char(text):
    """Dodaje losowy znak na końcu podanego tekstu."""
    return text + random.choice(string.ascii_letters + string.digits)


# Stały tekst dla pierwszego dokumentu
doc1 = "abc123"
hash1 = hashlib.md5(doc1.encode()).hexdigest()
target_prefix = hash1[:10]  # Pierwsze 5 bajtów (10 znaków heksadecymalnych) hexdigestu

found_collision = False
doc2 = doc1  # Startujemy od doc1

# Szukanie drugiego dokumentu, który ma taki sam 5-bajtowy prefiks MD5
while not found_collision:
    # Dodawanie losowego znaku na końcu doc2
    doc2 = add_random_char(doc2)

    # Obliczanie MD5 dla doc2
    hash2 = hashlib.md5(doc2.encode()).hexdigest()

    # Sprawdzanie czy 5-bajtowy prefiks jest taki sam
    if hash2[:10] == target_prefix:
        found_collision = True

# Wyświetlenie wyników
print(f"Doc1: {doc1}, Hash1: {hash1}")
print(f"Doc2: {doc2}, Hash2: {hash2}")
print(f"Pierwsze 5 bajtów (prefiks kolizyjny): {target_prefix}")
