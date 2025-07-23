import pygame
import cv2
from draw import engine
from hand_detection import hand_detection
from emotions import facial_recognition

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
cap = cv2.VideoCapture(0)

drawing_engine = engine(WIDTH, HEIGHT)
finger_count = 0
emotion = facial_recognition()
hand = hand_detection()

running = True
while running:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    screen.fill((0, 0, 0))

    dominant_emotion, secondary_emotion = emotion.analyze(frame)
    finger_count = hand.detect(frame)
    #print(finger_count)
    drawing_engine.update_and_draw(screen, frame, finger_count, dominant_emotion, secondary_emotion)

    cv2.imshow('Video Feed', frame)

    pygame.display.flip()
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if cv2.waitKey(1) & 0xFF == ord('q'):
        running = False

pygame.quit()
cap.release()
cv2.destroyAllWindows()
