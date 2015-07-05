import itertools


B = 9
S = 4
types = ["be", "bf", "se", "sf", "b->s", "s->b"]
states = {(b, s): i for (b, s), i in
          zip(itertools.product(range(10), range(5)), range(50))}
path = [0, 45, 29, 25, 9, 5, 1, 46, 34]


def convert_path():
    st = [(b, s) for (b, s) in itertools.product(range(10), range(5))]
    # print st
    return [st[x] for x in path]


def adj((b0, s0), (b1, s1)):
    if (b0, s0) == (b1, s1):
        return False
    for type in types:
        if trans((b0, s0), type) == (b1, s1):
            return True
    return False


def graph_file():
    f = open('graph_water', 'wr')
    f.write(str(len(states)) + "\n")
    for s0 in states.keys():
        for s1 in states.keys():
            if adj(s0, s1):
                f.write(str(states[s0]) + " " +
                        str(states[s1]) + "\n")


def trans((b, s), type):

    if type == "be":
        return (0, s)
    elif type == "bf":
        return (B, s)
    elif type == "se":
        return (b, 0)
    elif type == "sf":
        return (b, S)
    elif type == "b->s":
        if b < S - s:
            return (0, s + b)
        else:
            return (b - (S - s), S)
    elif type == "s->b":
        if s < B - b:
            return (b + s, 0)
        else:
            return (B, s - (B - b))


def main():
    # graph_file()
    # print states
    print convert_path()


if __name__ == '__main__':
    main()
