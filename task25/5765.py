def divs(n):
    res = {1, n}
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            res.add(d)
            res.add(n // d)
    return sorted(res)


for i in range(77, 100,2):
    if len(divs(i)) == 2:
        print(i ** 4, i ** 3)
