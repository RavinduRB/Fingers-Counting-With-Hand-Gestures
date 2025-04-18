from selenium.webdriver.common.keys import Keys
import pyautogui

class GameController:
    def __init__(self):
        self.actions = {
            1: self.jump,
            2: self.roll,
            3: self.move_right,
            4: self.move_left
        }

    def execute_action(self, finger_count):
        if finger_count in self.actions:
            self.actions[finger_count]()

    def jump(self):
        pyautogui.press('space')

    def roll(self):
        pyautogui.press('down')

    def move_right(self):
        pyautogui.press('right')

    def move_left(self):
        pyautogui.press('left')