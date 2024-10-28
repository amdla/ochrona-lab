"""
robi plik htpasswd z jakimis tam danymi
"""

from passlib.apache import HtpasswdFile

# Ścieżka do pliku htpasswd
example_htpasswd_path = "bruteforce.htpasswd"

# Utworzenie przykładowego pliku htpasswd z dwoma użytkownikami
htpasswd = HtpasswdFile(example_htpasswd_path, new=True)
htpasswd.set_password("user1", "pas")
htpasswd.set_password("user2", "sec")
htpasswd.save()

print(f"Przykładowy plik htpasswd został utworzony: {example_htpasswd_path}")
