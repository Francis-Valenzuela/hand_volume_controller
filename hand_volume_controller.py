import cv2
import mediapipe as mp
import pyautogui
import time

x1 = y1 = x2 = y2 = 0
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

while True:
    success, img = webcam.read()
    if not success:
        break

    image = cv2.flip(img, 1)
    frame_height, frame_width, _ = img.shape
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            drawing_utils.draw_landmarks(image, hand.landmark, mp_hands.HAND_CONNECTIONS)

            landmarks = hand.landmark

            x1 = int(landmarks[8].x * frame_width)
            y1 = int(landmarks[8].y * frame_height)
            x2 = int(landmarks[4].x * frame_width)
            y2 = int(landmarks[4].y * frame_height)

            cv2.circle(image, (x1, y1),8,(0,255,255),3)
            cv2.circle(image, (x2, y2), 8, (0, 0, 255), 3)
            cv2.line(image, (x1, y1),(x2, y2), (0, 255,0), 3)

            distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

            if time.time() - cd > 0.05:
                if distance > 80:
                    pyautogui.press("volumeup")
                    cooldown = time.time()
                elif distance < 40:
                    pyautogui.press("volumedown")
                    cooldown = time.time()
    cv2.imshow("Hand Volume Control", image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
webcam.release()
cv2.destroyAllWindows()
