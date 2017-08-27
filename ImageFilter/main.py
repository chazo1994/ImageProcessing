import AverageFilter as av
im = av.LoadImage('/home/thinh/Desktop/MyProject/ImageProcessing/ImageFilter/J13Wn.jpg',5)
im.save("J13Wn_Result_Average.png")
im = av.LoadImage('/home/thinh/Desktop/MyProject/ImageProcessing/ImageFilter/got.png',5)
im.save("got_Result_Average.png")