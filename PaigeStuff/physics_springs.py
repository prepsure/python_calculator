from input_handler import __input_eval as enput


def work_from_velocity():
    vf = enput("vf (m/s): ", float)
    vi = enput("vi (m/s): ", float)
    m = enput("mass (kg): ", float)

    print("W = " + str((m/2) * (vf**2 - vi**2)))


def work_from_distance():
    kx = enput("kx: ", float)
    xi = enput("xi (m): ", float)
    xf = enput("xf (m): ", float)

    print("W = " + str((kx/2) * (xi**2 - xf**2)))