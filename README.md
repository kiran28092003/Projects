# AI Virtual Mouse

## This Project is Done By:
- **Shinde Vrushali**  
- **Tajanpure Kiran**  
- **Bhagat Ashwini**  
- **Tarde Pooja**

---

## Project Description
The **AI Virtual Mouse** project aims to create a touchless mouse interface that allows users to control their computers using hand gestures and movements. This innovative system uses a camera to monitor hand movements and translates those movements into actions on the computer screen, such as moving the mouse pointer or clicking.

The core of this project involves:
1. **Capturing Real-Time Visuals**: Utilizing a webcam to record hand movements.  
2. **Processing Visual Data**: Using advanced computer vision techniques with libraries like OpenCV and MediaPipe to identify key landmarks on the hand (fingertips, joints, etc.).
3. **Recognizing Gestures**: Translating gestures into mouse actions, like moving the cursor or performing clicks.

---

## Key Components

### 1) Camera  
Captures real-time images or videos of the user's hand movements.  
### 2) Computer Vision  
Analyzes the captured visuals to detect and interpret hand gestures using machine learning models.  
### 3) Software  
Implements the system using programming languages like Python, alongside libraries such as OpenCV and MediaPipe.

---

## Why We Selected This Project
1. **Innovation**: Utilizes cutting-edge technologies like computer vision and AI.  
2. **Accessibility**: Provides a hands-free control system, aiding individuals who cannot use a traditional mouse.  
3. **Practical Use**: Finds applications in gaming, healthcare, and other environments where physical contact is limited.

---

## Challenges Faced
1. **Gesture Recognition Accuracy**: Achieving high precision in detecting hand gestures in different lighting conditions.  
2. **Hardware Limitations**: Ensuring the system works efficiently on devices with low processing power.  
3. **Real-time Performance**: Reducing lag between gesture input and system response.  
4. **Gesture Overlap**: Preventing confusion when similar gestures are performed consecutively.

### How We Overcame These Challenges
- Fine-tuned the gesture detection models to work in variable lighting.  
- Optimized the code to ensure smooth performance on lower-end systems.  
- Implemented gesture differentiation algorithms to avoid overlaps.

---


## Security Features
To ensure only authorized users can access the AI Virtual Mouse, several security features are included:  
- **User Authentication**: Requires login credentials before using the system.  
- **Gesture-Based Authentication**: Employs specific gestures as an additional layer of security.  
- **Access Logs**: Maintains a record of usage to monitor unauthorized access.

---

## Libraries Used
1. **NumPy**: Handles large datasets and performs numeric and scientific computations.  
2. **OpenCV (cv2)**: Processes images and videos to detect hand gestures.  
3. **MediaPipe**: Tracks hand movements in real-time, recognizing landmarks and gestures.  
4. **PyAutoGUI**: Controls the mouse and keyboard, enabling hand gestures to perform actions like moving and clicking.
5. **pyttsx3**: library converts text to speech, allowing you to set properties like voice, rate, and volume, and speak or save text as audio. 
---

## Example of Implementation
Below is an example image of how the AI Virtual Mouse works in real time:

**steps to Execute-**
- step 1)
## install all libraries:
```
pip install pyttsx3
pip install opencv-python
pip install mediapipe
pip install pyautogui
```
make sure your version of python is satisfies the libraries requirement ...we are using python 3.12
```
python --version
```
- step 2)
- 
![Screenshot (97)](https://github.com/user-attachments/assets/6f64a456-cccd-4be9-80da-73ca50f1ae6d)

- step 3)
- 
![Screenshot (93)](https://github.com/user-attachments/assets/23e7f71a-1d8c-431e-83b4-07ad8e20039f)
- step 4)
- 
![Screenshot 2025-01-01 122819](https://github.com/user-attachments/assets/285dd0cb-b049-4667-8474-7e688b33bd87)
- step 4)
- 
![Screenshot (94)](https://github.com/user-attachments/assets/f034a790-a512-4abf-9112-6f4ba0be4a94)
![Screenshot (95)](https://github.com/user-attachments/assets/dd968ad7-548d-426b-9901-43ae99bafb80)
![Screenshot (99)](https://github.com/user-attachments/assets/de8d35e5-f4b6-4725-baba-60ccf02eaf90)

This is the additional Feature GUI we added to it
---
## Applications
- **Gaming**: Hands-free control enhances gaming experiences.  
- **Healthcare**: Useful in sterile environments where touch is not allowed.  
- **Assistive Technology**: Aids individuals with physical disabilities.

---

## Contact
For inquiries, feel free to reach out to us:  
- **Email**: kirantajanpure48@gmail.com  
- **GitHub**: [https://github.com/kiran28092003](https://github.com/kiran28092003)  
- **LinkedIn**: [https://www.linkedin.com/in/kiran-tajanpure-a7509225b](https://www.linkedin.com/in/kiran-tajanpure-a7509225b)  

---

## Future Scope

1. **Gesture Expansion**  
   Introduce a wider range of gestures for advanced mouse operations, such as drag-and-drop, zooming, and scrolling.

2. **Voice Integration**  
   Combine gesture recognition with voice commands for a hybrid hands-free interface.

3. **Cross-Platform Compatibility**  
   Extend support to various operating systems like macOS, Linux, and mobile platforms.

4. **Improved Accuracy**  
   Enhance gesture recognition algorithms to work effectively in diverse lighting conditions and backgrounds.

5. **AR/VR Integration**  
   Use the AI Virtual Mouse in augmented reality (AR) and virtual reality (VR) environments for immersive user experiences.

6. **Accessibility Enhancements**  
   Adapt the system further for individuals with disabilities, making it more inclusive and accessible.

7. **Customizable UI**  
   Provide users with the ability to configure gestures and corresponding actions according to their preferences.

8. **Disaster Management Integration**  
   Utilize AI Virtual Mouse technology in disaster response scenarios, enabling hands-free control of systems for monitoring, communication, and rescue operations in hazardous environments.

---
