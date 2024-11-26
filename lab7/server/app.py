from flask import Flask, request, render_template
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.padding import OAEP, MGF1
from cryptography.hazmat.primitives.hashes import SHA256
import base64
import os

app = Flask(__name__)

messages = {}
keys = {}
deadbeef_key = None


def handle_deadbeef(message):
    resp = {}
    try:
        encoded_message = base64.b64decode(message.encode('utf-8'))
        decrypted = deadbeef_key.decrypt(
            encoded_message,
            OAEP(mgf=MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
        )
        resp['decrypted'] = decrypted.decode('utf-8')
        return resp, 200
    except Exception as e:
        resp['errors'] = str(e)
        return resp, 400


@app.route('/')
def index():
    return render_template('index.html', messages=messages)


@app.route('/message/<uid>', methods=['GET', 'POST'])
def message(uid):
    if request.method == 'GET':
        if uid in messages:
            message, ip = messages[uid]
            return message
        else:
            return f'Nie ma wiadomości do: {uid}', 404

    elif request.method == 'POST':
        json = request.get_json()
        if json and 'message' in json:
            if uid == 'deadbeef':
                return handle_deadbeef(json['message'])
            else:
                messages[uid] = json['message'], request.remote_addr
                return f'Dodano wiadomość dla: {uid}', 200
        else:
            return 'Niepoprawne zapytanie', 400


@app.route('/key/<uid>', methods=['GET', 'POST'])
def key(uid):
    if request.method == 'GET':
        if uid in keys:
            return keys[uid]
        else:
            return f'Nie ma klucza dla: {uid}', 404

    elif request.method == 'POST':
        if uid == 'deadbeef':
            return f'Nie można zmienić klucza', 403

        json = request.get_json()
        if json and 'key' in json:
            keys[uid] = json['key']
            return f'Dodano klucz dla: {uid}', 200
        else:
            return 'Niepoprawne zapytanie', 400


if __name__ == "__main__":
    print("[*] Load deadbeef keys...")
    pubkey_filename = "key.1"  # os.getenv("DEADBEEF_KEY_1")
    privkey_filename = "key.2"  # os.getenv("DEADBEEF_KEY_2")

    # Load public key
    with open(pubkey_filename, 'rb') as key_file:
        pubkey = serialization.load_pem_public_key(key_file.read())
        keys['deadbeef'] = pubkey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode('utf-8')

    # Load private key
    with open(privkey_filename, 'rb') as key_file:
        deadbeef_key = serialization.load_pem_private_key(
            key_file.read(), password=None
        )

    app.run(host="0.0.0.0", port=5555)
