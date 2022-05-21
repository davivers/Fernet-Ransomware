import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "m1d.py" or file == "private.key" or file =="m1dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


with open("private.key", "rb") as key:
    secretkey = key.read()


for file in files:
        with open(file, "rb") as locked:
                contents = locked.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as locked:
                locked.write(contents_decrypted)