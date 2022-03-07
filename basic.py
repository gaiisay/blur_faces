import cv2 as cv


img = cv.imread('img/crowd.jpg')
resized = cv.resize(img, (1920, 1080), interpolation=cv.INTER_AREA)
cv.imshow('resized', resized)

#blur = cv.GaussianBlur(img, (7, 7), interpolation=cv.BORDER_DEFAULT)

#cv.imshow('blur', blur)

cv.waitKey(0)
