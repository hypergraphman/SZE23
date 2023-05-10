n, *a = map(int, open('26-89.txt'))

a.sort(reverse=True)

b = [a[0]]
for i in range(1, len(a)):
    if b[-1] - 3 >= a[i]:
        b.append(a[i])
print(b)
print(len(b), b[-1])