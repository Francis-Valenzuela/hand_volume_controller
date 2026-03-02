import cv2
import mediapipe as mp
import pyautogui
import time

x1 = y1 = x2 = y2 = 0
prev_time = 0
cooldown = 0
webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
drawing_utils = mp.solutions.drawing_utils

