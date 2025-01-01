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

## Are We Able to Alter This Code?
Yes, the code is modular and easy to modify. Developers can:
1. **Add New Gestures**: Expand the system by defining new gestures for specific actions.  
2. **Integrate Additional Features**: Include functionalities like voice commands or keyboard emulation.  
3. **Improve Performance**: Enhance detection speed by optimizing model parameters.  
4. **Adapt for Different Environments**: Adjust the code for gaming, healthcare, or other specific use cases.

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
##use
```
pip install pyttsx3
pip install opencv-python
pip install mediapipe
pip install pyautogui
```
---

## Example of Implementation
Below is an example image of how the AI Virtual Mouse works in real time:

![AI Virtual Mouse Demo](path_or_url_to_image)

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
