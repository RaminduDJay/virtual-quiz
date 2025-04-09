import cv2
from hand_tracking import HandTracker
from game_logic import QuizManager
from src.ui import QuizUI

def main():
    # Initialize components
    tracker = HandTracker()
    quiz_manager = QuizManager("data/questions.json")
    ui = QuizUI(quiz_manager)

    # Start webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot access the camera")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Cannot read frame from camera")
            break
        
        # Process frame for hand tracking
        gesture, landmarks = tracker.detect_gesture(frame)
        
        # Update quiz state based on gesture
        if gesture:
            quiz_manager.update_state(gesture)
        
        # Render the quiz UI
        frame = ui.render(frame, gesture, landmarks)
        cv2.imshow("Virtual Quiz Game", frame)

        # Break on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
