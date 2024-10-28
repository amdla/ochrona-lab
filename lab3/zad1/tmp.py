import hashlib


def parse_sha1(hash_str, password):
    result = {}
    parts = hash_str.split('$')
    result['algorithm'] = "SHA-1"
    result['rounds'] = int(parts[2])  # Liczba rund
    result['salt'] = parts[3]
    result['hash'] = parts[4]

    # Wstępne połączenie soli z hasłem
    hash_val = (result['salt'] + password).encode()

    # Wykonywanie iteracji SHA-1
    for _ in range(result['rounds']):
        hash_val = hashlib.sha1(hash_val).digest()

    # Konwersja na heksadecymalny wynik końcowy
    generated_hash = hash_val.hex()

    result['generated_hash'] = generated_hash
    return result


# Przykładowe wywołanie dla SHA-1 z rundami
hash_str_sha1 = "$sha1$4294967$OOUilDcFFMLNREMDzF8j$KzWuoXraHudEvpjlcnAZu51Oe5bh"
password = "password"
parsed_sha1 = parse_sha1(hash_str_sha1, password)
print("SHA-1 result:", parsed_sha1)
