f = open('27-1b.txt').readlines()[1:]
sums = 0
diff = []
for line in f:
    line = list(map(int, line.split()))
    sums += min(line)
    if (max(line) - min(line)) % 3 != 0:
        diff.append(max(line) - min(line))
diff.sort()
if sums % 3 == 0:
    sums += diff[0]
print(sums)