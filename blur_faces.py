import sys
import cv2
import face_recognition

inputArgs = sys.argv
images = []

for path in inputArgs[1:]:
    images.append(path)


def blur_faces(imgPath):
    image = face_recognition.load_image_file(imgPath)
    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:
        top, right, bottom, left = face_location

        face_image = image[top:bottom, left:right]
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        image[top:bottom, left:right] = face_image

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    index = imagePath.index('.')
    cv2.imwrite(f'{imgPath[:index]}_blurred_faces.jpg', image)


for imagePath in images:
    blur_faces(imagePath)
