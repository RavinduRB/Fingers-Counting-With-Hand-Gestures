class HandDetector:
    def __init__(self, static_image_mode=False, max_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        import cv2
        import mediapipe as mp
        
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(static_image_mode=static_image_mode,
                                         max_num_hands=max_hands,
                                         min_detection_confidence=min_detection_confidence,
                                         min_tracking_confidence=min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_hands(self, image, draw=True):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(image, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
        return image, results.multi_hand_landmarks

    def get_gesture(self, hand_landmarks):
        if hand_landmarks:
            finger_tips = [hand_landmarks[self.mp_hands.HandLandmark.INDEX_FINGER_TIP],
                           hand_landmarks[self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP],
                           hand_landmarks[self.mp_hands.HandLandmark.RING_FINGER_TIP],
                           hand_landmarks[self.mp_hands.HandLandmark.PINKY_TIP]]

            finger_count = sum(1 for tip in finger_tips if tip.y < hand_landmarks[self.mp_hands.HandLandmark.WRIST].y)

            return finger_count
        return 0