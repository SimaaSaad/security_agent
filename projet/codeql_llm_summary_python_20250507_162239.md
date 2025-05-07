```python
# config.py Fix: Log sensitive data as SHA-256 hash instead of plaintext
import logging
import hashlib

# Before: Logging sensitive data in clear text
# logging.info("Secret configuration: %s", secret_config)

# After: Hash sensitive data before logging
hashed_config = hashlib.sha256(secret_config.encode()).hexdigest()
logging.info("Hashed configuration: %s", hashed_config)

# auth.py Fix: Replace SHA1 with bcrypt for password hashing
import bcrypt
import logging

# Before: Insecure SHA1 hashing
# password = "user_password"
# hashed = hashlib.sha1(password.encode()).hexdigest()

# After: Secure bcrypt hashing
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)
logging.debug("Password hashed securely with bcrypt")

# crypto.py Fix: Replace MD5 with bcrypt for password hashing
# Before: Insecure MD5 hashing
# hashed = hashlib.md5(password.encode()).hexdigest()

# After: Same bcrypt implementation as above
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)
```

```python
# Additional considerations:
# 1. Ensure bcrypt is installed: pip install bcrypt
# 2. Always use a secure, randomly generated salt for each password
# 3. Store the salt along with the hashed password
# 4. When verifying passwords, re-hash the input with the stored salt
```

Key improvements made:
1. Sensitive data is now logged as irreversible hashes
2. Passwords are now hashed with bcrypt which includes:
   - Adaptive algorithm resistant to GPU cracking
   - Built-in salt handling
   - Configurable work factor
3. Removed use of cryptographically broken algorithms (MD5/SHA1)
4. Added proper cryptographic best practices for password storage
```