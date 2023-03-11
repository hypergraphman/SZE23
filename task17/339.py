# a = [int(x) for x in open('17-339.txt').readlines()]
a = list(map(int, open('17-339.txt').readlines()))
# mn19 = 10**10
# for el in a:
#     if el % 19 == 0 and x > 0 and el < mn19:
#         mn19 = el
mn19 = min(filter(lambda x: x % 19 == 0 and x > 0, a))

s = [p1 + p2 for p1, p2 in zip(a, a[1:]) if p1 + p2 < mn19]
# for p1, p2 in zip(a, a[1:]):
#     if p1 + p2 < mn19:
#         s.append(p1 + p2)
print(len(s), abs(max(s)))
