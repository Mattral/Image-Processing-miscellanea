from skimage import exposure
from skimage import io
from pylab import *
img = io.imread('??????.jpg')     # img file name

gamma_corrected1 = exposure.adjust_gamma(img, 0.5)
gamma_corrected2 = exposure.adjust_gamma(img, 5)

figure(0)
io.imshow(gamma_corrected1)
figure(1)
io.imshow(gamma_corrected2)