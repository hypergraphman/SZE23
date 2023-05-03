def n_to_p(n, p):
    r = ''
    while n:
        r = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n % p] + r
        n //= p
    return r


print(n_to_p(3 * 292**1031 - 3 * 244**1032 + 16**1033 - 3 * 28**1034 - 1052, 4).count('0'))