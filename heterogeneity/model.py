# CREATING AN ARRAY MODEL FOR HETEROGENEITY ANALYSIS
import numpy as np
import matplotlib.pyplot as plt

image = np.random.rand(100, 100)
plt.imshow(image, cmap=plt.cm.hot)
plt.colorbar()
plt.show()