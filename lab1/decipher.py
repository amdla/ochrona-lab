from Crypto.Cipher import ARC4


def decrypt_rc4(key, file_path, output_path):
    try:
        with open(file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return

    # Create RC4 cipher instance
    cipher = ARC4.new(key)

    # Decrypt data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Output the decrypted data to a new file
    with open(output_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"Decrypted data has been written to {output_path}")


def main():
    key = "def"
    file_path = "crypto.rc4"
    output_path = "decrypted_output.txt"
    decrypt_rc4(key.encode(), file_path, output_path)


if __name__ == "__main__":
    main()
