from input_handler import __input_eval as enput, __input_list_eval as linput, __input_list_list_eval as manput


def __enter_matrix():
    return manput("Enter Row", "Enter Number of Rows: ", float)


def cum_sum():
    m = __enter_matrix()
    a = enput("Enter Axis (0 is default): ", int)
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


def det(m=None):
    if not m:
        m = __enter_matrix()
    if len(m) == 2:
        r = m[0][0] * m[1][1] - m[0][1] * m[1][0]
        print(r)
        return r
    elif len(m) == 3:
        r = m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[2][0] * m[1][2]) + \
            m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
        print(r)
        return r


def rref():
    def rref(m):
        if not m: return
        l = 0
        rc = len(m)
        cc = len(m[0])
        for r in range(rc):
            if l >= cc:
                return
            i = r
            while m[i][l] == 0:
                i += 1
                if i == rc:
                    i = r
                    l += 1
                    if cc == l:
                        return
            m[i], m[r] = m[r], m[i]
            lv = m[r][l]
            m[r] = [mrx / float(lv) for mrx in m[r]]
            for i in range(rc):
                if i != r:
                    lv = m[i][l]
                    m[i] = [iv - lv * rv for rv, iv in zip(m[r], m[i])]
            l += 1

    m = __enter_matrix()
    rref(m)
    for rw in m:
        print(", ".join((str(rv) for rv in rw)))