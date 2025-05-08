```python
# config.py (Fix: Remove sensitive data from logs)
# Original line: logger.info(f"Secret: {secret}")
logger.info("Configuration loaded successfully")
```

```python
# auth.py (Fix: Replace SHA1 with bcrypt)
import bcrypt

# Original line: hashed = hashlib.sha1(password.encode()).hexdigest()
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
```

```python
# crypto.py (Fix: Replace MD5 with bcrypt)
import bcrypt

# Original line: hash = hashlib.md5(data.encode()).hexdigest()
salt = bcrypt.gensalt()
hash = bcrypt.hashpw(data.encode('utf-8'), salt)
```