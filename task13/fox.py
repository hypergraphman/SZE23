g = {
    'А': 'Б',
    'Б': 'Д',
    'Д': 'ВЖЕ',
    'И': 'ДЛ',
    'Л': 'К',
    'Е': 'ИЛКЖ',
    'В': 'АБ',
    'Г': 'АВ',
    'Ж': 'ГВ',
    'К': 'Ж',
}


def f(v, p):
    if len(p) > 1 and p[0] == p[-1]:
        return 1
    if len(p) > len(set(p)):
        return 0
    return sum(f(w, p + w) for w in g[v])


print(f('Ж', 'Ж'))
