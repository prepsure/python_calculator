__evaluated_types = [
    int, float, complex, hex, oct
]

__split = " "

# out is the message right before the input, t is the type the input should be cast as
def __input_eval(out, t):
    data = input(out+"\n")
    if t in __evaluated_types:
        data = eval(data)
    return t(data)


def __input_list_eval(out, t):
    raw = input(out+":\n").split(__split)
    ret = []
    for i in range(len(raw)):
        if t in __evaluated_types:
            ret.append(t(eval(raw[i])))
        else:
            ret.append(t(raw[i]))
    return ret


def __input_list_list_eval(out1, out2, t):
  return [__input_list_eval(out1 + str(j + 1), float) for j in range(__input_eval(out2, int))]