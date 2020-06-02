import numpy as np
import matplotlib.pyplot as plt

def display_image_from_array(img_coords, dimensions:tuple):
    x = np.array(img_coords).reshape(dimensions)
    plt.imshow(x, cmap='gray')
    plt.show()