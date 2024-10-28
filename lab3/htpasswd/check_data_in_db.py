"""
sprawdza czy w pliku htpasswd jest ktos o wprowadzonych <username> i <password>
"""

from passlib.apache import HtpasswdFile


def check_user_credentials(htpasswd_file_path, username, password):
    # Załadowanie pliku htpasswd
    try:
        htpasswd = HtpasswdFile(htpasswd_file_path)
    except FileNotFoundError:
        print("Plik htpasswd nie został znaleziony.")
        return False
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
        return False

    # Sprawdzenie, czy użytkownik istnieje, a następnie weryfikacja hasła
    if htpasswd.check_password(username, password):
        print("Dane logowania poprawne.")
        return True
    else:
        print("Niepoprawny identyfikator lub hasło.")
        return False


# Przykład użycia programu
htpasswd_file_path = "3_pass_1_crackable.htpasswd"
username = input("Podaj nazwę użytkownika: ")
password = input("Podaj hasło: ")

# Sprawdzenie poświadczeń użytkownika
check_user_credentials(htpasswd_file_path, username, password)
