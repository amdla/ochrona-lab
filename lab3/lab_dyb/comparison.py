"""
porownaj czas wykonywania md5, sha256 i argon2
"""

import hashlib
import timeit

from passlib.hash import argon2

# Sample input to hash
sample_input = b"SamplePassword123"


# Define functions to hash using each method
def hash_md5():
    return hashlib.md5(sample_input).hexdigest()


def hash_sha256_hashlib():
    return hashlib.sha256(sample_input).hexdigest()


def hash_sha256_passlib():
    return hashlib.sha256(sample_input).hexdigest()


def hash_argon2_passlib():
    return argon2.hash(sample_input)


# Timing each hashing function
def measure_hashing_speed():
    iterations_md5_sha256 = 1000000  # Set high iterations for faster hashes
    iterations_argon2 = 20  # Lower iterations for Argon2 as it's slower

    md5_time = timeit.timeit(hash_md5, number=iterations_md5_sha256)
    sha256_hashlib_time = timeit.timeit(hash_sha256_hashlib, number=iterations_md5_sha256)
    sha256_passlib_time = timeit.timeit(hash_sha256_passlib, number=iterations_md5_sha256)
    argon2_passlib_time = timeit.timeit(hash_argon2_passlib, number=iterations_argon2)

    # Print results
    print("Hashing Speed Comparison:")
    print(f"MD5 (hashlib): {md5_time:.5f} seconds for {iterations_md5_sha256} iterations")
    print(f"SHA256 (hashlib): {sha256_hashlib_time:.5f} seconds for {iterations_md5_sha256} iterations")
    print(f"SHA256 (passlib): {sha256_passlib_time:.5f} seconds for {iterations_md5_sha256} iterations")
    print(f"Argon2 (passlib): {argon2_passlib_time:.5f} seconds for {iterations_argon2} iterations")


if __name__ == "__main__":
    measure_hashing_speed()
