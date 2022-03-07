import cv2 as cv

img = cv.imread('img/lumoview.jpg')
cv.imshow('Lumview', img)


cv.waitKey(0)
