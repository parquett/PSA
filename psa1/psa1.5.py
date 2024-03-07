import hashlib
import os

def md5_hashing(value):
  digest = hashlib.md5(value).hexdigest()
  return digest[:2]

collision_count = 0
lut = {}
for _ in range(0, 256):
    rvalue = os.urandom(16)
    digest = md5_hashing(rvalue)
    if digest in lut:
        collision_count += 1
    else:
        lut[digest] = True
        print("Collision count =", collision_count)
