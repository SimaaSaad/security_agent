# app.py
import os

def execute_user_input():
    user_input = input("Entrez une expression Python : ")
    # Vulnérabilité : Utilisation de eval, permet l'exécution de code arbitraire
    result = eval(user_input)
    print(f"Résultat : {result}")

# Vulnérabilité : Secret codé en dur
API_KEY = "sk-12345-super-secret-key"

if __name__ == "__main__":
    execute_user_input()