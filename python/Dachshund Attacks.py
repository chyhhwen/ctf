def rational_to_contfrac(x,y):
    # Converts a rational x/y fraction into a list of partial quotients [a0, ..., an]
    a = x // y
    pquotients = [a]
    while a * y != x:
        x, y = y, x - a * y
        a = x // y
        pquotients.append(a)
    return pquotients

def convergents_from_contfrac(frac):
    # computes the list of convergents using the list of partial quotients
    convs = [];
    for i in range(len(frac)): convs.append(contfrac_to_rational(frac[0 : i]))
    return convs

def contfrac_to_rational (frac):
    # Converts a finite continued fraction [a0, ..., an] to an x/y rational.
    if len(frac) == 0: return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2, -len(frac) - 1, -1): num, denom = frac[_] * num + denom, num
    return (num, denom)
e = 69303856311238509945063303884395360586158336116744369138313577350595035486903073380860377576354392829909956648714064625220601748668080179204467171008725680466181380046059475272517240680066973037670436094569163821931489703947600991637284390574093246025196493292259961920282714754178844023040484204931475964837
n= 89829843397909430028839774543603124608301893898584728934151676996373189487331500933262648649257107224056888903518345007221606976405958569663739194418532588807703048476202398330053603174341471958338734611483943109785826495343590863425869261278294427231183642679736880691264921912458908144614469187160031716297
c= 3964766493796178685058487857613775492405246320717753054633932662506793783624721298106898881157410706186201329404629258581456619836542943638114445396874878763063529719295778516319420129376552769186023425382974229553050497152967251059806969078522512440309871736309378390805673039300590040020205682607964861794
def egcd(a, b):
    if a == 0: return (b, 0, 1)
    g, x, y = egcd(b % a, a)
    return (g, y - (b // a) * x, x)

def mod_inv(a, m):
    g, x, _ = egcd(a, m)
    return (x + m) % m

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
  
def crack_rsa(e, n):
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)
    
    for (k, d) in convergents:
        if k != 0 and (e * d - 1) % k == 0:
            phi = (e * d - 1) // k
            s = n - phi + 1
            # check if x*x - s*x + n = 0 has integer roots
            D = s * s - 4 * n
            if D >= 0:
                sq = isqrt(D)
                if sq * sq == D and (s + sq) % 2 == 0: return d

d = crack_rsa(e, n)
m = hex(pow(c, d, n)).rstrip("L")[2:]
print(m)
