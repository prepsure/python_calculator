from math import ceil


def euler_step(dy_dx, initial_x, initial_y, steps, delta_x=0.00001, silent = False):
    """
    Performs `steps` steps of Euler's Method, starting at (`initial_x`, 
    `initial_y`). `dy_dx` is a function that takes 2 arguments, `x` and `y`. 
    `delta_x` is the step size for x. `silent` controls whether the intermediate
    steps are printed. The final value of `y` is returned. 

    Example: Given dy/dx = 2y, y(0) = 1/2, do 5 steps of Euler's method
    ```
    euler_step(lambda x,y: 2*y, 0, 0.5, 5, 0.1)
    ```
    """
    x = initial_x
    y = initial_y
    if not silent: print("x, y, dy/dx, deltaY, new y")
    for _ in range(steps):
        dy_dx_at_x = dy_dx(x, y)
        delta_y = dy_dx_at_x * delta_x
        new_y = y + delta_y
        if not silent: print([x, y, dy_dx_at_x, delta_y, new_y])
        x += delta_x
        y += delta_y
    if not silent: print([x,y])
    return y


def euler(dy_dx, initial_x, initial_y, final_x, delta_x=0.00001, silent = False):
    """
    Like euler_step, but continues Euler's method until `final_x` is reached. 

    Example: Given dy/dx = 2y, y(0) = 1/2, estimate y(1/2)
    ```
    euler(lambda x,y: 2*y, 0, 0.5, 0.5, 0.1)
    ```
    """
    return euler_step(dy_dx, initial_x, initial_y, ceil((final_x - initial_x) / delta_x), delta_x, silent)
