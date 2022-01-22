#structural similarity is used to find the index that indicate how much two images are similar 
# A value closer to one means the images are very similar; a value closer to zero means they are less similar

from skimage import io
from skimage.measure import compare_ssim as ssim
img_original = io.imread('???.jpg')           #first image's file name & format
img_modified = io.imread('?????.jpg')         #2nd image's file name & format

ssim_original = ssim(img_original, img_original, data_range=img_original.max() - img_original.min(), multichannel=True)
ssim_different = ssim(img_original, img_modified, data_range=img_modified.max() - img_modified.min(), multichannel=True)

print(ssim_original,ssim_different)

