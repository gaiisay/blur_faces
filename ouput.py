import sys
import cv2
import blur_faces

inputArgs = sys.argv
images = []

for path in inputArgs[1:]:
    images.append(path)

for imagePath in images:
    blur_faces(imagePath)
