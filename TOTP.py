from hashlib import sha1
import hmac
from datetime import datetime
import math

key = str.encode("JBSWY3DPEHPK3PXP")
unixTime = str(math.floor(datetime.now().timestamp()/30)).encode('UTF-8')  #how to represent unix time in python?
hash = hmac.new(key, unixTime, sha1)   #how to enter multiple inputs into sha1?

print("Type of hash: ", type(hash))
print("Raw hash object: ", hash)
print("Hash digest: ", hash.digest())
print("Digest size: ", hash.digest_size)
print("Hex form of hash: ", hash.hexdigest())
print("integer from hash digest", int.from_bytes(hash.digest(), 'big'))
hashInt =  int.from_bytes(hash.digest(), 'big')
hashIntString = str(hashInt)
offset = hash.digest()[len(hash.digest()) - 1] & 0xf
print("Offset :", offset)
code = ((hash.digest()[offset] & 0x7f) << 24) | ((hash.digest()[offset + 1] & 0xff) << 16) | ((hash.digest()[offset + 2] & 0xff) << 8) | (hash.digest()[offset + 3] & 0xff)
print("OPT code: ", code)
modulusCode = code % (10**6)
print("Modulus code: ", modulusCode)
TOTP = hashInt/(10^len(hashIntString))
print(TOTP)
