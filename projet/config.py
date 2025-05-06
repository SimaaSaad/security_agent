# config.py
def load_config():
    # Vulnérabilités : Secrets codés en dur
    DATABASE_URL = "mysql://user:password123@localhost/db"
    SECRET_TOKEN = "abc123-token-xyz789"

    # Vulnérabilité : Utilisation de exec
    config_code = input("Entrez du code de configuration : ")
    exec(config_code)

    return {"db": DATABASE_URL, "token": SECRET_TOKEN}

if __name__ == "__main__":
    config = load_config()
    print(config)