n, *a = map(int, open('27-75b.txt'))

k = 43
array_sum = [0] + [None] * (k - 1)
array_len = [0] * k

s = 0
max_sum = 0
min_len = float('inf')
for i in range(n):
    s += a[i]
    if array_sum[s % k]:
        cur_sum = s - array_sum[s % k]
        cur_len = i - array_len[s % k]
        if cur_sum > max_sum:
            max_sum = cur_sum
            min_len = cur_len
        elif cur_sum == max_sum and cur_len < min_len:
            min_len = cur_len
    else:
        array_sum[s % k] = s
        array_len[s % k] = i

print(min_len)