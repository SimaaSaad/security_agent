```python
# Example fixes for the reported security issues

# 1. Fix for clear-text logging in config.py
# Original insecure code (hypothetical):
# logging.error(f"Sensitive data: {secret}")

# Secure fix: Avoid logging sensitive data directly
def log_sensitive_info(message, sensitive_data):
    # Log without exposing the data
    logging.error(f"{message} (sensitive data redacted)")

# Usage instead of direct logging:
log_sensitive_info("Configuration error occurred", secret_data)

# 2. Fix for SHA-1 in auth.py
import bcrypt  # Requires: pip install bcrypt

# Original insecure code (hypothetical):
# import hashlib
# hashed_password = hashlib.sha1(password.encode()).hexdigest()

# Secure fix using bcrypt:
def hash_password(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

# 3. Fix for MD5 in crypto.py
# Original insecure code (hypothetical):
# import hashlib
# hashed = hashlib.md5(password.encode()).hexdigest()

# Secure fix (same as above using bcrypt):
def secure_hash(data):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(data.encode('utf-8'), salt).decode('utf-8')

# Additional notes:
# - Ensure bcrypt is installed: `pip install bcrypt`
# - Update all password hashing logic to use bcrypt
# - Audit logging code to remove sensitive data exposure
```

This script provides corrected implementations for the reported issues:
1. Uses a helper function to avoid logging sensitive data directly
2. Replaces insecure hashing algorithms with bcrypt for password storage
3. Follows modern cryptographic best practices for password hashing

Always remember to:
- Update all instances of insecure logging and hashing
- Configure logging to filter sensitive data patterns
- Use environment variables or secure vaults for secrets
- Regularly audit code for other potential vulnerabilities