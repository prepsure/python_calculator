from math import pi, radians, degrees, cos, sin, atan2, sqrt

def __enter_vector():
    print("press 1 for unit vector\n2 for mag and direction")
    choice = input("press 1 for unit vector\n2 for mag and direction:\n")
    if choice == "1":
        return __enter_unit_vector()
    else:
        return __enter_mag_and_angle()

def __enter_unit_vector():
    vector = []
    for n in input("enter vector: ").split(","):
        vector.append(float(n))
    return vector

def __enter_mag_and_angle():
    angle = float(input("enter angle: "))
    mag = float(input("enter magnitude: "))

    if angle >= 2 * pi or angle <= -2 * pi:
        angle = radians(angle)
        print("assuming degrees")
    else:
        print("assuming radians")

    return [mag * cos(angle), mag * sin(angle)]

def to_unit():
    return __enter_mag_and_angle()

def to_mag_and_direction():
    v = __enter_unit_vector()
    angle = atan2(v[1], v[0])

    print("angle:\n  " + str(degrees(angle)) + " deg\n  " + str(angle) + " rad")
    print("magnitude: " + str(sqrt(v[0]**2 + v[1]**2)))

def cross():
    v1 = __enter_unit_vector()
    v2 = __enter_unit_vector()

    crossed = [v1[1] * v2[2] - v1[2] * v2[1], v1[2] * v2[0] - v1[0] * v2[2], v1[0] * v2[1] - v1[1] * v2[0]]
    
    print(crossed)

def dot():
    v1 = __enter_unit_vector()
    v2 = __enter_unit_vector()

    dotted = sum(v1[i] * v2[i] for i in range(max(len(v1), len(v2))))

    print(dotted)