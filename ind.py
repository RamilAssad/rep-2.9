def alg(value, data):
    if len(data) > 1:
        return
    for i in range(1, int(value**0.5) + 1):
        res = value - i * i
        if res > 0:
            alg(res, data + [i])
        elif res == 0:
            print(' + '.join(f'{j} * {j}' for j in data + [i]), '=', sum(j * j for j in data + [i]))

alg(int(input('введите число')), [])