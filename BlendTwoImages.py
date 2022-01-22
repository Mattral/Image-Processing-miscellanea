#import required packages
import cv2
#Read image 1
img1 = cv2.imread('?????.jpg')    #first image's file name & format
#Read image 2
img2 = cv2.imread('?????.jpg')    #2nd image's file name & format
#Define alpha and beta
alpha = 0.30
beta = 0.70
#Blend images
final_image = cv2.addWeighted(img1, alpha, img2, beta, 0.0)
#Show image
io.imshow(final_image)