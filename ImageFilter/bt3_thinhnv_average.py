from PIL import Image
import numpy as np
def LoadImage(url, filterSize):
    #with numpy array [i,j,k] k: r,g,b,s; i,j: axist of image
    mImage = np.asarray(Image.open(url).convert('RGBA'))
    print (mImage.shape)
    image = applyFilter(mImage, filterSize)
    return image

def applyFilter(mImage, filterSize):
    #print(mImage[100,105,2])
    red=mImage[:,:,0]
    green=mImage[:,:,1]
    blue=mImage[:,:,2]
    print(red.shape)
    im = Image.fromarray(red)
    im = Image.fromarray(green)
    im = Image.fromarray(blue)
    nred = filter(red, filterSize)
    ngreen = filter(green, filterSize)
    nblue = filter(blue, filterSize)
    nImage = np.empty_like(mImage);
    nImage[:,:,0] = nred;
    nImage[:,:,1] = ngreen;
    nImage[:,:,2] = nblue;
    nImage[:,:,3] = mImage[:,:,3]
    img = Image.fromarray(nImage)
    img.show()
    return img
def filter(mColor, filterSize):
    xlength = np.size(mColor[:,1])
    ylength = np.size(mColor[1,:])
    rangesize = int(filterSize/2)
    nMatrix = np.zeros((xlength,ylength), dtype=mColor.dtype)
    print "range size: ",rangesize
    sub = mColor[0:5,0:5]
    for i in range(0,xlength):
        for j in range(0, ylength):
            if (i < rangesize):
                if j < rangesize:
                    xsize = i + 1 + rangesize
                    ysize = j + 1 + rangesize
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[0:xsize, 0:ysize]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
                elif j > (ylength - rangesize - 1):
                    xsize = i + 1 + rangesize
                    ysize = ylength - j + rangesize
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[0:xsize, (j-rangesize):ylength]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
                else:
                    xsize = i + 1 + rangesize
                    ysize = rangesize*2 + 1
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[0:xsize, (j - rangesize):(j + rangesize + 1)]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
            elif i > (xlength - rangesize - 1):
                if j < rangesize:
                    xsize = xlength - i + rangesize
                    ysize = j + 1 + rangesize
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[(i-rangesize):xlength, 0:ysize]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
                elif j > (ylength - rangesize - 1):
                    xsize = xlength - i + rangesize
                    ysize = ylength - j + rangesize
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[(i-rangesize):xlength, (j-rangesize):ylength]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
                else:
                    xsize = xlength - i + rangesize
                    ysize = rangesize*2 + 1
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[i - rangesize:xlength, (j - rangesize):(j + rangesize + 1)]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
            else:
                if j < rangesize:
                    xsize = rangesize*2 + 1
                    ysize = j + 1 + rangesize
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[(i-rangesize):(i+rangesize + 1), 0:ysize]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
                elif j > (ylength - rangesize - 1):
                    xsize = rangesize*2 + 1
                    ysize = ylength - j + rangesize
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[(i-rangesize):(i+rangesize + 1), (j-rangesize):ylength]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
                else:
                    xsize = rangesize*2 + 1
                    ysize = rangesize*2 + 1
                    num = xsize * ysize
                    win = np.full((xsize, ysize), 1)
                    sub = mColor[(i-rangesize):(i+rangesize + 1), (j - rangesize):(j + rangesize + 1)]
                    average = convMatrix(win, sub)
                    nMatrix[i,j] = average/num
    return nMatrix

def convMatrix(m1, m2):
    if m1.shape != m2.shape:
        print "two matrix must be same size m1: ",m1.shape," m2: ",m2.shape
    else:
        xlength = np.size(m1[:,1])
        ylength = np.size(m1[1,:])
        total = 0
        for i in range(0, xlength):
            for j in range(0, ylength):
                num1 = m1[i,j]
                num2 = m2[i,j]
                mul = num1*num2
                total = total + mul
        return total

if __name__ == "__main__":
    im = LoadImage('/home/thinh/Desktop/MyProject/ImageProcessing/ImageFilter/J13Wn.jpg', 5)
    im.save("J13Wn_Result_Average.png")
