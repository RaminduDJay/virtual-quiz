# import cv2
# import time
# from hand_tracking import HandTracker
# from game_logic import QuizGame

# def main():
#     # Initialize game and hand tracker
#     game = QuizGame("assets/questions.json")
#     hand_tracker = HandTracker()

#     # Setup for OpenCV video capture
#     cap = cv2.VideoCapture(0)
    
#     # Variables to handle question navigation and answer selection
#     selected_answer = None
#     start_time = time.time()  # Track the start time of the current question
#     time_gap = 5  # 5 seconds for each question
    
#     while True:
#         ret, frame = cap.read()
#         if not ret:
#             break

#         # Track hand gestures in the frame
#         frame = hand_tracker.track(frame)

#         # Check for finger positions to select answers
#         finger_positions = hand_tracker.get_finger_positions(frame)

#         # If finger tip is above a certain threshold, select the option
#         if finger_positions and finger_positions[0][1] < 0.3:  # Example: Finger above 30% of the screen height
#             selected_answer = game.get_current_question()['options'][0]  # Select the first option as an example

#         # Display current question and options on the screen
#         question = game.get_current_question()
#         cv2.putText(frame, f"Question: {question['question']}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#         y_offset = 100
#         for idx, option in enumerate(question['options']):
#             cv2.putText(frame, f"{idx + 1}. {option}", (50, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
#             y_offset += 50

#         # Check if the time gap has passed
#         if time.time() - start_time >= time_gap:
#             # Move to the next question after the time gap
#             if selected_answer:
#                 game.check_answer(selected_answer)
#                 game.next_question()
            
#             # Reset the timer for the next question
#             start_time = time.time()

#         # Show score
#         cv2.putText(frame, f"Score: {game.score}", (50, y_offset + 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

#         # Check for game over condition
#         if game.is_game_over():
#             cv2.putText(frame, "Game Over!", (50, y_offset + 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        
#         # Display the frame
#         cv2.imshow("Virtual Quiz Game", frame)

#         # Close the game on pressing 'q'
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#         # Check if the game is over
#         if game.is_game_over():
#             break

#     cap.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     main()





import cv2
import time
from hand_tracking import HandTracker
from game_logic import QuizGame

def main():
    # Initialize game and hand tracker
    game = QuizGame("assets/questions.json")
    hand_tracker = HandTracker()

    # Setup for OpenCV video capture
    cap = cv2.VideoCapture(0)
    
    # Variables to handle question navigation and answer selection
    selected_answer = None
    start_time = time.time()  # Track the start time of the current question
    time_gap = 5  # 5 seconds for each question
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Track hand gestures in the frame
        frame = hand_tracker.track(frame)

        # Get the number of fingers raised by the user
        num_fingers = hand_tracker.count_fingers(frame)
        
        # Map the number of fingers to an answer choice (1 finger = first answer, etc.)
        if num_fingers > 0:  # Ensure at least one finger is raised
            if num_fingers <= len(game.get_current_question()['options']):
                selected_answer = game.get_current_question()['options'][num_fingers - 1]

        # Display current question and options on the screen
        question = game.get_current_question()
        cv2.putText(frame, f"Question: {question['question']}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        y_offset = 100
        for idx, option in enumerate(question['options']):
            cv2.putText(frame, f"{idx + 1}. {option}", (50, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            y_offset += 50

        # Check if the time gap has passed
        if time.time() - start_time >= time_gap:
            # Move to the next question after the time gap
            if selected_answer:
                game.check_answer(selected_answer)
                game.next_question()
            
            # Reset the timer for the next question
            start_time = time.time()

        # Show score
        cv2.putText(frame, f"Score: {game.score}", (50, y_offset + 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        # Check for game over condition
        if game.is_game_over():
            cv2.putText(frame, "Game Over!", (50, y_offset + 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)
        
        # Display the frame
        cv2.imshow("Virtual Quiz Game", frame)

        # Close the game on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Check if the game is over
        if game.is_game_over():
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
