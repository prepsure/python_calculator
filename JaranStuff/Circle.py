from math import pi, sin, radians


def area():
    r = float(input("Radius: "))
    print("Area of the Cirle is\n%f" % (pi * r ** 2))


def circumference():
    r = float(input("Radius: "))
    print("Circumference of the Circle is\n%f" % (2 * pi * r))


def sector_area():
    r = float(input("Radius: "))
    t = input("Radians or Degrees: ").lower()
    if t[0] == "r":
        print("Sector Area is\n%f" % ((r ** 2 * __promptt(t)) / 2))
    else:
        print("Sector Area is\n%f" % (pi * (r ** 2) * (__promptt(t) / 360)))


def arc_length():
    r = float(input("Radius: "))
    t = input("Radians or Degrees: ").lower()
    if t[0] == "r":
        print("Arc length of the Circle is\n%f" % (r * __promptt(t)))
    else:
        print("Arc Length of the Circle is\n%f" % (2 * pi * r * (__promptt(t) / 360)))


def chord():
    r = float(input("Radius: "))
    t = input("Radians or Degrees: ").lower()
    if t[0] == "r":
        print("Chord Length of the Circle is\n%f" % (2 * r * sin(__promptt(t) / 2)))
    else:
        print("Chord Length of the Circle is\n%f" % (2 * r * sin(radians(__promptt(t)) / 2)))


def __promptt(z):
    if z.lower()[0] == "d":
        a = input("Enter Angle in Degrees: ")
        angles = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "SE": 315, "NW": 135, "SW": 225}
        try:
            return angles[a.upper()]
        finally:
            return float(a)
    else:
        return float(input("Enter in Radians: "))
