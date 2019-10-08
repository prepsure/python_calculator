__evaluated_types = [
    int, float, complex, hex, oct
]

# out is the message right before the input, t is the type the input should be cast as
def __input_eval(out, t):
    data = input(out)
    if t in __evaluated_types:
        data = eval(data)
    return t(data)