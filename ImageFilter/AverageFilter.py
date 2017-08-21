from PIL import Image
import numpy as np
def LoadImage(url, filterSize):
    #with numpy array [i,j,k] k: r,g,b,s; i,j: axist of image
    mImage = np.asarray(Image.open(url))
    applyFilter(mImage, filterSize)

def applyFilter(mImage, filterSize):
    #print(mImage[100,105,2])
    red=mImage[:,:,0]
    green=mImage[:,:,1]
    blue=mImage[:,:,2]
    print(red.shape)
    print(np.size(red[:,1]))
    print(np.size(red[1,:]))
    im = Image.fromarray(red)
    im = Image.fromarray(green)
    im = Image.fromarray(blue)
    filter(red, filterSize)
    print("done")

def filter(mColor, filterSize):
    print("color")
    xlength = np.size(mColor[:,1])
    ylength = np.size(mColor[1,:])
    rangesize = int(filterSize/2)
    print(rangesize)
    for i in range(0, xlength):
        for j in range(0, ylength):