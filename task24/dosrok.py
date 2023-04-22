from itertools import product

s = open('24.txt').read()

un_word = set(product('ABC', repeat=2))

max_len = 1
cur_len = 1
for c1, c2 in zip(s, s[1:]):
    if (c1, c2) not in un_word:
        cur_len += 1
        if cur_len > max_len:
            max_len = cur_len
    else:
        cur_len = 1
print(max_len)