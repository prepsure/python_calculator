from math import cos, sin, radians, atan2, degrees, sqrt, acos


def __enter_vector(o):
    return [float(i) for i in input(o + ":\n").split(" ")]


def conv():
    s = input("Converting from: ").lower()
    t = input("To: ").lower()
    if s[0] == "p" and (t[0] == "u" or t[0] == "v"):
        m = float(input("Magnitude: "))
        a = float(__prompta("Angle in Degrees: "))
        print("<%fi %fj>" % (m * cos(radians(a)), m * sin(radians(a))))
    if (s[0] == "v" or s[0] == "u") and t[0] == "p":
        x = float(input("x="))
        y = float(input("y="))
        a = atan2(y, x)
        M = y / sin(a) if x == 0 else x / cos(a)
        print("Magnitude=%f\nAngle=%f" % (M, degrees(a)))


def dot(m1=None, m2=None):
    if not m1 and not m2:
        m1 = __enter_vector("Enter First Vector")
        m2 = __enter_vector("Enter Second Vector")
    return sum(m1[i] * m2[i] for i in range(max(len(m1), len(m2))))


def cross():
    m1 = __enter_vector("Enter First Vector")
    m2 = __enter_vector("Enter Second Vector")
    m3 = [m1[1] * m2[2] - m1[2] * m2[1], m1[2] * m2[0] - m1[0] * m2[2], m1[0] * m2[1] - m1[1] * m2[0]]
    print(__printv(m3))


def angle(m1=None, m2=None):
    if not m1 and not m2:
        m1 = __enter_vector("Enter First Vector")
        m2 = __enter_vector("Enter Second Vector")
    mag1 = __find_mag(m1)
    mag2 = __find_mag(m2)
    d = dot(m1, m2)
    return degrees(acos((d) / (mag1 * mag2)))


def __prompta(o):
    a = input(o)
    angles = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "NW": 135, "SE": 315, "SW": 225}
    try:
        return angles[a.upper()]
    except:
        return float(a)


def __printv(M):
    return "<%fi + %fj + %fk>" % (M[0], M[1], M[2] if len(M) == 3 else 0)


def __give_angles(y, x):
    a = degrees(atan2(y, x))
    return "%f° or %f°" % (a, a + 360 if a < 0 else a - 360)


def __find_mag(M):
    return sqrt(sum(i ** 2 for i in M))
