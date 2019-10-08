__evaluated_types = [
    int, float, complex, hex, oct
]

__splitter = ","

def __eval_that(string, t):
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
    data = []
    for n in input(out).split(__splitter):
        data.append(__eval_that(n, t))
    return data

# out1 is the message right before the input for the amount of repetitions
# out2 is the message right before the input for each repetition
# t is the type the inputs should be cast as
'''
def __input_multidimensional(out1, out2, t):
    data = []

    for 

    return data
'''