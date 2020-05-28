import matplotlib.pyplot as plt
import numpy as np
from skimage.feature import greycomatrix

# VARIOUS TESTING 5x5 ARRAYS

# A: array (5x5) with random values 1 - 8 as float

simulated_image = 1 + (8 * np.random.rand(5, 5))
# array values changed to integer for GLCM conversion and analysis
A = simulated_image.astype(np.int16)

# B: array (5x5) with predefined values 1 - 8
B = np.array([[1, 1, 5, 6, 8],
              [2, 3, 5, 7, 1],
              [4, 5, 7, 1, 2],
              [8, 5, 1, 2, 5],
              [8, 3, 1, 5, 2]])

# C: array (5x5) with checkboard pattern
C = np.array([[0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0],
              [1, 0, 1, 0, 1],
              [0, 1, 0, 1, 0]])

# D: array (5x5) with 5 identical rows 0 - 4
D = np.array([[0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4],
              [0, 1, 2, 3, 4]])

# E: array (5x5) filled with zeros
E = np.array([[0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0]])

# which array to use? A, B, C, D, or E?
while True:
    print("A: Array 5x5 with random values 1-8")
    print("B: Array 5x5 with predefined values 1-8")
    print("C: Array 5x5 with checkboard pattern")
    print("D: Array 5x5 with 5 identical rows")
    print("E: Array 5x5 filled with zeros")
    choice = input('Which array to use (A, B, C, D, or E)?  ')

    if choice == 'A':
        test = A
        txt = "A: Array 5x5 with random values 1-8"
        break
    elif choice == 'B':
        test = B
        txt = "B: Array 5x5 with predefined values 1-8"
        break
    elif choice == 'C':
        test = C
        txt = "C: Array 5x5 with checkboard pattern"
        break
    elif choice == 'D':
        test = D
        txt = "D: Array 5x5 with 5 identical rows"
        break
    elif choice == 'E':
        test = E
        txt = "E: Array 5x5 filled with zeros"
        break
    else:
        print("Wrong value has been entered...")
        print()
        print()

print(txt)
print(test)
print()

# convert sample homogenous tumor image to gray level values
glcm = greycomatrix(test, [1], [0], 256)  # it creates 256x256 array
print("Dimensions of GLCM array")
print(glcm.shape)  # print array dimension
print()

sliced_glcm = glcm[:10, :10, 0, 0]  # we do not need all 256x256 array
print("GLCM array reduced to 10x10 array")
print(sliced_glcm)  # print sliced glcm array
print()

# plot representative figures
plt.figure(1)
plt.imshow(test, cmap='gray', interpolation='nearest')
plt.title('Original image for \n' + txt)
plt.colorbar()

plt.figure(2)
plt.imshow(sliced_glcm, cmap='gray', interpolation='nearest')
plt.title('GLCM image for \n' + txt)
plt.colorbar()

plt.show()
