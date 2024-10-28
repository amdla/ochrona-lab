import crypt
import random
import string

password = "pass"

salt = ''.join(random.sample(string.ascii_letters, 2))

protected_password = crypt.crypt(password, salt)
print(protected_password)
