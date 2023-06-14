def f(n):
    if n == 0:
        return 3
    if n > 0 and n % 2 == 0:
        return 1 + f(n // 2)
    return f(n // 2)


c = 0
for i in range(1, 1000_000_000 + 1):
    if f'{i:b}'.count('0') == 4:
        c += 1
print(c)
