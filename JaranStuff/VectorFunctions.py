from math import cos, sin, radians, atan2, degrees, sqrt, acos
from input_handler import __input_eval as enput, __input_list_eval as linput

__angles = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "NW": 135, "SE": 315, "SW": 225}


def __enter_vector(o):
    return linput(o, float)


def conv():
    s = enput("Converting from: ", str).lower()
    t = enput("To: ", str).lower()
    if s[0] == "p" and (t[0] == "u" or t[0] == "v"):
        m = enput("Magnitude: ", float)
        a = __prompta("Angle in Degrees: ")
        print("<%fi %fj>" % (m * cos(radians(a)), m * sin(radians(a))))
    if (s[0] == "v" or s[0] == "u") and t[0] == "p":
        x = enput("x=", float)
        y = enput("y=", float)
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
    print("Angle: %f" % degrees(acos(d / (mag1 * mag2))))


def __prompta(o):
    a = enput(o, str)
    try:
        return float(__angles[a.upper()])
    except:
        return float(a)


def __printv(M):
    return "<%fi + %fj + %fk>" % (M[0], M[1], M[2] if len(M) == 3 else 0)


def __find_mag(M):
    return sqrt(sum(i ** 2 for i in M))


def __to_polar(m, a):
    return [m * cos(radians(a)), m * sin(radians(a))]


def inf():
  n = enput("Number of Vectors:", int)
  t = enput("Type of Vector:", str).lower()
  c, s = 0, [0, 0, 0]
  while c < n:
    if t == "u" or t == "v":
      m = __enter_vector("Enter Vector")
    else:
      m = __to_polar(enput("Enter Mag:", float), __prompta("Enter Angle:"))
    for i in range(len(m)):
      s[i] += m[i]
    c+=1
  return __printv(m)