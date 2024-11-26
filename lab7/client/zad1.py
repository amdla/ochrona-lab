from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
from client import Client

client = Client('http://localhost:5555')

with open("key.1", "rb") as f:
    pub_key = RSA.import_key(f.read())

cipher = PKCS1_OAEP.new(pub_key)

message = "fhdahfafhaf"
encrypted_message = cipher.encrypt(message.encode('utf-8'))
client.send_binary_message('deadbeef', encrypted_message)
