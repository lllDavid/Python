import numpy as np
from numba import cuda
import matplotlib.pyplot as plt
from math import sqrt

G = 6.67430e-11  
DT = 0.01       
SOFTENING = 1e-9

@cuda.jit
def compute_forces(pos, vel, mass, N):
    i = cuda.grid(1)
    if i < N:
        fx = 0.0
        fy = 0.0
        for j in range(N):
            if i != j:
                dx = pos[j, 0] - pos[i, 0]
                dy = pos[j, 1] - pos[i, 1]
                dist_sqr = dx**2 + dy**2 + SOFTENING
                inv_dist = 1.0 / sqrt(dist_sqr) 
                inv_dist3 = inv_dist**3

                f = G * mass[i] * mass[j] * inv_dist3
                fx += f * dx
                fy += f * dy

        vel[i, 0] += fx / mass[i] * DT
        vel[i, 1] += fy / mass[i] * DT

@cuda.jit
def update_positions(pos, vel, N):
    i = cuda.grid(1)
    if i < N:
        pos[i, 0] += vel[i, 0] * DT
        pos[i, 1] += vel[i, 1] * DT

N = 512
pos = np.random.rand(N, 2).astype(np.float32) * 100.0 
vel = np.zeros((N, 2), dtype=np.float32)               
mass = np.ones(N, dtype=np.float32) * 1e3             

d_pos = cuda.to_device(pos)
d_vel = cuda.to_device(vel)
d_mass = cuda.to_device(mass)

threads_per_block = 128
blocks_per_grid = (N + threads_per_block - 1) // threads_per_block

for step in range(500):
    compute_forces[blocks_per_grid, threads_per_block](d_pos, d_vel, d_mass, N)
    update_positions[blocks_per_grid, threads_per_block](d_pos, d_vel, N)

pos = d_pos.copy_to_host()

plt.scatter(pos[:, 0], pos[:, 1], s=1)
plt.title('GPU Particle Simulation (Gravity)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.show()