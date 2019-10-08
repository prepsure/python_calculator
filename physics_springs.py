from input_handler import __input_eval as enput

def work_from_velocity():
    vf = float(input("vf (m/s): "))
    vi = float(input("vi (m/s): "))
    m = float(input("mass (kg): "))

    print("W = " + str((m/2) * (vf**2 - vi**2)))

def work_from_distance():
    kx = float(input("kx: "))
    xi = float(input("xi (m): "))
    xf = float(input("xf (m): "))

    print("W = " + str((kx/2) * (xi**2 - xf**2)))