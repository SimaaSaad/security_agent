```python
import logging
import hashlib
import bcrypt

def log_sensitive_data(data):
    """
    Logs sensitive data as a SHA-256 hash instead of clear text.
    Ensure not to log sensitive data directly; this is a minimal fix.
    """
    hashed_data = hashlib.sha256(data.encode()).hexdigest()
    logging.info(f"Hashed sensitive data: {hashed_data}")

def hash_password(password):
    """
    Secure password hashing using bcrypt instead of SHA1/MD5.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

# Example usage for logging sensitive data (replace in config.py):
# log_sensitive_data("your_secret_here")

# Example usage for password hashing (replace in auth.py and crypto.py):
# password = "user_password"
# hashed = hash_password(password)

# Note: Ensure bcrypt is installed via `pip install bcrypt`
```

**Explanation of fixes:**

1. **Clear-text Logging Fix**:
   - Replaces direct logging of secrets with their SHA-256 hashes.
   - SHA-256 is a stronger algorithm than the unhashed data, but avoid logging sensitive data if possible.

2. **SHA1/MD5 to Bcrypt**:
   - Replaces insecure hashing algorithms (SHA1/MD5) with bcrypt, which is designed for password storage.
   - Bcrypt's computational cost and salting make it resistant to brute-force attacks.

**Implementation Steps**:
1. **Update `config.py`**:
   - Replace logging statements with `log_sensitive_data()` function.
2. **Update `auth.py` and `crypto.py`**:
   - Replace SHA1/MD5 hashing with `hash_password()` function.
3. **Install Dependencies**:
   - Run `pip install bcrypt` to use the bcrypt library.

**Important Notes**:
- Always avoid logging sensitive data whenever possible.
- Use environment variables or secure vaults for storing secrets.
- Ensure bcrypt is properly installed and used with appropriate work factors.