import math
from Crypto.Cipher import ARC4

def calculate_entropy(data):
    if not data:
        return 0
    frequency = {}
    for byte in data:
        frequency[byte] = frequency.get(byte, 0) + 1
    entropy = -sum((count / len(data) * math.log2(count / len(data))) for count in frequency.values())
    return entropy

def decrypt_rc4(key, file_data):
    cipher = ARC4.new(key)
    return cipher.decrypt(file_data)

def main():
    file_path = "encrypted.3rc4"
    try:
        with open(file_path, 'rb') as file:
            file_data = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
        return

    entropy_results = []

    for a in range(ord('a'), ord('z') + 1):
        for b in range(ord('a'), ord('z') + 1):
            for c in range(ord('a'), ord('z') + 1):
                key = chr(a) + chr(b) + chr(c)
                decrypted_data = decrypt_rc4(key.encode(), file_data)
                current_entropy = calculate_entropy(decrypted_data)
                entropy_results.append((key, current_entropy))

    # Write all keys with corresponding entropies to a file
    all_keys_file_path = "keys_with_entropies.txt"
    with open(all_keys_file_path, 'w') as all_keys_file:
        for key, entropy in entropy_results:
            all_keys_file.write(f"Key: {key}, Entropy: {entropy:.4f}\n")

    # Sort the keys by entropy in ascending order
    entropy_results.sort(key=lambda x: x[1])

    # Write the sorted keys to a file
    sorted_keys_file_path = "keys_sorted.txt"
    with open(sorted_keys_file_path, 'w') as sorted_keys_file:
        for key, entropy in entropy_results:
            sorted_keys_file.write(f"Key: {key}, Entropy: {entropy:.4f}\n")

    print(f"All keys and entropies have been written to '{all_keys_file_path}'.")
    print(f"Sorted keys and entropies have been written to '{sorted_keys_file_path}'.")

if __name__ == "__main__":
    main()
