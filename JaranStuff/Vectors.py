from math import radians, sqrt, degrees, atan2, sin, cos


def __prompta(o):
    a = input(o)
    A = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "NW": 135, "SE": 315, "SW": 225}
    try:
        return A[a.upper()]
    except:
        return float(a)


def __enter_vector(o):
    return [float(i) for i in input(o + ":\n").split(" ")]


def __printv(m):
    return "<%fi + %fj + %fk>" % (m[0], m[1], m[2] if len(m) == 3 else 0)


def __give_angles(y, x):
    a = degrees(atan2(y, x))
    return "%f° or %f°" % (a, a + 360 if a < 0 else a - 360)


def __find_mag(m):
    return sqrt(sum(i ** 2 for i in m))


def inf():
    operators = [1, -1]
    n = int(input("Number of Vectors: "))
    t = input("Type of Vector: ").lower()
    o = operators["+-".index(input("Addition (+)\nor Subtraction (-): "))]
    i = 0
    s = [0, 0, 0]
    d = 0
    m = []
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
            m = float(input("Enter Magnitude: "))
            a = radians(float(__prompta("Enter Angle in Degrees: ")))
            s[0] += (m * cos(a)) * (o if i != 0 else 1)
            s[1] += (m * sin(a)) * (o if i != 0 else 1)
            i += 1
    else:
        print("Incorrect Vector Type")
    print("Resultant Vector:\n%s\nResultant Magnitude:\n%f\nResultant Angle:\n%s" % (
    __printv(s), __find_mag(s), __give_angles(s[1], s[0]) if d == 2 else 0))
