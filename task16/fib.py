from functools import lru_cache


@lru_cache(None)
def f(x):
    if x <= 2:
        return 1
    return f(x - 1) + f(x - 2)


n = int(input())
for i in range(100, n, 100):
    f(i)
# cur, nxt = 1, 1
# for i in range(2, n + 1):
#     cur, nxt = nxt, cur + nxt
# print(cur)

a = [0, 1, 1]
for i in range(3, n + 1):
    a.append(a[i - 1] + a[i - 2])
print(a[n])
print(f(n))