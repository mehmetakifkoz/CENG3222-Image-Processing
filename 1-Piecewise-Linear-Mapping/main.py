# piecewiseLinearMapping by Mehmet Akif KOZ 192010020023

from turtle import numinput
import cv2 as cv
import numpy as np

def f(x, slope, vertical, horizontal):
    """
        x          --> input
        slope      --> slope of the line
        vertical   --> the shift on the y axis
        horizontal --> the shift on the x axis
    """
    return slope*(x-horizontal) + vertical

def piecewiseLinearMapping(im1, A, B, S1, S2):
    im2 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
    row = im1.shape[0]
    col = im1.shape[1]
    im3 = np.zeros((row,col),np.uint8) # unit8 --> 8 bits

    # if (color scale < A)
    im3 = np.where(
          im2 < A,
          f(x=im2, slope=S1/A, vertical=0, horizontal=0),
          im3)
    # if (color scale is between A and B)
    im3 = np.where(
          np.logical_and(A <= im2, im2 < B),
          f(x=im2, slope=(S2-S1)/(B-A), vertical=S1, horizontal=A),
          im3)
    # if (B <= color scale)
    im3 = np.where(B <= im2,
          f(x=im2, slope=(255-S2)/(255-B), vertical=S2, horizontal=B),
          im3)

    return im3
    
                                        # default values are applied if 
                                        # the user does not enter any input
inImg= input("inImg = ") or "Image.png" # inImg = "Image.png"
A = int(input("A  = ") or "100")        # A = 100
B = int(input("B  = ") or "150")        # B = 150
S1= int(input("S1 = ") or "50")         # S1= 50
S2= int(input("S2 = ") or "200")        # S2= 200

im1 = cv.imread(inImg)
im2 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
im3 = piecewiseLinearMapping(im1, A, B, S1, S2)
cv.imwrite('Grayscale.png',im2)
cv.imwrite('Mapped.png',im3)
