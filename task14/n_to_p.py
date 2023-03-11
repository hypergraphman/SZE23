def n_to_p(n, p):
    r = ''
    while n:
        r = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[n % p] + r
        n //= p
    return r


print(n_to_p(49 ** 7 + 7 ** 21 - 7, 7).count('6'))


n = 49 ** 7 + 7 ** 21 - 7
r = ''
while n:
    r = '0123456'[n % 7] + r
    n //= 7
print(r.count('6'))

