import random
import pygame
import cv2

EMOTION_COLOR_MAP = {
    'happy': (255, 190, 130),
    'neutral': (99, 142, 168),
    'sad': (72, 159, 212),
    'angry': (150, 3, 8),
    'surprised': (255, 255, 120),
    'fear': (163, 33, 133),
    'disgust': (39, 110, 84),
    'None': (69, 85, 102)
}

ASCII_CHARS = "@%#*+=-:. "
FONT_SIZE = 10  # Increased from 8 to 16

class engine:
    def __init__(self, width, height, font_size=FONT_SIZE):
        self.width = width
        self.height = height
        self.font_size = font_size
        self.char_w = font_size
        self.char_h = font_size
        self.grid_cols = self.width // self.char_w
        self.grid_rows = self.height // self.char_h
        self.font = pygame.font.SysFont("Courier", self.font_size, bold=False)

    def brightness_to_char(self, val):
        idx = int(val / 256 * len(ASCII_CHARS))
        return ASCII_CHARS[min(idx, len(ASCII_CHARS) - 1)]

    def update_and_draw(self, screen, frame, finger_count, dominant_emotion='None', secondary_emotion='None'):
        primary_color = EMOTION_COLOR_MAP.get(dominant_emotion, EMOTION_COLOR_MAP['None'])
        secondary_color = EMOTION_COLOR_MAP.get(secondary_emotion, EMOTION_COLOR_MAP['None'])
        noise = 0.05 * finger_count  # Reduced pixel-level chaos

        small = cv2.resize(frame, (self.grid_cols, self.grid_rows))
        gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

        for y in range(self.grid_rows):
            for x in range(self.grid_cols):
                pixel_val = gray[y, x]
                char = self.brightness_to_char(pixel_val)

                dx = random.uniform(-noise, noise) * self.char_w
                dy = random.uniform(-noise, noise) * self.char_h

                if random.random() < 0.7:
                    base_color = primary_color
                else:
                    base_color = secondary_color

                color = tuple(min(255, max(0, c + random.randint(-5, 5))) for c in base_color)
                text = self.font.render(char, True, color)
                screen.blit(text, (x * self.char_w + dx, y * self.char_h + dy))
