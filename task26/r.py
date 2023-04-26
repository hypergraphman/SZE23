v, n, *a = map(int, open('26.txt').read().split())
a.sort()
k = 0
i = 0
while i < len(a) and v >= a[i]:
    v -= a[i]
    k += 1
    i += 1
v += a[i - 1]
mx = a[i - 1]
while i < len(a) and v >= a[i]:
    mx = a[i]
    i += 1
print(k, mx)