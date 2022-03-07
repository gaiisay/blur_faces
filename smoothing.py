import cv2 as cv
from numpy import median

img = cv.imread('img/crowd.jpg')
resized = cv.resize(img, (1920, 1080), interpolation=cv.INTER_AREA)

cv.imshow('resized', resized)

# Averaging
average = cv.blur(resized, (9, 9))
cv.imshow('average', average)

# GaussianBlur
gaussian = cv.GaussianBlur(resized, (9, 9), 0)
cv.imshow('gaussian', gaussian)

# MedianBlur
median = cv.medianBlur(resized, 9)
cv.imshow('median', median)

# BilateralBlur
bilateral = cv.bilateralFilter(resized, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
