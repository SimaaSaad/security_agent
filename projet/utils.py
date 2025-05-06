# utils.py
import os

def run_command(command):
    # Vulnérabilité : Injection de commande via os.system
    os.system(f"echo {command}")
    return "Commande exécutée"

def process_data(data):
    # Pas de validation des entrées
    print(f"Données reçues : {data}")

if __name__ == "__main__":
    user_command = input("Entrez une commande : ")
    run_command(user_command)