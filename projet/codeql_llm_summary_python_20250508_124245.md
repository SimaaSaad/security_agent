```python
# Addressing Security Issues in config.py, auth.py, and crypto.py

# 1. Fix for Clear-text Logging in config.py
# Original (config.py line 15):
# logging.info(f"Sensitive data: {secret}")

# Fixed version using SHA-256 hashing before logging:
import hashlib
def log_sensitive_data(data):
    hashed = hashlib.sha256(data.encode()).hexdigest()
    logging.info(f"Hashed sensitive data: {hashed}")

# Usage:
log_sensitive_data(secret_data)

# 2. Fix for SHA-1 in auth.py
# Original (auth.py line 33):
# import hashlib
# hashed_password = hashlib.sha1(password.encode()).hexdigest()

# Fixed version using bcrypt:
import bcrypt

def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

# Usage:
hashed_password = hash_password(user_password)

# 3. Fix for MD5 in crypto.py
# Original (crypto.py line 4):
# import hashlib
# hashed = hashlib.md5(password.encode()).hexdigest()

# Fixed version using bcrypt:
def secure_hash(data):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(data.encode(), salt)

# Usage:
secure_hashed_password = secure_hash(input_password)

# Note: Ensure bcrypt is installed via `pip install bcrypt`
```

```markdown
### Key Changes Explained:
1. **Clear-text Logging Fix**:
   - **Issue**: Sensitive data logged in plaintext.
   - **Fix**: Use SHA-256 hashing before logging. While not perfect, this prevents direct exposure. Ideally, avoid logging sensitive data entirely if possible.

2. **SHA-1/MD5 Replacement**:
   - **Issue**: Weak hashing algorithms (SHA-1/MD5) used for passwords.
   - **Fix**: Replace with **bcrypt**, a secure, computationally intensive algorithm designed for password hashing. This prevents brute-force attacks.

### Additional Recommendations:
- Use environment variables or secrets management tools (e.g., `python-decouple`, AWS Secrets Manager) for sensitive data storage.
- Update logging configurations to redact sensitive fields automatically.
- Regularly audit code for other insecure practices using tools like Bandit or OWASP Dependency-Check.
```

This script provides corrected code snippets to address the vulnerabilities. Replace the insecure hashing/logging patterns in your project with these implementations and ensure dependencies like `bcrypt` are installed.