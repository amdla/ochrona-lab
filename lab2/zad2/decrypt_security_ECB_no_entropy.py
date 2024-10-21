from Crypto.Cipher import AES
import os


def decrypt_data(encrypted_data, key):
    """Decrypt data using AES ECB mode without checking padding."""
    aes = AES.new(key, AES.MODE_ECB)
    decrypted_data = aes.decrypt(encrypted_data)
    return decrypted_data


def decrypt_file(file_name):
    """Decrypt an image file using the key that results in a valid BMP header."""
    key_characters = "abcdefghijklmnopqrstuvwxyz0123456789"
    valid_decryptions = []
    with open(file_name, 'rb') as file:
        encrypted_data = file.read()
    # Check if data length is a multiple of 16, pad if necessary
    if len(encrypted_data) % 16 != 0:
        needed_padding = 16 - len(encrypted_data) % 16
        encrypted_data += b"\x00" * needed_padding

    for char in key_characters:
        key = (char * 16).encode('UTF-8')
        decrypted_data = decrypt_data(encrypted_data, key)
        if decrypted_data.startswith(b'BM'):
            valid_decryptions.append((key.decode(), decrypted_data))

    # Write results to a file
    with open("valid_decryption_keys.txt", "w") as file:
        for key, _ in valid_decryptions:
            file.write(f"Key: {key}\n")

    if valid_decryptions:
        best_key, best_decrypted_data = valid_decryptions[0]
        with open(f"decrypted_with_best_key.bmp", "wb") as out_file:
            out_file.write(best_decrypted_data)
        print(f"Decrypted using best key '{best_key}'. Output saved as 'decrypted_with_best_key.bmp'.")
    else:
        print("No valid BMP header found with any of the keys.")


if __name__ == "__main__":
    decrypt_file("./security_ECB_encrypted.bmp")
