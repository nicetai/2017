# -*- coding: utf-8 -*-

import uuid
import hashlib

def encrypt_password(password):
    salt = uuid.uuid4().hex
    result = password
    for i in range(10):
        result = hashlib.sha256(salt.encode() + result.encode()).hexdigest()
    return salt + ':' + result

if __name__ == "__main__":
    pw = 'nice123456'
    print encrypt_password(pw)