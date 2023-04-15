import numpy as np
import matplotlib.pyplot as plt

# Define camera parameters
xo, yo, zo = 0, 0, 0
xe, ye, ze = 10, 10, 10
f = 5

# Define object parameters
vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

# Define image plane
image_plane = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]])

# Project vertices onto image plane
vertex_list = []
for vertex in vertices:
    # Transform vertex to camera coordinate system
    x = vertex[0] - xe
    y = vertex[1] - ye
    z = vertex[2] - ze
    x_prime = x
    y_prime = y * np.cos(np.arctan2(x, f)) + z * np.sin(np.arctan2(x, f))
    z_prime = -y * np.sin(np.arctan2(x, f)) + z * np.cos(np.arctan2(x, f)) - f

    # Transform vertex to image coordinate system
    u = f * x_prime / z_prime
    v = f * y_prime / z_prime

    # Scale and shift vertex to fit image plane
    u_scaled = (u + 1) * 128
    v_scaled = (v + 1) * 128
    vertex_list.append([u_scaled, v_scaled])

# Plot projected edges on image plane
fig, ax = plt.subplots()
for edge in edges:
    start_vertex = vertex_list[edge[0]]
    end_vertex = vertex_list[edge[1]]
    ax.plot([start_vertex[0], end_vertex[0]], [start_vertex[1], end_vertex[1]], color='black')

# Display image
ax.imshow(np.zeros((256, 256)), cmap='gray')
plt.show()
