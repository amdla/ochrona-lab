import client

client = client.Client('http://10.42.12.148:5555')
client.get_key("deadbeef")
# pub
with open("../server/key.2", "rb") as f:
    private_key = f.read()

client.send_binary_message("deadbeef", private_key)

# wygeneruj wiadomosc z podpisem, zweryfikuj go
# mamy swoja wiadomosc zahashowac sha256, a potem zaszyfrowac kluczem prywatnym