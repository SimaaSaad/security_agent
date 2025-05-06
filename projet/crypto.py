# crypto.py
from hashlib import md5

def hash_password(password):
    # Vulnérabilité : Utilisation de MD5, algorithme cryptographique obsolète
    return md5(password.encode()).hexdigest()

if __name__ == "__main__":
    pwd = input("Entrez un mot de passe : ")
    print(hash_password(pwd))