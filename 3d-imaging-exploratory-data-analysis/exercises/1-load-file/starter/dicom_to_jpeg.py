import pydicom
import numpy as np
from PIL import Image
import os
import matplotlib.pyplot as plt

# TASK: In the same folder as this .py file you will find a DICOM file
# that is called instance.dcm. Your goal is to save it as a png file. 
# You must apply a WW/WC transform in order to map values to grayscale.

# 1. Use pydicom's dcmread method to load the image

# <YOUR CODE HERE>

# 2. Apply WW/WC transform. Keep in mind that pixels are available as 
# NumPy array by accessing .pixel_array field.
# You might want to display the image to check that it comes out right.
# You can use matplotlib's plt.imshow method to display image as 
# grayscale data like so: plt.imshow(pixels, cmap="gray")

# <YOUR CODE HERE>

# 3. You can use PIL's Image.fromarray and .save methods to save a NumPy array as png
# Don't forget that when you are using "L" mode, PIL is expecting your data to 
# be of type uint8 (and in the range of 0-255)

# <YOUR CODE HERE>