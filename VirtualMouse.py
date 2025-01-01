import tkinter as tk
from tkinter import messagebox, simpledialog
import cv2
import numpy as np
import mediapipe as mp
import pyautogui
import pyttsx3
import time
import re


class VirtualMouse:
    def __init__(self, password="123"):
        self.PASSWORD = password
        self.virtual_mouse_on = False
        self.last_click_time = 0

        # Mediapipe initialization
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=1)

        self.screen_width, self.screen_height = pyautogui.size()
        self.camera_width, self.camera_height = 1280, 720

    def start_program(self):
        self.virtual_mouse_on = True
        cap = cv2.VideoCapture(0)
        engine = pyttsx3.init()
        engine.say("Starting the virtual mouse program. Press Esc to exit.")
        engine.runAndWait()

        while cap.isOpened() and self.virtual_mouse_on:
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            display_image = cv2.flip(image, 1)
            image_rgb = cv2.cvtColor(display_image, cv2.COLOR_BGR2RGB)
            results = self.hands.process(image_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(display_image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                    self.process_gestures(hand_landmarks)

            cv2.imshow('Virtual Mouse', display_image)

            if cv2.waitKey(1) & 0xFF == 27:  # Exit if 'Esc' key is pressed
                break

        cap.release()
        cv2.destroyAllWindows()

    def process_gestures(self, hand_landmarks):
        finger_coords = np.array([[l.x * self.camera_width, l.y * self.camera_height] for l in hand_landmarks.landmark])
        wrist_coords = np.array([hand_landmarks.landmark[0].x * self.camera_width, hand_landmarks.landmark[0].y * self.camera_height])

        thumb_coords = finger_coords[4]

        left_click_gesture = finger_coords[8][1] < finger_coords[6][1] and finger_coords[12][1] > finger_coords[10][1]
        right_click_gesture = np.linalg.norm(finger_coords[4] - finger_coords[8]) < 40 and all(
            np.linalg.norm(finger_coords[i] - wrist_coords) > 40 for i in range(1, 5))
        double_click_gesture = np.linalg.norm(finger_coords[8] - finger_coords[12]) < 40 and time.time() - self.last_click_time < 0.3
        scroll_gesture = finger_coords[16][1] > finger_coords[14][1]
        mouse_movement_gesture = thumb_coords[0] < wrist_coords[0] - 50

        self.last_click_time = time.time() if double_click_gesture else self.last_click_time

        # Perform actions
        if left_click_gesture:
            pyautogui.click()
        if right_click_gesture:
            pyautogui.click(button='right')
        if double_click_gesture:
            pyautogui.doubleClick()
        if scroll_gesture:
            pyautogui.scroll(10)
        if mouse_movement_gesture:
            new_x = max(0, min(thumb_coords[0], self.screen_width - 1))
            new_y = max(0, min(thumb_coords[1], self.screen_height - 1))
            pyautogui.moveTo(new_x, new_y)


class VirtualMouseGUI:
    def __init__(self):
        self.virtual_mouse = VirtualMouse()
        self.root = tk.Tk()
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Virtual Mouse Control")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg='lightblue')

        self.name_label = tk.Label(self.root, text="Name:", bg='lightblue')
        self.name_label.pack(pady=(10, 0))
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password:", bg='lightblue')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=(0, 10))

        self.start_btn = tk.Button(self.root, text="Start Virtual Mouse", command=self.start_virtual_mouse)
        self.start_btn.pack(pady=10)

        self.exit_btn = tk.Button(self.root, text="Exit", command=self.exit_program)
        self.exit_btn.pack(pady=10)

        self.label = tk.Label(self.root, text="", bg='lightblue')
        self.label.pack()

    def start_virtual_mouse(self):
        name = self.name_entry.get()
        password = self.password_entry.get()

        if not self.validate_name(name):
            messagebox.showwarning("Invalid Name", "Please input a valid name.")
            return

        if name.lower() == "kiran" and password == self.virtual_mouse.PASSWORD:
            result = messagebox.askquestion("Confirmation", "Welcome Madam, do you want to turn on the virtual mouse program?")
            if result == 'yes':
                self.countdown(3)
                self.virtual_mouse.start_program()
            else:
                feedback = simpledialog.askstring("Feedback", "Please provide feedback:")
                if feedback:
                    messagebox.showinfo("Thank You", "Thank you for your feedback!")
                else:
                    messagebox.showinfo("Information", "No feedback provided.")

                self.root.quit()
        else:
            messagebox.showwarning("Invalid User", "You are not authorized to use this program.")

    def countdown(self, count):
        self.label.config(text=f"Starting in {count} seconds...")
        if count > 0:
            self.root.after(1000, self.countdown, count - 1)
        else:
            self.label.config(text="")
            self.root.update()

    @staticmethod
    def validate_name(name):
        pattern = r'^[a-zA-Z ]+$'
        return bool(re.match(pattern, name))

    def exit_program(self):
        feedback = simpledialog.askstring("Feedback", "Please provide feedback:")
        if feedback:
            messagebox.showinfo("Thank You", "Thank you for your feedback!")
        else:
            messagebox.showinfo("Information", "No feedback provided.")
        self.root.quit()

    def run(self):
        self.root.mainloop()


class VirtualMouseApp:
    def __init__(self):
        self.gui = VirtualMouseGUI()

    def start(self):
        self.gui.run()


if __name__ == "__main__":
    app = VirtualMouseApp()
    app.start()
