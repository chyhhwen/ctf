import requests
from base64 import b64decode, b64encode
from tqdm import tqdm
cookie ="ZW5KQXcxZWpBaDN2c3FTTEI3dTJZS1plTFBaWmF4SzRYMW5LZ0JCNit0VmFtTTI1KzZNOXZ3WnczcFNLVFBDQnRBZEFmMC9aWFdaQkhOS3lyVHFjN09OOTNEeXVJdnhTelh0UVQzbmplZTBHS0VXQ0o1MzJxcHFpK3dCaU1UNG4="
def bit_flip(pos, bit, data):
    raw = b64decode(b64decode(data).decode())
    list1 = bytearray(raw)
    list1[pos] = list1[pos] ^ bit
    raw = bytes(list1)
    return b64encode(b64encode(raw)).decode()
for position_idx in tqdm(range(10), desc="Bruteforcing Position"):
    for bit_idx in tqdm(range(96), desc="Bruteforcing Bit"):
        auth_cookie = bit_flip(position_idx, bit_idx, cookie)
        cookies = {'auth_name': auth_cookie}
        r = requests.get('http://mercury.picoctf.net:25992/', cookies=cookies)
        if "picoCTF{" in r.text:
            print("Flag: " + r.text.split("<code>")[1].split("</code>")[0])
            break
