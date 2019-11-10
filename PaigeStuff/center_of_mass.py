from input_handler import __input_eval as enput, __input_list_eval as linput


def __combine_com(dense = False):
    num_objs = enput("how many objects? ", int)
    objs_coords = []
    objs_mass = []

    for _ in range(0, num_objs):
        coords = linput("coordinates of object: ", float)
        if not dense:
            mass = enput("mass of object: ", float)
        else:
            volume = enput("volume of object: ", float)
            density = enput("density of object: ", float)
            mass = volume * density
        objs_coords.append(coords)
        objs_mass.append(mass)

    for coord_place in range(0, len(objs_coords[0])):
        cm = 0
        total_mass = 0
        for obj_place in range(0, len(objs_coords)):
            cm += objs_mass[obj_place] * objs_coords[obj_place][coord_place]
            total_mass += objs_mass[obj_place]
        cm /= total_mass
        print("cm: " + str(cm))


def center_of_mass():
    __combine_com()


def center_of_dense_mass():
    __combine_com(True)