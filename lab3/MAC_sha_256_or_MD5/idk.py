"""
bierze pliki, liczy hashe, sprawdza z checksumami i okresla czy pliki sa dalej takie same
jezeli sa inne, to hash bedzie inny od checksuma
12/13 linijka zmienia sha256 i md5 w zaleznosci od tego co jest potrzebne
original.file i some_other_original.file - pliki do sprawdzenia
checksums.txt - plik z checksumami

do sprawdzenia poprawnosci trzeba zakomentowac funkcje 'create_checksum_file' i odkomentowac 'verify_files'
"""

import hashlib
import os


def generate_hash(file_path):
    hash_value = hashlib.sha256()
    # hash_value = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_value.update(chunk)
    return hash_value.hexdigest()


def create_checksum_file(file_paths, checksum_file="checksums.txt"):
    """Tworzy plik kontrolny z hashami dla podanych plików."""
    with open(checksum_file, "w") as f:
        for file_path in file_paths:
            if os.path.isfile(file_path):
                file_hash = generate_hash(file_path)
                f.write(f"{file_hash} {file_path}\n")
                print(f"Hash dla {file_path}: {file_hash}")
            else:
                print(f"Plik {file_path} nie istnieje!")


def verify_files(checksum_file="checksums.txt"):
    """Sprawdza integralność plików na podstawie pliku kontrolnego."""
    with open(checksum_file, "r") as f:
        for line in f:
            saved_hash, file_path = line.strip().split(" ", 1)
            if os.path.isfile(file_path):
                current_hash = generate_hash(file_path)
                if current_hash == saved_hash:
                    print(f"{file_path} jest zgodny.")
                else:
                    print(f"{file_path} ZOSTAŁ ZMIENIONY!")
            else:
                print(f"Plik {file_path} nie istnieje!")


file_paths = ["original.file", "some_other_original.file"]
create_checksum_file(file_paths)

verify_files()
