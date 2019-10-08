from math import pi, sin, radians


def Area():
    r = float(input("Radius: "))
    print("Area of the Cirle is\n%f" % (pi * r ** 2))


def Circum():
    r = float(input("Radius: "))
    print("Circumference of the Circle is\n%f" % (2 * pi * r))


def SectorArea():
    r = float(input("Radius: "))
    t = input("Radians or Degrees: ").lower()
    if t[0] == "r":
        print("Sector Area is\n%f" % ((r ** 2 * __promptT(t)) / 2))
    else:
        print("Sector Area is\n%f" % ((pi) * (r ** 2) * (__promptT(t) / 360)))


def ArcLength():
    r = float(input("Radius: "))
    t = input("Radians or Degrees: ").lower()
    if t[0] == "r":
        print("Arc length of the Circle is\n%f" % (r * __promptT(t)))
    else:
        print("Arc Length of the Circle is\n%f" % (2 * (pi) * (r) * (__promptT(t) / 360)))


def Chord():
    r = float(input("Radius: "))
    t = input("Radians or Degrees: ").lower()
    if t[0] == "r":
        print("Chord Length of the Circle is\n%f" % (2 * r * sin(__promptT(t) / 2)))
    else:
        print("Chord Length of the Circle is\n%f" % (2 * r * sin(radians(__promptT(t)) / 2)))


def __promptT(Z):
    if (Z.lower()[0] == "d"):
        a = input("Enter Angle in Degrees: ")
        angles = {"N": 90, "S": 270, "E": 0, "W": 180, "NE": 45, "SE": 315, "NW": 135, "SW": 225}
        try:
            return angles[a.upper()]
        except:
            return float(a)
    else:
        return float(input("Enter in Radians: "))
