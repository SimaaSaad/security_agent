```python
"""
Security Fixes Script: Addressing Sensitive Data Handling Vulnerabilities

This script provides corrected implementations for the following issues:
1. Clear-text logging of sensitive information
2. Use of weak/insecure hashing algorithms (SHA1/MD5)
"""

import logging
import bcrypt

# 1. Secure logging of sensitive data
def log_sensitive_data(data, message="Sensitive data logged"):
    """
    Logs sensitive data without exposing its actual value.
    Args:
        data (str): The sensitive data to log securely.
        message (str): Optional log message prefix.
    """
    logging.info(f"{message}: [REDACTED]")

# Example usage (instead of logging the actual secret)
secret = "my_secret_key"
log_sensitive_data(secret, "Secret value")

# 2. Secure password hashing using bcrypt (replaces SHA1/MD5)
def hash_password(password):
    """
    Hashes passwords using bcrypt for secure storage.
    Args:
        password (str): The plaintext password to hash.
    Returns:
        bytes: The bcrypt-hashed password
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)

# Example usage for auth.py/crypto.py
password = "user_password"
hashed = hash_password(password)
print("Securely hashed password:", hashed)

# 3. Password verification function (complementary to hashing)
def verify_password(input_password, stored_hash):
    """
    Verifies a password against a stored bcrypt hash.
    Args:
        input_password (str): User-provided password.
        stored_hash (bytes): The stored bcrypt hash.
    Returns:
        bool: True if passwords match, False otherwise
    """
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash)

# Verification example
is_valid = verify_password("user_password", hashed)
print("Password verification result:", is_valid)

# Installation note: pip install bcrypt
```

Key improvements made:
1. **Logging Fix**: Replaced direct logging of sensitive data with a redacted placeholder
2. **Hashing Fixes**:
   - Replaced insecure SHA1/MD5 with bcrypt
   - Added proper password verification function
3. **Security Best Practices**:
   - Salt generation handled by bcrypt
   - Modern password hashing standard (bcrypt)
   - No hard-coded secrets in logs

To use this script:
1. Install bcrypt: `pip install bcrypt`
2. Replace existing hashing logic with the provided functions
3. Modify logging statements to use the secure logging function
4. Ensure proper error handling for password verification
5. Update existing stored hashes incrementally
```