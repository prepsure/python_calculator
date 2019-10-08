def work_from_velo():
    mass = float(input("Enter Mass in (kg): "))
    velocity = [float(i) for i in input("Enter Velocity Vf Vi in (m/s):\n").split(" ")]
    return 1/2 * mass * (velocity[0]**2 - velocity[1]**2)


def work_from_x():
    kx = float(input("Enter Spring Const: "))
    displacement = [float(i) for i in input("Enter Position Xi Xf in (m):\n").split(" ")]
    return 1/2 * kx * (displacement[0]**2 - displacement[1]**2)


