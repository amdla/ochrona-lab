from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import base64
import client

server_url = "http://localhost:5555"
client = client.Client(server_url)

with open("../server/key.1", "rb") as f:
    pub_key = RSA.import_key(f.read())

with open("../server/key.2", "rb") as f:
    private_key = RSA.import_key(f.read())

message = "brglauigas"
hashed_message = SHA256.new(message.encode())

signature = pkcs1_15.new(private_key).sign(hashed_message)
encoded_signature = base64.b64encode(signature).decode()

client.send_text_message("abc", message + "|" + encoded_signature)

received_message = client.get_text_message("abc")
original_message, received_signature = received_message.split('|')
decoded_signature = base64.b64decode(received_signature.encode())
hashed_received_message = SHA256.new(original_message.encode())
pkcs1_15.new(pub_key).verify(hashed_received_message, decoded_signature)

print(original_message)
print(received_signature)
