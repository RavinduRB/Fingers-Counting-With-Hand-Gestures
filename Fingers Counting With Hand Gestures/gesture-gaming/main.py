import cv2
import mediapipe as mp
import pyautogui
import time

class HandDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)
        
        if self.results.multi_hand_landmarks:
            for hand_landmarks in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
        return img

    def count_fingers(self):
        fingers = 0
        if self.results.multi_hand_landmarks:
            hand = self.results.multi_hand_landmarks[0]
            tips = [8, 12, 16, 20]  # finger tip ids
            
            # Thumb
            if hand.landmark[4].y < hand.landmark[3].y:
                fingers += 1
                
            # Other fingers
            for tip in tips:
                if hand.landmark[tip].y < hand.landmark[tip-2].y:
                    fingers += 1
        return fingers

def main():
    # Initialize
    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    
    # Game controls mapping
    controls = {
        1: 'space',    # Jump
        2: 'down',     # Roll
        3: 'right',    # Move right
        4: 'left'      # Move left
    }
    
    # Cooldown to prevent rapid-fire inputs
    last_action_time = 0
    cooldown = 0.5  # seconds
    
    while True:
        # Get frame
        success, img = cap.read()
        if not success:
            break
            
        # Flip image for mirror effect
        img = cv2.flip(img, 1)
        
        # Find hands and count fingers
        img = detector.find_hands(img)
        finger_count = detector.count_fingers()
        
        # Execute game action with cooldown
        current_time = time.time()
        if current_time - last_action_time >= cooldown:
            if finger_count in controls:
                pyautogui.press(controls[finger_count])
                last_action_time = current_time
        
        # Display info on screen
        cv2.putText(img, f'Fingers: {finger_count}', (10, 70), 
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        
        # Show image
        cv2.imshow("Gesture Gaming", img)
        
        # Exit on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()