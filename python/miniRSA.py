import gmpy2

c = 2205316413931134031074603746928247799030155221252519872650080519263755075355825243327515211479747536697517688468095325517209911688684309894900992899707504087647575997847717180766377832435022794675332132906451858990782325436498952049751141
e = 3

def fix(put):
    use = ord(put)
    if use >= 97  :
        return use - 87
    else:
        return use - 48

C = gmpy2.mpz(c)
E = gmpy2.mpz(e)
R, exact = gmpy2.iroot(C, E)
check = 0
ans = 0
final_ans = ""

for i in format(R, 'x'):
    if check == 0:
        check += 1
        ans += fix(i) * 16
    else:
        ans += fix(i)
        final_ans += str(chr(ans))
        check = 0
        ans = 0
print(final_ans)