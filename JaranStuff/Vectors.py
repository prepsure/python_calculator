from math import radians, sqrt, degrees, atan2, sin, cos, acos
from input_handler import __input_eval as enput, __input_list_eval as linput
"""
DEPRECATED
NOT IN USE
"""

def __prompta(o):
    a = enput(o, str)
    angles = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "NW": 135, "SE": 315, "SW": 225}
    try:
        return float(angles[a.upper()])
    except:
        return float(eval(a))


def __enter_vector(o):
    return linput(o, float)


def __printv(m):
    return "<%fi + %fj + %fk>" % (m[0], m[1], m[2] if len(m) == 3 else 0)


def __give_angles(x, y, z, d):
    if d == 2:
        a = degrees(atan2(y, x))
        return "%f° or %f°" % (a, a + 360 if a < 0 else a - 360)
    else:
        mag = __find_mag([x, y, z])
        ax = degrees(acos(x/mag))
        ay = degrees(acos(y/mag))
        az = degrees(acos(z/mag))
    return "%f°(i), %f°(j), %f°(k)" % (ax, ay, az)


def __find_mag(m):
    return sqrt(sum(i ** 2 for i in m))


def inf():
    operators = [1, -1]
    n = enput("Number of Vectors: ", int)
    t = enput("Type of Vector: ", str).lower()
    o = operators["+-".index(enput("Addition (+)\nor Subtraction (-): ", str))]
    i, s, d, m = 0, [0, 0, 0], 0, []
    if t[0] == "u" or t[0] == "v":
        while i < n:
            m.append(__enter_vector("Enter Vector"))
            d = len(m[i])
            s[0] += m[i][0] * (o if i != 0 else 1)
            s[1] += m[i][1] * (o if i != 0 else 1)
            s[2] += (m[i][2] * (o if i != 0 else 1) if len(m[i]) > 2 else 0)
            i += 1
    elif t[0] == "p":
        d = 2
        while i < n:
            m = enput("Enter Magnitude: ", float)
            a = radians(__prompta("Enter Angle in Degrees: "))
            s[0] += (m * cos(a)) * (o if i != 0 else 1)
            s[1] += (m * sin(a)) * (o if i != 0 else 1)
            i += 1
    else:
        print("Incorrect Vector Type")
    print("Resultant Vector:\n%s\nResultant Magnitude:\n%f\nResultant Angle:\n%s" % (__printv(s),
                                                                                     __find_mag(s),
                                                                                     __give_angles(s[0], s[1], s[2], d))
          )
