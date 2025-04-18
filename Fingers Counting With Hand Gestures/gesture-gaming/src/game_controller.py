class GameController:
    def __init__(self):
        self.is_jumping = False
        self.is_rolling = False
        self.position = 0  # Represents the horizontal position of the player

    def jump(self):
        self.is_jumping = True
        print("Jump action triggered!")

    def roll(self):
        self.is_rolling = True
        print("Roll action triggered!")

    def move_right(self):
        self.position += 1
        print(f"Moved right to position {self.position}!")

    def move_left(self):
        self.position -= 1
        print(f"Moved left to position {self.position}!")

    def reset_actions(self):
        self.is_jumping = False
        self.is_rolling = False
        print("Actions reset!")