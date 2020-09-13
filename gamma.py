import numpy as np
import matplotlib.pylab as plt
import sys
import cv2 as cv
import matplotlib.image as img
'''
def gammaTransform(i, factor):
    f = (i + 0.5) / 255
    f = np.power(f, factor)
    v = int(f * 255.0 - 0.5)
    return v

srcImage = plt.imread('balance.jpg')
width = srcImage.shape[0]
height = srcImage.shape[1]
channel = srcImage.shape[2]
resultImage = np.zeros((width, height, channel), dtype=np.uint8)

width = srcImage.shape[0]
height = srcImage.shape[1]

gamma = 2.2
factor = 1 / gamma

for x in range(0, width-1):
    for y in range(0, height-1):
        resultImage[x, y, 0] = gammaTransform(srcImage[x, y, 0],factor)
        resultImage[x, y, 1] = gammaTransform(srcImage[x, y, 1],factor)
        resultImage[x, y, 2] = gammaTransform(srcImage[x, y, 2],factor)

img.imsave("res1.jpg", resultImage)
'''

def gammaTransform(srcImage, factor):
    gammaLUT = np.zeros(256, float)
    width = srcImage.shape[0]
    height = srcImage.shape[1]
    channel = srcImage.shape[2]
    for i in range(0, 255):
        f = (i + 0.5) / 255
        c = np.power(f, factor)
        v = int(c * 255.0 - 0.5)
        gammaLUT[i] = v
    resultImage = np.zeros((width, height, channel), np.uint8)
    print(gammaLUT)
    for x in range(0, width - 1):
        for y in range(0, height - 1):
            resultImage[x, y, 0] = gammaLUT[srcImage[x, y, 0]]
            resultImage[x, y, 1] = gammaLUT[srcImage[x, y, 1]]
            resultImage[x, y, 2] = gammaLUT[srcImage[x, y, 2]]
    return resultImage

srcImage = img.imread('balance.jpg')
gamma = 1.8
factor = 1 / gamma
result = gammaTransform(srcImage, factor)
img.imsave("res1.jpg", result)