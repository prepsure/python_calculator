from math import radians, sqrt, degrees, atan2, sin, cos


def __promptA(o):
    a = input(o)
    A = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "NW": 135, "SE": 315, "SW": 225}
    try:
        return A[a.upper()]
    except:
        return float(a)


def __enterVector(o): return [float(i) for i in input(o + ":\n").split(" ")]


def __printV(M): return "<%fi + %fj + %fk>" % (M[0], M[1], M[2] if len(M) == 3 else 0)


def __giveAngles(y, x): a = degrees(atan2(y, x));return "%f° or %f°" % (a, a + 360 if a < 0 else a - 360)


def __findMag(M): return sqrt(sum(i ** 2 for i in M))


def inf():
    O = [1, -1]
    n = int(input("Number of Vectors: "))
    t = input("Type of Vector: ").lower()
    o = O[("+-").index(input("Addition (+)\nor Subtraction (-): "))]
    i = 0
    s = [0, 0, 0]
    d = 0
    M = []
    if (t[0] == "u" or t[0] == "v"):
        while (i < n):
            M.append(__enterVector("Enter Vector"))
            d = len(M[i])
            s[0] += M[i][0] * (o if i != 0 else 1)
            s[1] += M[i][1] * (o if i != 0 else 1)
            s[2] += (M[i][2] * (o if i != 0 else 1) if len(M[i]) > 2 else 0)
            i += 1
    elif t[0] == "p":
        d = 2
        while i < n:
            m = float(input("Enter Magnitude: "))
            a = radians(float(__promptA("Enter Angle in Degrees: ")))
            s[0] += (m * cos(a)) * (o if i != 0 else 1)
            s[1] += (m * sin(a)) * (o if i != 0 else 1)
            i += 1
    else:
        print("Incorrect Vector Type")
    print("Resultant Vector:\n%s\nResultant Magnitude:\n%f\nResultant Angle:\n%s" % (
    __printV(s), __findMag(s), __giveAngles(s[1], s[0]) if d == 2 else 0))
