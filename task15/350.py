for a in range(-1, -100, -1):
    is_a = True
    for k in range(100):
        for m in range(100):
            if not (k + m > 10 or ((k + m > a) and (k - m > a))):
                is_a = False
    if is_a:
        print(a)
