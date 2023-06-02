n, *a = map(int, open('27-75a.txt'))
print(a, n)
k = 43
mx = 0
mx_len = 0
for i in range(n):
    s = 0
    for j in range(i, n):
        s += a[j]
        if s > mx and s % k == 0:
            mx = s
            mx_len = j - i + 1
        if s == mx and j - i + 1 < mx_len and s % k == 0:
            mx_len = j - i + 1
print(mx_len)