import unittest
from src.hand_detector import HandDetector

class TestHandDetector(unittest.TestCase):
    def setUp(self):
        self.detector = HandDetector()

    def test_find_hands(self):
        # Test with a sample image or video frame
        frame = ...  # Load a sample frame
        hands = self.detector.find_hands(frame)
        self.assertIsInstance(hands, list)

    def test_get_gesture(self):
        # Test gesture recognition for different finger counts
        self.assertEqual(self.detector.get_gesture(1), 'jump')
        self.assertEqual(self.detector.get_gesture(2), 'roll')
        self.assertEqual(self.detector.get_gesture(3), 'move_right')
        self.assertEqual(self.detector.get_gesture(4), 'move_left')

if __name__ == '__main__':
    unittest.main()