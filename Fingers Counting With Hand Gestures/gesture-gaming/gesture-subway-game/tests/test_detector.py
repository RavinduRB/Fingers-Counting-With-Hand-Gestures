def test_hand_detector():
    import cv2
    import mediapipe as mp
    from src.hand_detector import HandDetector

    # Initialize the HandDetector
    detector = HandDetector()

    # Create a test image (black image)
    test_image = cv2.imread('test_image.jpg')  # Replace with an actual test image path

    # Find hands in the test image
    processed_image = detector.find_hands(test_image)

    # Count fingers in the test image
    finger_count = detector.count_fingers()

    # Assertions to verify the functionality
    assert processed_image is not None, "Processed image should not be None"
    assert isinstance(finger_count, int), "Finger count should be an integer"
    assert finger_count >= 0, "Finger count should be non-negative"