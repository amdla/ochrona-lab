import re
import hashlib
from passlib.hash import sha256_crypt, sha512_crypt, md5_crypt, argon2

# Lista hashy z pliku
hashes = [
    "$sha1$4294967$OOUilDcFFMLNREMDzF8j$KzWuoXraHudEvpjlcnAZu51Oe5bh",
    "$5$rounds=535454$HqGH/NKcuIcQnTat$XTYMrolDMlq0jTvE2M5HlEvRcpABiDEj0W1OOhWvwV5",
    "$6$rounds=645656$WvRRFY4mM9EalwJ1$CaR3PCwL5avpBFWVbIj8jsYmVN3fdDDflOprSYdcDyUHO3uJjuOoZppaulWs.vr1UdVTOqU6MvCSSyQBtmuVq1",
    "$2y$09$dLHDaBvnZcjNkt7CluXkvedRjqxufJFXcKhRxSZeWJiErlA12Fq1G",
    "$2b$13$e9NUzhfBF1.QHnvORw5S6.WHEagqTLcXbazCIKnBxuYR6bBynkD4S",
    "$1$A/Fz53gT$XaFVcCJGiwMqiEP.Jqfv61",
    "$1$NOj3d3M$sDSgbCpgQK.5ey9mMjFnk/",
    "$argon2id$v=19$m=1654,t=5,p=2$zJnTeg/BmHOOMaYU4hxjDA$wrCvr93+Ba/cl119NAic2lX5usaKCCdlsNVZHsoRmtE"
]

password = "password"


# Funkcja do iteracyjnego SHA-1 z solą
def sha1_with_rounds(password, salt, rounds):
    hash_val = (salt + password).encode()
    for _ in range(int(rounds)):
        hash_val = hashlib.sha1(hash_val).digest()
    return hash_val.hex()


# Główna funkcja przetwarzająca i ponownie haszująca
def parse_hash(hash_str):
    result = {}
    generated_hash = ""

    if hash_str.startswith("$sha1$"):
        parts = hash_str.split('$')
        result['algorithm'] = "SHA-1"
        result['rounds'] = parts[2]
        result['salt'] = parts[3]
        print(result['salt'])
        result['hash'] = parts[4]

        # Proste użycie hashlib.sha1 bez iteracji
        sha1_input = (result['salt'] + password).encode()
        generated_hash = hashlib.sha1(sha1_input).hexdigest()

        result['generated_hash'] = generated_hash

    elif hash_str.startswith("$5$"):  # SHA-256
        parts = hash_str.split('$')
        result['algorithm'] = "SHA-256"
        result['rounds'] = re.search(r'rounds=(\d+)', parts[2]).group(1)
        result['salt'] = parts[3]
        result['hash'] = parts[4]
        generated_hash = \
            sha256_crypt.using(rounds=int(result['rounds']), salt=result['salt']).hash(password).split('$')[-1]

    elif hash_str.startswith("$6$"):  # SHA-512
        parts = hash_str.split('$')
        result['algorithm'] = "SHA-512"
        result['rounds'] = re.search(r'rounds=(\d+)', parts[2]).group(1)
        result['salt'] = parts[3]
        result['hash'] = parts[4]
        generated_hash = \
            sha512_crypt.using(rounds=int(result['rounds']), salt=result['salt']).hash(password).split('$')[-1]

    elif hash_str.startswith("$2y$") or hash_str.startswith("$2b$"):  # bcrypt 2y and 2b
        import bcrypt
        parts = hash_str.split('$')
        result['algorithm'] = "bcrypt (2y)" if hash_str.startswith("$2y$") else "bcrypt (2b)"
        result['cost'] = parts[2]
        result['salt'] = parts[3][:22]  # Prawdziwa sól
        result['hash'] = parts[3][22:]  # Oczekiwany hash wynikowy

        # Utworzenie pełnej soli bcrypt z prefiksem wersji, kosztem i solą
        bcrypt_salt = f"${'2y' if hash_str.startswith('$2y$') else '2b'}${result['cost']}${result['salt']}".encode()

        # Generowanie bcrypt hash przy użyciu bcrypt.hashpw
        generated_hash = bcrypt.hashpw(password.encode(), bcrypt_salt).decode().split('$')[-1]


    elif hash_str.startswith("$1$"):  # MD5
        parts = hash_str.split('$')
        result['algorithm'] = "MD5"
        result['salt'] = parts[2]
        result['hash'] = parts[3]
        generated_hash = md5_crypt.using(salt=result['salt']).hash(password).split('$')[-1]

    elif hash_str.startswith("$argon2id$"):  # Argon2id
        parts = hash_str.split('$')
        result['algorithm'] = "Argon2id"
        result['version'] = parts[2].split('=')[1]
        m_t_p = parts[3].split(',')
        result['memory'] = int(m_t_p[0].split('=')[1])
        result['time'] = int(m_t_p[1].split('=')[1])
        result['parallelism'] = int(m_t_p[2].split('=')[1])
        result['salt'] = parts[4].encode()
        result['hash'] = parts[5]
        generated_hash = argon2.using(
            memory_cost=result['memory'],
            time_cost=result['time'],
            parallelism=result['parallelism'],
            salt=result['salt']
        ).hash(password).split('$')[-1]

    result['generated_hash'] = generated_hash
    return result


print("---------------------------------------------------------------------")

for parsed_hash in [parse_hash(h) for h in hashes]:
    print(parsed_hash['algorithm'] + parsed_hash['hash'])
    print(parsed_hash['algorithm'] + parsed_hash['generated_hash'])
