FROM python:3.10

WORKDIR /blur-faces

COPY blur_faces.py .

#ADD output.py ./ blur_faces.py ./ 

RUN apt-get -y update
RUN apt-get install -y --fix-missing \
    cmake \
    python3-opencv

RUN pip install opencv-python face_recognition

CMD [ "/blur_faces" ]