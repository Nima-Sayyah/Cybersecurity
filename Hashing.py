import hashlib

# encode it to bytes using UTF-8 encoding
message = "Some text to hash".encode()

# hash with MD5 (not recommended)
print("MD5:", hashlib.md5(message).hexdigest())
