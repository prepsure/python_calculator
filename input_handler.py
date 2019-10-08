__evaluated_types = [
    int, float, complex, hex, oct
]

# out is the message right before the input, t is the type the input should be cast as
def __input_eval(out, t):
    data = input(out)
    if t in __evaluated_types:
        data = eval(data)
    return t(data)


def __input_list_eval(out, t, s):
    raw = input(out+":\n").split(s)
    ret = []
    for i in range(len(raw)):
        if t in __evaluated_types:
            ret.append(t(eval(raw[i])))
        else:
            ret.append(t(raw[i]))
    return ret