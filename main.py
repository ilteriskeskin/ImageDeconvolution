import numpy as np
import matplotlib.pyplot as plt

from skimage import color, restoration, io
from scipy.signal import convolve2d as conv2

img = io.imread('images/sabiha-gokcen.jpg')
img = color.rgb2gray(img)

psf = np.ones((5, 5)) / 25
img = conv2(img, psf, 'same')
img += 0.1 * img.std() * np.random.standard_normal(img.shape)

deconvolved, _ = restoration.unsupervised_wiener(img, psf)

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5),
                       sharex=True, sharey=True)

plt.gray()

ax[0].imshow(img, vmin=deconvolved.min(), vmax=deconvolved.max())
ax[0].axis('off')
ax[0].set_title('Data')

ax[1].imshow(deconvolved)
ax[1].axis('off')
ax[1].set_title('Self tuned restoration')

fig.tight_layout()

plt.show()
