import cv2
import mediapipe as mp

mp_face_detection = mp.solutions.mediapipe.python.solutions.face_detection
mp_drawing = mp.solutions.mediapipe.python.solutions.drawing_utils
face_detection = mp_face_detection.FaceDetection(model_selection=1)


img = cv2.imread('img/lumoview.jpg')
results = face_detection.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

img = cv2.resize(img, (1920, 1080))


for detection in results.detections:
    mp_drawing.draw_detection(img, detection)


cv2.imshow('lumoview faces', img)


cv2.waitKey(0)
