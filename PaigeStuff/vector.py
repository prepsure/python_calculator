from math import pi, radians, degrees, cos, sin, acos, atan2, sqrt
from input_handler import __input_eval as enput, __input_list_eval as linput


def __enter_unit_vector():
    return linput("enter vector: ", float)


def __enter_polar():
    angle = enput("enter angle: ", float)
    if angle - 0.01 >= 2 * pi or angle + 0.01 <= -2 * pi: # comparing floats with an accuracy of 0.01
        angle = radians(angle)
        print("assuming degrees")
    else:
        print("assuming radians")

    mag = enput("enter magnitude: ", float)

    return [mag * cos(angle), mag * sin(angle)]


def __enter_vector():
    choice = input("press 1 for a unit vector\n      2 for a polar vector\n")
    if choice == "1":
        return __enter_unit_vector()
    else:
        return __enter_polar()


def __get_mag(v):
    return sqrt(sum(i ** 2 for i in v))


def to_unit():
    print(__enter_polar())


def to_mag_and_direction():
    v = __enter_unit_vector()
    angle = atan2(v[1], v[0]) # angle as radians

    print("angle:\n  " + str(degrees(angle)) + " deg\n  " + str(angle) + " rad")
    print("magnitude: " + str(__get_mag(v)))


def cross():
    v1 = __enter_vector()
    v2 = __enter_vector()

    for v in [v1, v2]:
        while len(v) < 3:
            v.append(0)

    crossed = [v1[1] * v2[2] - v1[2] * v2[1],
               v1[2] * v2[0] - v1[0] * v2[2],
               v1[0] * v2[1] - v1[1] * v2[0]]
    
    print(crossed)


def __get_dot(v1, v2):
    return sum(v1[i] * v2[i] for i in range(max(len(v1), len(v2))))


def dot():
    v1 = __enter_vector()
    v2 = __enter_vector()
    print(__get_dot(v1, v2))


def angle_between():
    v1 = __enter_vector()
    v2 = __enter_vector()
    dot = __get_dot(v1, v2)
    angle = acos(dot/(__get_mag(v1) * __get_mag(v2)))
    print("in radians: " + str(angle))
    print("in degrees: " + str(degrees(angle)))


def add_vectors():
    v1 = __enter_vector()
    v2 = __enter_vector()

    vf = [v1[0] + v2[0], v1[1] + v2[1]]

    angle = atan2(vf[1], vf[0]) # angle as radians

    print("angle:\n  " + str(degrees(angle)) + " deg\n  " + str(angle) + " rad")
    print("magnitude: " + str(sqrt(vf[0]**2 + vf[1]**2)))