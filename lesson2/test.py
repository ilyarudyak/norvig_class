def ints(start, end=None):
    i = start
    while i <= end or end is None:
        yield i
        i = i + 1


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    i, j = 0, 1
    flag = True
    while True:
        if flag:
            flag = False
            yield i
            i = i - 1
        else:
            flag = True
            yield j
            j = j + 1


for n in all_ints():
    if n < 10:
        print n,
    else:
        break
