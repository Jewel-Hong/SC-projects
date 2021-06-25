def code():
    sc = [0]
    if sc[0]:
        print('1', sc.pop())
    else:
        print('2', sc.pop(0))
    print('3', sc)

    cs = 1
    mystery(sc, cs)


def mystery(cs, sc):
    if cs:
        print('4', cs)
    else:
        print('5', cs)


if __name__ == '__main__':
    code()
