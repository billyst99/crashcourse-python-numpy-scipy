import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import sys
from PIL import Image

#For each pixel in the image, it calculates the mean value of its RGB values
#And that pixel is assigned to that value
def grayscaleConvertion(img):
	heigthAndWidth = img.shape
	for i in range (heigthAndWidth[0]):
		for j in range(heigthAndWidth[1]):
			img[i][j][:]= (img[i][j][0] + img[i][j][1] + img[i][j][2])/3
	return img


argumentsList = (sys.argv) #The list of arguments that we pass on the program

arg1 = argumentsList[1]
arg2 =argumentsList[2]
arg3 = argumentsList[3]

imageToOpen =arg1 #The image we take as an input, which is the second argument

img = np.array(Image.open(imageToOpen).convert('RGB'))
#Opening the image as an RGB image
#The case of an RGB image() is covered with convert() function above

#If the input image in a Grayscale image, it is converted to RGB and again to grayscale with
#grayscaleConvertion() function bellow

heigthAndWidth = img.shape #An array that contains the heigth and the width of the image

img = grayscaleConvertion(img)

threshold = int (arg3) #The threshold that is given by the user

for i in range (heigthAndWidth[0]):
	for j in range (heigthAndWidth[1]): 
		if (img[i][j][0]) > threshold:
			img[i][j][:] = 255 #For each pixel, we check its colour and if it is above the threshold
		else:				   #it is converted to a black pixel
			img[i][j][:] = 0   #In any other case, it becomes a white pixel

outputFile = arg2
Image.fromarray(img).save(outputFile) #The saving of the image to an output file