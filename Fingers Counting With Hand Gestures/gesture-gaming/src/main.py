import cv2
from hand_detector import HandDetector
from game_controller import GameController

def main():
    # Initialize the hand detector and game controller
    hand_detector = HandDetector()
    game_controller = GameController()

    # Start video capture
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Process the frame to find hands and get the gesture
        hands = hand_detector.find_hands(frame)
        gesture = hand_detector.get_gesture(hands)

        # Control the game based on the detected gesture
        if gesture == 1:
            game_controller.jump()
        elif gesture == 2:
            game_controller.roll()
        elif gesture == 3:
            game_controller.move_right()
        elif gesture == 4:
            game_controller.move_left()

        # Display the frame
        cv2.imshow("Gesture Controlled Gaming", frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()