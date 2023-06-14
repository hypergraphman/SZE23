f = open('27-1b.txt').readlines()[1:]
sums = 0
mn = float('inf')
for line in f:
    x, y, z = map(int, line.split())
    a = sorted([x, y, z])
    sums += a[2]
    t = a[2] - a[0]
    if t % 4 != 0 and t < mn:
        mn = t
    t = a[2] - a[1]
    if t % 4 != 0 and t < mn:
        mn = t
if sums % 4 == 0:
    sums += mn
print(sums)