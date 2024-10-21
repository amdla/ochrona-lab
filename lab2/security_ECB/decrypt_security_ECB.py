from Crypto.Cipher import AES
import math
import os


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


def decrypt_data(encrypted_data, key):
    """Decrypt data using AES ECB mode without checking padding."""
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_data = aes.decrypt(encrypted_data)
    return decrypted_data


def decrypt_file(file_name):
    """Decrypt an image file using the key with the lowest entropy."""
    key_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    results = []
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    # Check if data length is a multiple of 16, pad if necessary
    if len(encrypted_data) % 16 != 0:
        needed_padding = 16 - len(encrypted_data) % 16
        encrypted_data += b"\x00" * needed_padding

    for char in key_characters:
        key = (char * 16).encode('UTF-8')  # Create a key by repeating the character 16 times
        decrypted_data = decrypt_data(encrypted_data, key)
        entropy = calculate_entropy(decrypted_data)
        results.append((key.decode(), entropy, decrypted_data))

    # Sort results by entropy, ascending
    results.sort(key=lambda x: x[1])

    # Write results to a file
    with open("decryption_keys_and_entropy.txt", "w") as file:
        for key, entropy, _ in results:
            file.write(f"Key: {key} - Entropy: {entropy:.4f}\n")

    # Use the key with the lowest entropy to decrypt and save the output
    best_key, _, best_decrypted_data = results[0]
    with open(f"decrypted_with_best_key.bmp", "wb") as out_file:
        out_file.write(best_decrypted_data)
    print(f"Decrypted using best key '{best_key}' with lowest entropy. Output saved as 'decrypted_with_best_key.bmp'.")


if __name__ == "__main__":
    decrypt_file("./security_ECB_encrypted.bmp")
