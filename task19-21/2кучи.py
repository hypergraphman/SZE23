def f(s1, s2, c, m):
    if s1 + s2 >= 77:
        return c % 2 == m % 2
    if c == m:
        return False
    moves = [f(s1 + 2, s2, c + 1, m),
             f(s1, s2 + 2, c + 1, m),
             f(s1 * 2, s2, c + 1, m),
             f(s1, s2 * 2, c + 1, m)]
    return any(moves) if (c + 1) % 2 == m % 2 else all(moves)


for s in range(1, 70):
    for m in range(1, 5):
        if f(7, s, 0, m):
            print(s, m)
            break


# 2 - Ваня выиграл 1м ходом
# 3 - Петя выиграл 2м ходом
# 4 - Ваня выиграл 2м ходом