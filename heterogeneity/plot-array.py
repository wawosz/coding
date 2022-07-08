# standard imports
import numpy as np
import matplotlib.pyplot as plt

# define different arrays to plot and print in terminal

# MANUAL DEFINITION OF AN 10x10 ARRAY
# array = np.array([
#             [0,1,1,0,0,1,1,0,0,1],
#             [1,0,0,1,1,0,0,1,1,0],
#             [0,1,1,0,0,1,1,0,0,1],
#             [1,0,0,1,1,0,0,1,1,0],
#             [0,1,1,0,0,1,1,0,0,1],
#             [1,0,0,1,1,0,0,1,1,0],
#             [0,1,1,0,0,1,1,0,0,1],
#             [1,0,0,1,1,0,0,1,1,0],
#             [0,1,1,0,0,1,1,0,0,1],
#             [1,0,0,1,1,0,0,1,1,0]
#         ])

# RANDOMIZED ARRAY
# 10x10 array randomized values 0 or 1
#array = np.random.randint(2, size=(10,10))

# HOMOGENOUS WHITE
# 10x10 array filled with zeros
# b = np.array([[0,0],[0,0]])  # small array which will be repeated 5 times (tiled)
# array = np.tile(b, (5,5))

# HOMOGENOUS BLACK
# 10x10 array filled with ones (not sure why it plots empty cells but it should be filled)
#b = np.array([[1,1],[1,1]])  # small array which will be repeated 5 times (tiled)
#array = np.tile(b, (5,5))

# PATTERNED ARRAY - CHECKBOARD
# b = np.array([[0,1],[1,0]])  # small array which will be repeated 5 times (tiled)
# array = np.tile(b, (5,5))

# PATTERNED ARRAY - LINES HORIZONTAL
b = np.array([[1,1],[0,0]])  # small array which will be repeated 5 times (tiled)
array = np.tile(b, (5,5))

# PATTERNED ARRAY - LINES VERTICAL
# b = np.array([[0,1],[0,1]])  # small array which will be repeated 5 times (tiled)
# array = np.tile(b, (5,5))


# print the array in terminal
print(array)

# plot array as mesh with lines between cells
plt.pcolormesh(array, cmap='Greys', edgecolors='k', linewidth=0.5)
ax = plt.gca()
ax.set_aspect('equal')
ax.set_xticks([])  # remove x ticks
ax.set_yticks([])  # remove y ticks

plt.show()
