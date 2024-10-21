from Crypto.Cipher import AES
import math
import os
from Crypto.Util.Padding import unpad


def calculate_entropy(data):
    """Calculate the Shannon entropy of a byte string."""
    if not data:
        return 0
    entropy = 0
    for x in range(256):
        p_x = float(data.count(bytes([x]))) / len(data)
        if p_x > 0:
            entropy -= p_x * math.log2(p_x)
    return entropy


def decrypt_data(encrypted_data, key, iv):
    """Decrypt data using AES CBC mode with specified IV, attempting to unpad using PKCS7."""
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = aes.decrypt(encrypted_data)
    try:
        decrypted_data = unpad(decrypted_data, AES.block_size)  # Attempt to unpad data
    except ValueError:
        print("Padding is incorrect, or data is corrupted")
    return decrypted_data


def decrypt_file(file_name):
    """Decrypt an image file using the key with the lowest entropy, assuming IV of all zeroes."""
    key_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    results = []
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    iv = b'\x00' * 16  # Assuming a 16-byte IV of all zeroes

    for char in key_characters:
        key = (char * 16).encode('UTF-8')  # Create a key by repeating the character 16 times
        decrypted_data = decrypt_data(encrypted_data, key, iv)
        entropy = calculate_entropy(decrypted_data)
        results.append((key.decode(), entropy, decrypted_data))

    results.sort(key=lambda x: x[1])

    with open("decryption_keys_and_entropy.txt", "w") as file:
        for key, entropy, _ in results:
            file.write(f"Key: {key} - Entropy: {entropy:.4f}\n")

    best_key, _, best_decrypted_data = results[0]
    with open(f"decrypted_with_best_key.bmp", "wb") as out_file:
        out_file.write(best_decrypted_data)
    print(f"Decrypted using best key '{best_key}' with lowest entropy. Output saved as 'decrypted_with_best_key.bmp'.")


if __name__ == "__main__":
    decrypt_file("./security_CBC_encrypted.bmp")
