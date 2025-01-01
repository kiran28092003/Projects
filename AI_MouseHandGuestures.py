import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import pyttsx3
import time


class VirtualMouse:
    def __init__(self, camera_width=1280, camera_height=720, speed_factor=2):
        self.camera_width = camera_width
        self.camera_height = camera_height
        self.speed_factor = speed_factor
        self.screen_width, self.screen_height = pyautogui.size()

        # Gesture flags
        self.left_click_gesture = False
        self.right_click_gesture = False
        self.scroll_gesture = False
        self.mouse_movement_gesture = False
        self.double_click_gesture = False
        self.last_click_time = 0

        # Initialize MediaPipe and speech engine
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)
        self.engine = pyttsx3.init()

        # Camera setup
        self.cap = cv2.VideoCapture(0)

    def speak(self, text):
        """ Function to speak text using pyttsx3 """
        self.engine.say(text)
        self.engine.runAndWait()

    def process_gestures(self, hand_landmarks):
        """ Function to process gestures from hand landmarks """
        finger_coords = np.array([[l.x * self.camera_width, l.y * self.camera_height] for l in hand_landmarks.landmark])
        wrist_coords = np.array([hand_landmarks.landmark[0].x * self.camera_width, hand_landmarks.landmark[0].y * self.camera_height])

        # Thumb movement for mouse movement
        thumb_coords = finger_coords[4]
        if thumb_coords[0] < wrist_coords[0] - 50:  # Adjust the threshold for thumb movement
            self.mouse_movement_gesture = True
        else:
            self.mouse_movement_gesture = False

        # Left click gesture
        if finger_coords[8][1] < finger_coords[6][1] and finger_coords[12][1] > finger_coords[10][1]:
            self.left_click_gesture = True
        else:
            self.left_click_gesture = False

        # Right click gesture
        if np.linalg.norm(finger_coords[4] - finger_coords[8]) < 40 and all(np.linalg.norm(finger_coords[i] - wrist_coords) > 40 for i in range(1, 5)):
            self.right_click_gesture = True
        else:
            self.right_click_gesture = False

        # Double click gesture
        if np.linalg.norm(finger_coords[8] - finger_coords[12]) < 40:
            if time.time() - self.last_click_time < 0.3:
                self.double_click_gesture = True
            self.last_click_time = time.time()
        else:
            self.double_click_gesture = False

        # Scroll gesture
        if finger_coords[16][1] > finger_coords[14][1]:
            self.scroll_gesture = True
        else:
            self.scroll_gesture = False

    def perform_actions(self):
        """ Perform mouse actions based on recognized gestures """
        if self.left_click_gesture:
            pyautogui.click()

        if self.right_click_gesture:
            pyautogui.click(button='right')

        if self.double_click_gesture:
            pyautogui.doubleClick()

        if self.scroll_gesture:
            pyautogui.scroll(10)  # Scroll down

    def move_mouse(self, thumb_coords):
        """ Move the mouse based on thumb coordinates """
        new_x = max(0, min(thumb_coords[0] * self.speed_factor, self.screen_width - 1))
        new_y = max(0, min(thumb_coords[1] * self.speed_factor, self.screen_height - 1))
        pyautogui.moveTo(new_x, new_y)

    def process_frame(self, image):
        """ Process each frame to detect gestures and perform actions """
        display_image = cv2.flip(image, 1)
        image_rgb = cv2.cvtColor(display_image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(display_image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                self.process_gestures(hand_landmarks)

                # Thumb coordinates for mouse movement
                thumb_coords = np.array([hand_landmarks.landmark[4].x * self.camera_width, hand_landmarks.landmark[4].y * self.camera_height])

                # Perform actions based on gestures
                self.perform_actions()

                # Move the mouse
                if self.mouse_movement_gesture:
                    self.move_mouse(thumb_coords)

                # Draw circles on hand landmarks for visualization
                finger_coords = np.array([[l.x * self.camera_width, l.y * self.camera_height] for l in hand_landmarks.landmark])
                cv2.circle(display_image, tuple(np.array([finger_coords[8][0], finger_coords[8][1]]).astype(int)), 10, (255, 0, 0), -1)  # Blue color
                cv2.circle(display_image, tuple(np.array([finger_coords[12][0], finger_coords[12][1]]).astype(int)), 10, (255, 0, 0), -1)  # Blue color
                cv2.circle(display_image, tuple(np.array([finger_coords[4][0], finger_coords[4][1]]).astype(int)), 10, (255, 192, 203), -1)  # Pink color
                cv2.circle(display_image, tuple(np.array([finger_coords[16][0], finger_coords[16][1]]).astype(int)), 10, (0, 255, 0), -1)  # Green color

        return display_image

    def run(self):
        """ Main loop to run the Virtual Mouse """
        self.speak("Press Esc key to exit the program.")
        
        while self.cap.isOpened():
            success, image = self.cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            display_image = self.process_frame(image)

            cv2.imshow('Virtual Mouse', display_image)

            if cv2.waitKey(1) & 0xFF == 27:  # Exit if 'Esc' key is pressed
                break

        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    virtual_mouse = VirtualMouse()
    virtual_mouse.run()
