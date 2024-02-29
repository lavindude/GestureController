import cv2
import pyautogui
import mediapipe as mp
from mediapipe.tasks.python import vision

screen_width, screen_height = pyautogui.size() # of primary monitor, more complex for multiple monitors**
cycle_count = [0]
current_gesture_state = [""]
def process_result(result: mp.tasks.vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    # print('gesture recognition result: {}'.format(result))

    if len(result.hand_landmarks) > 0:
        x_norm = result.hand_landmarks[0][0].x
        y_norm = result.hand_landmarks[0][0].y

        # math to figure out coordinates to move mouse to on screen
        x_img = x_norm * output_image.width
        y_img = y_norm * output_image.height

        x = screen_width / output_image.width * x_img
        y = screen_height / output_image.height * y_img

        if cycle_count[0] % 4 == 0:
            pyautogui.moveTo(-x, y)

        cycle_count[0] += 1

    if len(result.gestures) > 0:
        gesture = result.gestures[0][0].category_name
        if current_gesture_state[0] != gesture: # indicates a change in state
            if current_gesture_state[0] == "Open_Palm" and (gesture == "Closed_Fist" or gesture == "None"):
                pyautogui.click()

            current_gesture_state[0] = gesture

# Load the gesture recognizer model
options = mp.tasks.vision.GestureRecognizerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path='models/gesture_recognizer.task'),
    running_mode=mp.tasks.vision.RunningMode.LIVE_STREAM,
    result_callback=process_result)

gesture_recognizer = vision.GestureRecognizer.create_from_options(options)

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read frame from webcam
    ret, frame = cap.read()

    if not ret:
        break

    # Process the frame with the gesture recognizer model
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    timestamp = int(cv2.getTickCount())
    gesture_recognizer.recognize_async(mp_image, timestamp)

    # Display the frame
    cv2.imshow('Gesture Recognition', frame)

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
