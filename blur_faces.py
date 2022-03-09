import cv2
import face_recognition


def blur_faces(imgPath):
    image = face_recognition.load_image_file(imgPath)
    face_locations = face_recognition.face_locations(image)

    for face_location in face_locations:
        top, right, bottom, left = face_location

        face_image = image[top:bottom, left:right]
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        image[top:bottom, left:right] = face_image

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    cv2.imwrite(f'{imgPath}_blurred_faces.jpg', image)
