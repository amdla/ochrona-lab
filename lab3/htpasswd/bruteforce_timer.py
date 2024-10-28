"""
bruteforce hasla o dowolnej dlugosci ze znakow a-z i A-Z
do tego mierzy czas ;33
dziala na timer_task.htpasswd
"""

import itertools
import time

from passlib.apache import HtpasswdFile


def crack_password(username, ht_file, length):
    """Próbuje złamać hasło o określonej długości, składające się z małych i dużych liter."""
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for trial in itertools.product(chars, repeat=length):
        trial_password = ''.join(trial)
        if ht_file.check_password(username, trial_password):
            return trial_password
    return None


def measure_cracking_time(file_path):
    """Mierzy czas potrzebny na złamanie hasła dla każdego użytkownika w pliku htpasswd, z założeniem że każdy użytkownik ma hasło o długości odpowiadającej jego numerowi."""
    ht_file = HtpasswdFile(file_path)
    users = ht_file.users()

    for idx, username in enumerate(users, start=1):
        password_length = idx  # Długość hasła równa numerowi użytkownika
        start_time = time.time()
        cracked_password = crack_password(username, ht_file, password_length)
        elapsed_time = time.time() - start_time

        if cracked_password:
            print(
                f"Użytkownik: {username}, Długość hasła: {password_length}, Hasło: {cracked_password}, Czas: {elapsed_time:.4f} sekundy")
        else:
            print(
                f"Użytkownik: {username}, Długość hasła: {password_length}, Nie udało się złamać hasła w czasie: {elapsed_time:.4f} sekundy")

        print("\n")


# Przykładowe użycie
file_path = "timer_task.htpasswd"
measure_cracking_time(file_path)
