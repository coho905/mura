import cv2 as cv
from deepface import DeepFace

class facial_recognition:
    def __init__(self):
        self.face_find = cv.CascadeClassifier('./haar_cascade.xml')

    def analyze(self, img):
        face_img = None
        face = self.face_find.detectMultiScale(img)

        for(x, y, w, h) in face:
            face_img = img[y:y+h, x:x+w]

        
        if face_img is not None:
            result = DeepFace.analyze(face_img, actions=['emotion'], enforce_detection=False)
            emotions = result[0]['emotion']
            sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
            primary_emotion = sorted_emotions[0][0]
            secondary_emotion = sorted_emotions[1][0]
            #print(primary_emotion, secondary_emotion)
            return primary_emotion, secondary_emotion
        
        return None, None
