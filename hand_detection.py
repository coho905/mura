import cv2 as cv
import numpy as np
import mediapipe as mp
class hand_detection:
    def __init__(self):
        self.hand_cascade = cv.CascadeClassifier('./right_hand.xml')
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
        self.mp_drawing = mp.solutions.drawing_utils

        
    def detect(self, img):
        if img is not None:
            return self.count_fingers(img)
        return 0
    
    def count_fingers(self, hand_img):
        img_rgb = cv.cvtColor(hand_img, cv.COLOR_BGR2RGB)
        results = self.hands.process(img_rgb)

        if not results.multi_hand_landmarks:
            return 0

        hand_landmarks = results.multi_hand_landmarks[0]
        lm = hand_landmarks.landmark

        tip_ids = [4, 8, 12, 16, 20]
        fingers = []

        if lm[tip_ids[0]].x < lm[tip_ids[0] - 1].x:
            fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1, 5):
            if lm[tip_ids[id]].y < lm[tip_ids[id] - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
        return sum(fingers)