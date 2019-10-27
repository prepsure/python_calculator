__evaluated_types = [
    int, float, complex, hex, oct
]

__splitter = ","

def __eval_that(data, t):
    if t in __evaluated_types:
        data = eval(data)
    return t(data)

# out is the message right before the input
# t is the type the inputs should be cast as
def __input_eval(out, t):
    return __eval_that(input(out), t)

# out is the message right before the input for each repetition
# t is the type the inputs should be cast as
def __input_list(out, t):
    given_list = []
    for n in input(out).split(__splitter):
        given_list.append(__eval_that(n, t))
    return given_list