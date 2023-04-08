from collections import Counter, defaultdict

file = open('24-s1.txt').readlines()
print(len(file))
min_a = list(map(lambda x: x.count('A'), file))
string = file[min_a.index(min(min_a))]
counter = Counter(string)
find = sorted(counter.most_common(10), key=lambda x: (-x[1], -ord(x[0])))[0][0]
print(open('24-s1.txt').read().count(find))

d = defaultdict(int)
for char in string:
    d[char] += 1
print(d.items())
find = sorted(counter.most_common(10), key=lambda x: (-x[1], -ord(x[0])))[0][0]
print(find)