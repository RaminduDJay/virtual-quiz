# import cv2
# import mediapipe as mp

# class HandTracker:
#     def __init__(self):
#         self.mp_hands = mp.solutions.hands
#         self.hands = self.mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
#         self.mp_draw = mp.solutions.drawing_utils

#     def track(self, frame):
#         # Convert BGR to RGB
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(rgb_frame)
        
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 self.mp_draw.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
#         return frame

#     def get_finger_positions(self, frame):
#         # Extract finger positions (e.g., tip of index finger)
#         rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         results = self.hands.process(rgb_frame)
        
#         finger_positions = []
#         if results.multi_hand_landmarks:
#             for hand_landmarks in results.multi_hand_landmarks:
#                 # Finger tip positions (index finger, middle finger, etc.)
#                 finger_positions = [
#                     (hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].x,
#                      hand_landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y)
#                 ]
#         return finger_positions



import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
        self.mp_draw = mp.solutions.drawing_utils

    def track(self, frame):
        # Convert the frame to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        # Draw landmarks and connections if hands are detected
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, landmarks, self.mp_hands.HAND_CONNECTIONS)

        return frame

    def count_fingers(self, frame):
        # Count fingers based on hand landmarks
        fingers = 0
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                # Access landmarks using 'landmark' and check finger tips
                if landmarks.landmark[self.mp_hands.HandLandmark.THUMB_TIP].y < landmarks.landmark[self.mp_hands.HandLandmark.THUMB_IP].y:
                    fingers += 1
                if landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks.landmark[self.mp_hands.HandLandmark.INDEX_FINGER_DIP].y:
                    fingers += 1
                if landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks.landmark[self.mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y:
                    fingers += 1
                if landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks.landmark[self.mp_hands.HandLandmark.RING_FINGER_DIP].y:
                    fingers += 1
                if landmarks.landmark[self.mp_hands.HandLandmark.PINKY_TIP].y < landmarks.landmark[self.mp_hands.HandLandmark.PINKY_DIP].y:
                    fingers += 1

        return fingers
