def change_in_ke():
    mass = float(input("Enter Mass: "))
    velocity = [float(i) for i in input("Enter Velocity Vf Vi:\n").split(" ")]
    return 1/2 * mass * (velocity[0]**2 - velocity[1]**2)


def work():
    mass = float(input("Enter Mass: "))
    displacement = [float(i) for i in input("Enter Position Xi Xf:\n").split(" ")]
    return 1/2 * mass * (displacement[0]**2 - displacement[1]**2)
