evaluated_types = [
    int, float, complex, hex, oct
]

# out is the message right before the input, t is the type the input should be cast as
def __input_eval(out, t):
    raw = input(out)
    out = raw
    if t in evaluated_types:
        out = eval(out)
    return t(out)