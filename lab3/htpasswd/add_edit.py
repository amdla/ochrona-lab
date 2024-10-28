"""
dodaj / edytuj użytkownika w pliku htpasswd (DZIALA NA WINDOWSIE [YIPPIE])
"""

import os

from passlib.apache import HtpasswdFile


def add_user(htpasswd_file_path, username, password):
    """Dodaje nowego użytkownika do pliku htpasswd lub zmienia hasło istniejącego użytkownika."""
    htpasswd = HtpasswdFile(htpasswd_file_path)

    if htpasswd.check_password(username, password) is not None:
        print(f"Użytkownik '{username}' już istnieje. Aktualizuję hasło...")
    else:
        print(f"Dodaję nowego użytkownika: {username}")

    # Dodaje lub aktualizuje hasło użytkownika
    htpasswd.set_password(username, password)
    htpasswd.save()
    print(f"Hasło dla użytkownika '{username}' zostało ustawione.")


def change_password(htpasswd_file_path, username, new_password):
    """Zmienia hasło istniejącego użytkownika w pliku htpasswd."""
    htpasswd = HtpasswdFile(htpasswd_file_path)

    if username in htpasswd.users():
        htpasswd.set_password(username, new_password)
        htpasswd.save()
        print(f"Hasło dla użytkownika '{username}' zostało zaktualizowane.")
    else:
        print(f"Użytkownik '{username}' nie istnieje w pliku htpasswd.")


def main():
    htpasswd_file_path = "3_pass_1_crackable.htpasswd"

    # Stwórz plik htpasswd, jeśli nie istnieje
    if not os.path.exists(htpasswd_file_path):
        open(htpasswd_file_path, 'w').close()
        print(f"Utworzono nowy plik htpasswd pod ścieżką: {htpasswd_file_path}")

    while True:
        print("\nOpcje:")
        print("1. Dodaj użytkownika lub ustaw hasło")
        print("2. Zmień hasło użytkownika")
        print("3. Wyjdź")

        choice = input("Wybierz opcję (1/2/3): ")

        if choice == '1':
            username = input("Podaj nazwę użytkownika: ")
            password = input("Podaj hasło: ")
            add_user(htpasswd_file_path, username, password)
        elif choice == '2':
            username = input("Podaj nazwę użytkownika: ")
            new_password = input("Podaj nowe hasło: ")
            change_password(htpasswd_file_path, username, new_password)
        elif choice == '3':
            print("Zakończono działanie programu.")
            break
        else:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


if __name__ == "__main__":
    main()
