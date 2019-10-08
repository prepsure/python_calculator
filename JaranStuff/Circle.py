from math import pi, sin, radians
from input_handler import __input_eval as enput

def area():
    r = enput("Radius: ", float)
    print("Area of the Cirle is\n%f" % (pi * r ** 2))


def circumference():
    r = enput("Radius: ", float)
    print("Circumference of the Circle is\n%f" % (2 * pi * r))


def sector_area():
    r = enput("Radius: ", float)
    t = enput("Radians or Degrees: ", str).lower()
    if t[0] == "r":
        print("Sector Area is\n%f" % ((r ** 2 * __promptt(t)) / 2))
    else:
        print("Sector Area is\n%f" % (pi * (r ** 2) * (__promptt(t) / 360)))


def arc_length():
    r = enput("Radius: ", float)
    t = enput("Radians or Degrees: ", str).lower()
    if t[0] == "r":
        print("Arc length of the Circle is\n%f" % (r * __promptt(t)))
    else:
        print("Arc Length of the Circle is\n%f" % (2 * pi * r * (__promptt(t) / 360)))


def chord():
    r = enput("Radius: ", float)
    t = enput("Radians or Degrees: ", str).lower()
    if t[0] == "r":
        print("Chord Length of the Circle is\n%f" % (2 * r * sin(__promptt(t) / 2)))
    else:
        print("Chord Length of the Circle is\n%f" % (2 * r * sin(radians(__promptt(t)) / 2)))


def __promptt(z):
    if z.lower()[0] == "d":
        a = enput("Enter Angle in Degrees: ", str)
        angles = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "SE": 315, "NW": 135, "SW": 225}
        try:
            return angles[a.upper()]
        finally:
            return float(a)
    else:
        return enput("Enter in Radians: ", float)
