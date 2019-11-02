from input_handler import __input_eval as enput, __input_list_list_eval as listput


def work_from_velo():
    mass = float(input("Enter Mass in (kg): "))
    velocity = [float(i) for i in input("Enter Velocity Vf Vi in (m/s):\n").split(" ")]
    return 1/2 * mass * (velocity[0]**2 - velocity[1]**2)


def work_from_x():
    kx = float(input("Enter Spring Const: "))
    displacement = [float(i) for i in input("Enter Position Xi Xf in (m):\n").split(" ")]
    return 1/2 * kx * (displacement[0]**2 - displacement[1]**2)


def center_of_mass():
    coordinates_of_particles = listput("Enter M + coordinates of Particle", "Enter Number of Particles", float)
    cop = coordinates_of_particles.copy()
    sum_of_mass = sum(cop[i][0] for i in range(len(cop)))
    return [sum([cop[j][0] * cop[j][i] for j in range(len(cop))])/sum_of_mass for i in range(1,len(cop[0]))]


