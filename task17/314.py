
a = list(map(int, open('17-304.txt').readlines()))

mm = max(filter(lambda x: x % 246 == 0, a))

s = [p1 + p2 for p1, p2 in zip(a, a[1:]) if p1 + p2 < mm and 'aa' in hex(p1) and 'aa' in hex(p2)]

print(len(s), abs(max(s)))
