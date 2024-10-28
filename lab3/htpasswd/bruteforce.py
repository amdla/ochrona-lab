"""
bruteforce hasla z pliku htpasswd, 3 male litery
"""

import itertools

from passlib.apache import HtpasswdFile


def crack_password(encrypted_password, ht_file):
    """Próbuje złamać hasło o długości 3 znaki składające się z małych liter."""
    for trial in itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=3):
        trial_password = ''.join(trial)
        if ht_file.check_password(encrypted_password, trial_password):
            return trial_password
    return None


def crack_htpasswd(file_path):
    """Próbuje złamać hasła wszystkich użytkowników w pliku htpasswd."""
    ht_file = HtpasswdFile(file_path)
    for username in ht_file.users():
        encrypted_password = ht_file.get_hash(username)
        cracked_password = crack_password(username, ht_file)
        if cracked_password:
            print(f"Użytkownik: {username}, hasło: {cracked_password}")
        else:
            print(f"Użytkownik: {username}, nie udało się złamać hasła")


# Przykładowe użycie
# file_path = "single_pass.htpasswd"
# file_path = "3_pass_1_crackable.htpasswd"
file_path = "bruteforce.htpasswd"
crack_htpasswd(file_path)
