import numpy as np
import matplotlib.pyplot as plt

height, width = 50, 50
black = np.zeros([height, width], dtype=bool)
white = np.ones([height, width], dtype=bool)

top_row = np.hstack((black, white))
bottom_row = np.hstack((white, black))

checkerboard = np.vstack((top_row, bottom_row))

plt.imshow(checkerboard, cmap='gray')
plt.axis('off')
plt.show()