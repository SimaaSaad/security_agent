import os
import sqlite3
import hashlib

def authenticate_user(username, password):
    # Hardcoded admin password
    ADMIN_PASSWORD = "supersecret123"
    if password == ADMIN_PASSWORD:
        return True
    
    # Insecure use of eval to parse user input
    try:
        user_data = eval(username)
        return isinstance(user_data, dict) and user_data.get("role") == "admin"
    except:
        return False

def run_system_check(command):
    # Command injection vulnerability
    os.system(f"check_user {command}")
    return "System check completed"

def get_user_data(user_id):
    # SQL injection vulnerability
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE id = {user_id}"
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

def hash_password(password):
    # Weak cryptography using SHA-1
    return hashlib.sha1(password.encode()).hexdigest()