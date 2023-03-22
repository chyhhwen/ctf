import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

ALPHABET = "abcdefghijklmnop"


def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc


def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]


def b16_decode(plain):
    enc = ""
    for i in range(0, len(plain), 2):
        binary = "{0:04b}".format(ALPHABET.index(plain[i])) + "{0:04b}".format(ALPHABET.index(plain[i + 1]))
        enc += chr(int(binary, 2))
    return enc


# redacted
# flag = "redacted"
# key = "redacted"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1
# b16 = b16_encode(flag)
# enc = ""
# for i, c in enumerate(b16):
# enc += shift(c, key[i % len(key)])
# print(enc)

enc_flag = "mlnklfnknljflfjljnjijjmmjkmljnjhmhjgjnjjjmmkjjmijhmkjhjpmkmkmljkjijnjpmhmjjgjj"

for i in ALPHABET:
    dec = ""
    for j in enc_flag:
        dec += shift(j, i)
    b16 = b16_decode(dec)
    print("picoCTF{" + b16 + "}")


