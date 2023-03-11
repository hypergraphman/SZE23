for a in range(1, 100):
    is_a = True
    for x in range(1, 100):
        if not (((x & 28 != 0) or (x & 45 != 0)) <= ((x & 17 == 0) <= (x & a != 0))):
            is_a = False
            break

    if is_a:
        print(a)
