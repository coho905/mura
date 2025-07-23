import cv2
import pygame
import numpy as np

ASCII_CHARS = "@%#*+=-:. "
FONT_SIZE = 8
CAM_WIDTH, CAM_HEIGHT = 640, 480
CHAR_WIDTH, CHAR_HEIGHT = FONT_SIZE, FONT_SIZE
GRID_COLS = CAM_WIDTH // CHAR_WIDTH
GRID_ROWS = CAM_HEIGHT // CHAR_HEIGHT

pygame.init()
screen = pygame.display.set_mode((CAM_WIDTH, CAM_HEIGHT))
font = pygame.font.SysFont("Courier", FONT_SIZE, bold=False)
cap = cv2.VideoCapture(0)

def brightness_to_char(val):
    scale = int(val / 256 * len(ASCII_CHARS))
    return ASCII_CHARS[min(scale, len(ASCII_CHARS) - 1)]

running = True
while running:
    screen.fill((0, 0, 0))
    ret, frame = cap.read()
    if not ret:
        break

    # Resize and grayscale
    small = cv2.resize(frame, (GRID_COLS, GRID_ROWS))
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

    for y in range(GRID_ROWS):
        for x in range(GRID_COLS):
            pixel_val = gray[y, x]
            char = brightness_to_char(pixel_val)
            color = (pixel_val, pixel_val, pixel_val)
            text = font.render(char, True, color)
            screen.blit(text, (x * CHAR_WIDTH, y * CHAR_HEIGHT))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
cap.release()
cv2.destroyAllWindows()