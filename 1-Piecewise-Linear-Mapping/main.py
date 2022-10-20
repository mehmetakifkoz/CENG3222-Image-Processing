# piecewiseLinearMapping by Mehmet Akif KOZ 192010020023

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
    im3 = np.zeros((row,col),np.uint8)
    for i in range(row):
        for j in range(col):
            if im2[i, j] < A:
                im3[i, j] = f(x=im2[i, j], slope=S1/A,
                              vertical=0, horizontal=0);
            if A <= im2[i, j] < B:
                im3[i, j] = f(x=im2[i, j], slope=(S2-S1)/(B-A),
                              vertical=S1, horizontal=A);
            if B <= im2[i, j]:
                im3[i, j] = f(x=im2[i, j], slope=(255-S2)/(255-B),
                              vertical=S2, horizontal=B);
    return im3
       
im1 = cv.imread('image.jpg')
im2 = cv.cvtColor(im1, cv.COLOR_BGR2GRAY)
A = int(input("A  = "))
B = int(input("B  = "))
S1= int(input("S1 = "))
S2= int(input("S2 = "))
im3 = piecewiseLinearMapping(im1, A, B, S1, S2)
cv.imshow('Mapped image',im3)
cv.imshow('image',im2)
cv.waitKey(0)
cv.destroyAllWindows()
