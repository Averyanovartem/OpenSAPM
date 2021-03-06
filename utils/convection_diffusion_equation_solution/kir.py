import numpy as np
"""Use numpy arrays and lists"""

def kir(x_nods_quantity, grid, transfer_velocity, time_step, x_step):
    new_grid = grid
    sigma = transfer_velocity* time_step / x_step
    for m in range(1, x_nods_quantity - 1):
        if (transfer_velocity >= 0):
            new_grid[m] = grid[m] - np.dot(sigma, (grid[m] - grid[m-1]))
            continue
        else:
            new_grid[m] = grid[m] - np.dot(sigma, (grid[m+1] - grid[m]))
    return new_grid[1:-1]
