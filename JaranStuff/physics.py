from input_handler import __input_eval as enput, __input_list_list_eval as listput


def work_from_velo():
    mass = enput("Enter Mass in (kg):", float)
    velocity = listput("Enter Velocity Vf Vi in (m/s):", float)
    return 1/2 * mass * (velocity[0]**2 - velocity[1]**2)


def work_from_x():
    kx = enput("Enter Spring Const:", float)
    displacement = listput("Enter Position Xi Xf in (m)", float)
    return 1/2 * kx * (displacement[0]**2 - displacement[1]**2)


def center_of_mass():
    coordinates_of_particles = listput("Enter M + coordinates of Particle", "Enter Number of Particles", float)
    cop = coordinates_of_particles.copy()
    sum_of_mass = sum(cop[i][0] for i in range(len(cop)))
    return [sum([cop[j][0] * cop[j][i] for j in range(len(cop))])/sum_of_mass for i in range(1, len(cop[0]))]

