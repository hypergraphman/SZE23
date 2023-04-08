def f(s, e):
    if s == e:
        return 1
    if s > e or '5' in str(s):
        return 0
    return f(s + 1, e) + f(s * 3, e) + f(s + 3, e)


print(f(1, 49))