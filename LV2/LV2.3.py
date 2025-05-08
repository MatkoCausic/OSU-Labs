import numpy as np
import matplotlib.pyplot as plt

# a)
# img = plt.imread('road.jpg')
# # bright_img = np.clip(img + 0.2, 0, 1) -- za RGB sliku
# bright_img = np.clip(img + 50, 0, 255).astype(np.uint8)

# plt.imshow(bright_img)
# plt.title('Posvijetljena slika')
# plt.axis('off')
# plt.show()

# b)
# img = plt.imread('road.jpg')
# height, width = img.shape[:2]
# second_quarter = img[:, width//4 : width//2]

# plt.imshow(second_quarter)
# plt.title('Druga četvrtina slike')
# plt.axis('off')
# plt.show()

# c)
# img = plt.imread('road.jpg')
# rotated_img = np.rot90(img, k=3)

# plt.imshow(rotated_img)
# plt.title('Rotirana za 90* udesno')
# plt.axis('off')
# plt.show()

# d)
img = plt.imread('road.jpg')
mirrored_img = img[:, ::-1]

plt.imshow(mirrored_img)
plt.title('Zrcaljena slika')
plt.axis('off')
plt.show()