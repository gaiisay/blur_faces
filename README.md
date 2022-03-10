# Case-Study-Lumoview

docker build -t blur-faces .

docker run --rm -v C:\Users\IsayGa\Desktop\test:/images blur-faces python3 blur_faces.py /images/lumoview.jpg /images/crowd.jpg