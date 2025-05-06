# server.py
import sqlite3

def query_user(user_id):
    conn = sqlite3.connect("users.db")
    # Vulnérabilité : Injection SQL potentielle
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    user_id = input("Entrez l’ID utilisateur : ")
    print(query_user(user_id))