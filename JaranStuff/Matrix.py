def __enterMatrix():
    return [[float(i) for i in input("Enter Row " + str(j + 1) + ": ").split(" ")] for j in
            range(int(input("Enter Number of Rows: ")))]


def cumsum():
    m = __enterMatrix()
    a = int(input("Enter Axis (0 is default): "))
    r = 0
    for i in range(len(m)):
        if a != 0 and i % a == 0:
            r = 0
        else:
            r = r
        for j in range(len(m[i])):
            r += m[i][j]
            m[i][j] = r
    print(m)


def det():
    m = __enterMatrix()
    if len(m) == 2:
        r = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        print(r)
    elif len(m) == 3:
        r = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[2][0] * m[1][2]) + \
            m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        print(r)


def rref():
    def rref(M):
        if not M: return
        l = 0
        rC = len(M)
        cC = len(M[0])
        for r in range(rC):
            if l >= cC:
                return
            i = r
            while M[i][l] == 0:
                i += 1
                if i == rC:
                    i = r
                    l += 1
                    if cC == l:
                        return
            M[i], M[r] = M[r], M[i]
            lv = M[r][l]
            M[r] = [mrx / float(lv) for mrx in M[r]]
            for i in range(rC):
                if i != r:
                    lv = M[i][l]
                    M[i] = [iv - lv * rv for rv, iv in zip(M[r], M[i])]
            l += 1

    m = __enterMatrix()
    rref(m)
    for rw in m:
        print((", ").join((str(rv) for rv in rw)))