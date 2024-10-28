"""
generuje hasla a-z i A-Z o rosnacej dlugosci dla bruteforce_timer
"""

import random
import string

from passlib.apache import HtpasswdFile


def generate_random_password(length):
    """Generuje losowe hasło o określonej długości składające się z małych i dużych liter."""
    characters = string.ascii_letters  # Małe i duże litery
    return ''.join(random.choice(characters) for _ in range(length))


def create_htpasswd_with_incremental_password_lengths(file_path, num_users):
    """Tworzy plik htpasswd z hasłami o rosnącej długości dla kolejnych użytkowników."""
    htpasswd = HtpasswdFile(file_path, new=True)
    for i in range(1, num_users + 1):
        username = f"user{i}"
        password_length = i  # Długość hasła równa numerowi użytkownika
        password = generate_random_password(password_length)
        htpasswd.set_password(username, password)
        print(f"Użytkownik: {username}, Hasło: {password}")  # Opcjonalnie: wyświetla nazwę użytkownika i hasło
    htpasswd.save()
    print(f"Plik htpasswd został utworzony: {file_path}")


# Parametry
example_htpasswd_path = "timer_task.htpasswd"  # Ścieżka do pliku htpasswd
num_users = 8  # Liczba użytkowników

# Utworzenie przykładowego pliku htpasswd
create_htpasswd_with_incremental_password_lengths(example_htpasswd_path, num_users)
