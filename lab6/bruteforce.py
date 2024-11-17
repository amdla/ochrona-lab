from passlib.hash import sha256_crypt

# Hash and salt from the password
hashed_password = "$5$rounds=535000$ZJ4umOqZwQkWULPh$LwyaABcGgVyOvJwualNZ5/qM4XcxxPpkm9TKh4Zm4w4"

# Load the RockYou wordlist
wordlist_path = "rockyou.txt"

# Count total lines in the wordlist for progress tracking
with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    total_lines = sum(1 for _ in f)

# Open the wordlist and start processing
with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as wordlist:
    for i, password in enumerate(wordlist):
        password = password.strip()

        # Verify if the password matches the hash
        if sha256_crypt.verify(password, hashed_password):
            print(f"\nPassword found: {password}")
            break

        # Update progress every 0.1% of the list
        if i % (total_lines // 1000) == 0:  # 0.1% step
            progress = (i / total_lines) * 100
            print(f"Progress: {progress:.1f}%", end="\r")
    else:
        print("\nPassword not found in wordlist.")
